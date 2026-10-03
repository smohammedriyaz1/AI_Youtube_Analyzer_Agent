# 🎥 AI YouTube Analyzer Agent

An **AI-powered YouTube Video Analyzer** built with **Python, Streamlit, and Agentic AI**.

This application allows users to provide a YouTube video URL and receive an AI-generated analysis of the video's content through an intelligent AI agent.

---

## 🚀 Overview

The **AI YouTube Analyzer Agent** is designed to simplify the process of understanding long YouTube videos.

Instead of manually watching an entire video to identify important information, users can provide a YouTube URL and let the AI agent analyze the content and generate a structured report.

### Core Workflow

```text
YouTube Video URL
        ↓
   AI Agent
        ↓
Video Content Analysis
        ↓
Summary & Insights
        ↓
Structured AI Report
```

---

## ✨ Features

* 🎥 Analyze YouTube videos using a URL
* 🤖 AI-powered video analysis
* 🧠 Agentic AI workflow
* 📝 Automatic content summarization
* 🔑 Identify important concepts and key points
* 💡 Generate useful insights
* 📊 Structured analysis reports
* 🖥️ Interactive Streamlit interface
* 🔐 Secure API-key configuration using environment variables

---

## 🛠️ Tech Stack

### Programming

* Python

### AI / Generative AI

* Agentic AI
* Generative AI
* Large Language Models (LLMs)
* Prompt Engineering
* AI Agents

### Frameworks & Libraries

* Streamlit
* Agno
* OpenAI
* Groq
* Python-dotenv

### Development Tools

* Git
* GitHub
* VS Code

---

## 🏗️ Project Architecture

```text
                    👤 User
                      │
                      ▼
             ┌─────────────────┐
             │ Streamlit App   │
             │    app.py       │
             └────────┬────────┘
                      │
                 YouTube URL
                      │
                      ▼
          ┌──────────────────────┐
          │  YouTube AI Agent    │
          │ Youtube_Analyzer.py   │
          └──────────┬───────────┘
                     │
                     ▼
              🧠 LLM Reasoning
                     │
                     ▼
          ┌──────────────────────┐
          │ Video Content        │
          │ Analysis              │
          └──────────┬───────────┘
                     │
                     ▼
             📊 AI Analysis
                     │
                     ▼
               👤 User
```

---

## 📂 Project Structure

```text
AI_Youtube_Analyzer_Agent/
│
├── app.py
│   └── Streamlit user interface
│
├── Youtube_Analyzer.py
│   └── AI agent configuration and video analysis logic
│
├── .gitignore
│   └── Prevents sensitive files from being committed
│
├── requirements.txt
│   └── Project dependencies
│
└── README.md
    └── Project documentation
```

> API keys and `.env` files are intentionally excluded from the repository.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/smohammedriyaz1/AI_Youtube_Analyzer_Agent.git
```

### 2. Navigate to the project

```bash
cd AI_Youtube_Analyzer_Agent
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project directory:

```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

### ⚠️ Security

**Never upload your `.env` file to GitHub.**

The `.gitignore` file is configured to prevent environment files and sensitive information from being committed.

Example:

```gitignore
.env
.env.*
!.env.example

__pycache__/
*.pyc
```

For other developers, create an `.env.example` file:

```env
OPENAI_API_KEY=
GROQ_API_KEY=
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🖥️ How to Use

### Step 1

Open the application.

### Step 2

Enter a YouTube video URL.

Example:

```text
https://www.youtube.com/watch?v=JkaxUblCGz0
```

### Step 3

Click:

```text
🚀 Analyze Video
```

### Step 4

The AI agent processes the video and generates an analysis.

### Step 5

Review the generated report.

---

## 🤖 Agentic AI Workflow

The project demonstrates the basic concept of an AI agent:

```text
                User Request
                     │
                     ▼
              Understand Task
                     │
                     ▼
              AI Agent Reasoning
                     │
                     ▼
            Analyze Video Content
                     │
                     ▼
             Generate Insights
                     │
                     ▼
              Final AI Report
```

The agent-based approach makes the application extensible for adding additional tools, memory, specialized agents, and more advanced workflows.

---

## 📊 Example Use Cases

### 🎓 Students

Analyze educational videos and quickly identify:

* Important concepts
* Learning points
* Key explanations
* Revision notes

### 💻 Developers

Analyze:

* Programming tutorials
* Technical presentations
* AI/ML videos
* Software engineering content

### 📚 Researchers

Use AI-generated summaries to quickly understand video content and identify topics for deeper research.

### 📈 Professionals

Analyze:

* Webinars
* Presentations
* Industry discussions
* Educational content

---

## 🔮 Future Improvements

Planned improvements include:

* [ ] Interactive AI chat about the analyzed video
* [ ] Video summary and key-points tabs
* [ ] Downloadable analysis reports
* [ ] Timestamp-based insights
* [ ] Automatic transcript processing
* [ ] Multiple specialized AI agents
* [ ] RAG-based video question answering
* [ ] Conversation memory
* [ ] YouTube metadata extraction
* [ ] Improved Streamlit UI
* [ ] Cloud deployment
* [ ] Video comparison
* [ ] Automatic learning notes generation

---

## 🌐 Deployment

The application can be deployed using platforms that support Python and Streamlit applications.

For deployment, configure API keys as platform secrets/environment variables rather than storing them in the source code.

---

## 🎯 Learning Outcomes

Through this project, I explored practical implementation of:

* Agentic AI
* Generative AI
* Large Language Models
* AI agents
* Prompt engineering
* API integration
* Streamlit application development
* Environment-variable management
* Git and GitHub
* AI-powered content analysis

---

## 👨‍💻 Author

### Shaik Mohammed Riyaz

**AI/ML Engineer | Generative AI Developer | Java & Python Developer**

Interested in:

* Artificial Intelligence
* Machine Learning
* Generative AI
* Agentic AI
* RAG
* Python
* Java
* Data Structures & Algorithms
* Full-Stack Development

### GitHub

https://github.com/smohammedriyaz1

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is created for educational and development purposes.
