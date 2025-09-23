## 🧠 Agentic AI Researcher

Your autonomous research assistant that browses, reads, and writes academic papers — so you don’t have to.

Automate academic research with an AI agent that:

- 🔍 **Searches arXiv.org** for papers on any topic
- 📖 **Reads and comprehends PDFs** in depth using read_pdf
- 🧪 **Synthesizes findings** and performs novel research analysis
- 📄 **Exports a ready-to-publish paper** in LaTeX or PDF

Built with LangChain, LangGraph, and powered by Google’s Gemini models — this is your 24/7 AI Research Intern.

## 🚀 Quick Start

1. Clone the repository:

   ```bash
   git clone https://github.com/Muhammad-Junaid23/Agentic-AI-Researcher.git
   cd Agentic-AI-Researcher
   ```

2. Install dependencies with uv (ultra-fast Python package installer):

   ```bash
   uv sync
   ```

✅ This will:

- Create a virtual environment (if missing)
- Install all pinned dependencies from uv.lock
- Set up your environment exactly as tested

## Add your API keys:

Create a .env file in the root directory:

```bash
   GOOGLE_API_KEY=your_google_api_key_here
```

## Run the app:

```bash
   uv run streamlit run frontend.py
```

## 🛠️ Tech Stack

- AI Framework: LangChain + LangGraph for agentic workflows
- LLM: Google Gemini via langchain-google-genai
- PDF Processing: PyPDF2
- Environment: python-dotenv, uv for dependency management
- UI (Optional): Streamlit for interactive interface
- Python: >=3.11

## 🎯 Features

- arXiv Browser --
  Fetch latest or relevant papers by keyword, author, or category
- Deep PDF Reader --
  Extract and comprehend full paper content not just abstracts
- Research Synthesis --
  Compare papers, identify gaps, suggest novel directions
- Paper Writer --
  Generate structured, citation-ready drafts in academic format
- Export Ready --
  Output in LaTeX or PDF

## 🤝 Contributing

Contributions welcome! Please open an issue or PR for:

- New tool integrations (e.g., Semantic Scholar, ACL Anthology)
- Better PDF parsing (try llama-index or unstructured)
- Export formats (LaTeX templates, Overleaf sync)
- Evaluation metrics for generated papers
