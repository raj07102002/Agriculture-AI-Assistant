from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load PDF
loader = PyPDFLoader("data/wheat (1).pdf")
docs = loader.load()
print(f"Loaded {len(docs)} pages")

# Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

print(f"Created {len(chunks)} chunks")

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# FAISS
vector_store = FAISS.from_documents(
    chunks,
    embeddings
)

# Save Database
vector_store.save_local("vector_db")

print("✅ FAISS Database Created Successfully")