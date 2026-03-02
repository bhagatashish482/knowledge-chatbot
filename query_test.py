from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


def main():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectordb = Chroma(persist_directory="db", embedding_function=embeddings)
    query = input("Enter your query: ")
    results = vectordb.similarity_search(query)
    print("\nTop results:")

    for i, doc in enumerate(results):
        print(f"\nResult {i+1}:")
        print(f"Content: {doc.page_content}")
        print("-" * 50)


if __name__ == "__main__":
    main()
