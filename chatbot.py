from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2
)

def ask_question(question):

    docs = retriever.invoke(question)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content