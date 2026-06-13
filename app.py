import streamlit as st
from chatbot import ask_question

st.set_page_config(
    page_title="Agriculture AI Assistant",
    page_icon="🌾"
)

# Custom CSS
st.markdown("""
<style>
h1 {
    font-size: 55px !important;
    color: #2E7D32;
    text-align: center;
}

p {
    font-size: 20px !important;
}

.stChatMessage {
    font-size: 18px !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🌾 Agriculture AI Assistant")

st.markdown(
    "<p style='text-align:center;'>AI-powered farming assistant using RAG + Groq + FAISS</p>",
    unsafe_allow_html=True
)

st.divider()

question = st.chat_input(
    "Ask your agriculture question..."
)

if question:

    with st.chat_message("user"):
        st.write(question)

    answer = ask_question(question)

    with st.chat_message("assistant"):
        st.write(answer)