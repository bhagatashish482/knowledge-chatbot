from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings


def load_pdf(pdf_path):
    documents = []
    for pdf_file in pdf_path.glob("*.pdf"):
        loader = PyPDFLoader(pdf_file)
        documents.extend(loader.load())
    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(documents)


def create_embeddings():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embeddings


def main():
    print("Loading documents...")

    data_dir = Path("data")
    pdf_files = list(data_dir.glob("*.pdf"))

    loaded_documents = load_pdf(data_dir)
    print(f"Loaded {len(loaded_documents)} pages")

    chunks = split_documents(loaded_documents)
    print(f"Split into {len(chunks)} chunks")

    embeddings = create_embeddings()
    print(f"Embeddings model created")


if __name__ == "__main__":
    main()
