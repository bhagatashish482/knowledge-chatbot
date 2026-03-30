from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def load_vector_db():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectordb = Chroma(persist_directory="db", embedding_function=embeddings)
    return vectordb


def retrieve_context(query, vectordb, k=3):
    results = vectordb.similarity_search(query, k=k)
    context = "\n".join([doc.page_content for doc in results])
    return context


def generate_response(query, context):
    llm = ChatOpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        model="llama-3.3-70b-versatile",
    )

    prompt = f"""
    You are a helpful assistant that can answer questions about the following context:
    {context}
    Question: {query}
    Answer:
    """

    response = llm.invoke(prompt)
    return response.content


def main():
    print("Welcome to the chatbot!")
    vectordb = load_vector_db()
    print("RAG chatbot is ready! Type 'exit' to end the chat.\n")
    while True:
        query = input("Enter your query: ")
        if query.lower() == "exit":
            break

        context = retrieve_context(query, vectordb, k=3)
        response = generate_response(query, context)
        print("\nResponse:")
        print(response)
        print("\n")


if __name__ == "__main__":
    main()
