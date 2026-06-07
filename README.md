🚀 SABOT AI
AI-Powered Sales Intelligence Platform using RAG, Vector Search, and Conversational AI

Transform static business documents into an intelligent sales assistant capable of answering questions, retrieving evidence-backed insights, and capturing potential leads.

🎥 Project Overview

Sales teams spend hours searching through:

Product catalogs
Pricing documents
Policy manuals
Compliance documents
Sales playbooks
Competitive intelligence reports

SalesMind AI converts these documents into a conversational knowledge base.

Upload PDFs → Build Knowledge Base → Ask Questions → Receive Context-Aware Answers

✨ Key Features
📄 Intelligent Document Ingestion

Upload business documents including:

Product Catalogs
Pricing Guides
Company Policies
Service Documentation
Compliance Documents
Sales Enablement Content
🧠 Retrieval-Augmented Generation (RAG)

Instead of hallucinating answers, the system:

Searches uploaded documents
Retrieves relevant chunks
Builds contextual responses
Returns evidence-backed answers
🔍 Semantic Search

Traditional keyword search fails when wording differs.

SalesMind AI uses:

Sentence Transformers
Dense Embeddings
FAISS Vector Search

to understand meaning rather than exact words.

💬 Conversational AI Assistant

Supports:

Policy Questions
Product Questions
Pricing Questions
Sales Queries
General Knowledge Base Search

Example:

User:
What are Amazon seller conduct policies?

AI:
Amazon requires sellers to:

• Provide accurate information
• Act fairly and honestly
• Avoid manipulating reviews
• Follow category restrictions
• Protect customer information
📚 Source Attribution

Every answer includes:

Document source
Retrieved evidence
Supporting snippets

This improves trust and transparency.

🎯 Lead Capture

When sales-oriented intent is detected:

Demo Requests
Pricing Requests
Purchase Intent

the system can automatically capture:

Name
Email
Company

for follow-up by the sales team.

⚙ Technology Stack
Layer	Technology
Frontend	Streamlit
Backend	FastAPI
Vector Database	FAISS
Embeddings	Sentence Transformers
Text Processing	LangChain
Document Parsing	PyPDF
Language Model	Gemini
Storage	CSV / Local Storage
Programming Language	Python
📂 Project Structure
SalesMind-AI/
│
├── api/
│   ├── main.py
│   ├── routes.py
│   ├── upload.py
│   └── build_index.py
│
├── agent/
│   ├── generator.py
│   ├── intent_router.py
│   ├── confidence.py
│   └── lead_capture.py
│
├── ingestion/
│   ├── ingest.py
│   ├── chunk.py
│   └── embed.py
│
├── retrieval/
│   └── hybrid_search.py
│
├── frontend/
│   ├── app.py
│   └── pages/
│       └── chat.py
│
├── uploads/
├── vectorstore/
├── storage/
└── README.md
🚀 Installation

Clone repository

git clone https://github.com/yourusername/SalesMind-AI.git

cd SABOT-AI

Create virtual environment

python -m venv .venv

Activate environment

Windows
.venv\Scripts\activate

Install dependencies

pip install -r requirements.txt
🔑 Environment Variables

Create:

.env

Add:

GEMINI_API_KEY=YOUR_API_KEY
▶ Running Backend
uvicorn api.main:app --reload

Backend:

http://127.0.0.1:8000
▶ Running Frontend
streamlit run app.py

Frontend:

http://localhost:8501
🧪 Demo Credentials
Username: demo
Password: demo123
📈 Future Enhancements
Multi-Document Collections

Support separate knowledge bases:

HR
Sales
Legal
Customer Support
Role-Based Access Control

Different permissions for:

Admin
Sales Representatives
Managers
CRM Integration

Connect with:

Salesforce
HubSpot
Zoho CRM
Advanced Analytics

Track:

Most Asked Questions
Lead Conversion Rate
Knowledge Gaps
Sales Trends
Multi-LLM Support

Support:

Gemini
GPT
Claude
Open Source Models
🏆 Why This Project Matters

Organizations generate thousands of pages of business knowledge.

Most of it remains buried inside PDFs.

SalesMind AI transforms static documents into an interactive, searchable, and intelligent assistant that enables teams to access information instantly, improve productivity, and accelerate decision-making.

👨‍💻 Author

Aditya

B.Tech Artificial Intelligence & Machine Learning

Focused on:

Generative AI
Retrieval-Augmented Generation
AI Agents
Machine Learning Systems
Production AI Applications
⭐ If you found this project useful, consider giving it a star.

SABOT AI — Turning Business Knowledge into Conversations. 🚀

This version reads like a serious portfolio project rather than a student assignment, which is exactly what recruiters and hackathon judges respond to.
