# 🤖 Funny AI Chatbot

A simple conversational AI chatbot built with **Python, Streamlit, LangChain, and Groq**.

The chatbot maintains conversation history using LangChain's message objects, allowing the AI to remember previous messages during the current session. It is designed with a sarcastic and witty personality to make conversations more engaging.

## ✨ Features

- 💬 Conversational AI chat interface
- 🧠 In-memory conversation history
- 👤 Human, AI, and System message handling
- 😂 Sarcastic and witty AI personality
- ⚡ Powered by Groq's LLM API
- 🔗 Built using LangChain
- 🎨 Clean Streamlit web interface
- 🔐 API key management using `.env`
- 🚪 Easy chat session control

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM integration and message management |
| Groq | LLM inference |
| Streamlit | Web-based chat interface |
| python-dotenv | Environment variable management |

## 🧠 How It Works

The chatbot maintains a list of structured LangChain messages:

```text
SystemMessage
      ↓
HumanMessage
      ↓
AIMessage
      ↓
HumanMessage
      ↓
AIMessage
```

Every time the user sends a message:

```text
User Input
    ↓
HumanMessage
    ↓
Conversation History
    ↓
Groq LLM
    ↓
AIMessage
    ↓
Conversation History
    ↓
Streamlit UI
```

The complete conversation history is passed to the LLM with every new request, allowing the chatbot to maintain context.

## 📁 Project Structure

```text
chatmodels/
│
├── app.py
├── README.md
│
└── .venv/              # Local virtual environment
```

> `.env` and `.venv` are intentionally excluded from GitHub.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/langchain-funny-chatbot.git
cd langchain-funny-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

You can use `.env.example` as a reference.

**Never commit your actual `.env` file or API keys to GitHub.**

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 💬 Example

```text
User:
What is Python?

AI:
Python? It's that programming language where
indentation decides whether your code lives or dies. 😏
```

## 🧩 Core LangChain Concepts Used

This project demonstrates several fundamental LangChain concepts:

- `ChatGroq`
- `SystemMessage`
- `HumanMessage`
- `AIMessage`
- `invoke()`
- Conversation history
- System prompts
- LLM integration

## 🚀 Future Improvements

Planned improvements include:

- 💾 Persistent conversation memory
- 🧠 Conversation summarization
- 🗄️ Database-backed chat history
- 🔄 Streaming AI responses
- 🧹 Clear conversation button
- 👥 Multiple conversation sessions
- 🔐 User authentication
- 📚 RAG-based knowledge retrieval
- 🤖 AI agents and tool calling

## 🎯 Learning Purpose

This project was created as a hands-on project for learning **Generative AI and LangChain**, with a focus on understanding how LLMs process structured conversation history and maintain context.

## 👨‍💻 Author

**Utsav Kashyap**

Interested in:

- Full Stack Development
- Generative AI
- LLM Applications
- RAG
- AI Engineering

---

⭐ If you found this project useful, consider giving the repository a star!