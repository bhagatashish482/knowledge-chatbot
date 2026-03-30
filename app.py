# app.py

import streamlit as st
from rag_chain import load_qa_chain

st.set_page_config(page_title="Personal Knowledge Bot")

st.title("🧠 Personal Knowledge Base Chatbot")


# Load chain once
@st.cache_resource
def get_chain():
    return load_qa_chain()


qa_chain = get_chain()

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
prompt = st.chat_input("Ask something about your documents...")

if prompt:
    # show user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    # get response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            result = qa_chain({"query": prompt})
            answer = result["result"]

            st.write(answer)

            # show sources
            with st.expander("Sources"):
                for doc in result["source_documents"]:
                    st.write(doc.metadata)

    st.session_state.messages.append({"role": "assistant", "content": answer})
