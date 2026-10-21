import streamlit as st

from main import ask_question, create_chatbot


# Step 1: Set the browser tab title and page layout.
st.set_page_config(page_title="PDF Chatbot", page_icon="📄")
st.title("📄 PDF Chatbot")
st.caption("Ask questions about the LangChain Beginner Study Guide.")


# Step 2: Load the PDF, Chroma database, and LLM only once per Streamlit server.
@st.cache_resource(show_spinner="Reading the PDF and preparing the chatbot...")
def load_chatbot():
    return create_chatbot()


try:
    vector_store, chain = load_chatbot()
except Exception as error:
    st.error("The chatbot could not start. Check your PDF file and GOOGLE_API_KEY.")
    st.exception(error)
    st.stop()


# Step 3: Save conversation messages between Streamlit page reruns.
if "messages" not in st.session_state:
    st.session_state.messages = []


# Step 4: Draw all messages already saved in this chat session.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Step 5: Get a new question and show its answer.
question = st.chat_input("Ask a question about the PDF")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = ask_question(question, vector_store, chain)
                answer = response.answer
                found_in_context = response.found_in_context
            except Exception as error:
                answer = "Sorry, I could not generate an answer. Please try again."
                found_in_context = True
                st.exception(error)

        st.write(answer)
        if not found_in_context:
            st.caption("This answer was not found in the PDF context.")

    st.session_state.messages.append({"role": "assistant", "content": answer})
