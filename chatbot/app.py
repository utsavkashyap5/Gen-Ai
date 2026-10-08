import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

load_dotenv()


# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="Funny AI",
    page_icon="🤖",
    layout="centered"
)


# -------------------------------
# Custom CSS
# -------------------------------

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: #0f1117;
    }

    /* Header */
    .main-title {
        text-align: center;
        font-size: 2.4rem;
        font-weight: 700;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        color: #8b949e;
        margin-top: 5px;
        margin-bottom: 30px;
    }

    /* Chat messages */
    [data-testid="stChatMessage"] {
        border-radius: 14px;
        padding: 10px;
        margin-bottom: 10px;
    }

    /* Input */
    [data-testid="stChatInput"] {
        border-radius: 15px;
    }

</style>
""", unsafe_allow_html=True)


# -------------------------------
# Header
# -------------------------------

st.markdown(
    '<div class="main-title">🤖 Funny AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your sarcastic, witty AI companion.</div>',
    unsafe_allow_html=True
)


# -------------------------------
# LLM
# -------------------------------

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.6
)


# -------------------------------
# Initialize Chat History
# -------------------------------

if "history" not in st.session_state:

    st.session_state.history = [
        SystemMessage(
            content="""
            You are a funny assistant that is very sarcastic and witty.
            Keep your responses entertaining but helpful.
            """
        )
    ]


# -------------------------------
# Display Previous Messages
# -------------------------------

for message in st.session_state.history:

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):
            st.markdown(message.content)


# -------------------------------
# Chat Input
# -------------------------------

prompt = st.chat_input("Ask me something...")


if prompt:

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to history
    st.session_state.history.append(
        HumanMessage(content=prompt)
    )

    # Generate response
    response = llm.invoke(
        st.session_state.history
    )

    # Add AI response to history
    st.session_state.history.append(
        AIMessage(content=response.content)
    )

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response.content)