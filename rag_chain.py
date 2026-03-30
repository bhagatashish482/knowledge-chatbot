from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def load_qa_chain():
    """Load the QA chain with retrieval and generation components."""

    # Initialize embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load vector database
    vectordb = Chroma(persist_directory="db", embedding_function=embeddings)

    # Initialize LLM with Groq via OpenAI interface
    llm = ChatOpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        model="llama-3.3-70b-versatile",
        temperature=0.1,
    )

    # Create retriever
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    # Create custom prompt template
    prompt_template = """
    You are a helpful AI assistant. Use the following context to answer the question.
    If you cannot find the answer in the context, say "I don't have enough information to answer that question."
    
    Context: {context}
    
    Question: {question}
    
    Answer:"""

    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # Helper function to format documents
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # Create the chain using LCEL (LangChain Expression Language)
    def qa_chain_func(inputs):
        query = inputs["query"]

        # Retrieve documents using the correct method
        docs = retriever.invoke(query)

        # Format context
        context = format_docs(docs)

        # Generate response
        response = llm.invoke(prompt.format(context=context, question=query))

        return {"result": response.content, "source_documents": docs}

    return qa_chain_func


def get_vector_store():
    """Get the vector store for direct access if needed."""
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma(persist_directory="db", embedding_function=embeddings)

    return vectordb
