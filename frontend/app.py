import streamlit as st

st.set_page_config(
    page_title="SABOT AI",
    page_icon="",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown(
    """
<style>

.stApp {
    background-color: #0f172a;
    color: white;
}

.main-title {
    font-size: 3.2rem;
    font-weight: 700;
    color: white;
    text-align: center;
}

.sub-title {
    font-size: 1.2rem;
    color: #94a3b8;
    text-align: center;
    margin-bottom: 40px;
}

.feature-card {
    background: #1e293b;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
}

.login-card {
    background: #111827;
    padding: 30px;
    border-radius: 15px;
    border: 1px solid #334155;
}

.demo-box {
    background: #1e293b;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 20px;
}

</style>
""",
    unsafe_allow_html=True
)

# =====================================
# SESSION STATE
# =====================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =====================================
# HERO SECTION
# =====================================

st.markdown(
    """
<div class="main-title">
 SABOT AI
</div>

<div class="sub-title">
AI-Powered Sales Intelligence Platform
</div>
""",
    unsafe_allow_html=True
)

# =====================================
# LAYOUT
# =====================================

left, right = st.columns([1.5, 1])

# =====================================
# LEFT SIDE
# =====================================

with left:

    st.markdown(
        """
### 🎯 What This Application Does

SABOT AI enables organizations to transform PDFs,
sales documents, policy manuals, product catalogs,
pricing sheets and knowledge bases into an intelligent
AI assistant.

The system can:

- 📄 Ingest PDF documents
- 🔍 Build a semantic vector database
- 🤖 Answer questions using Retrieval Augmented Generation (RAG)
- 📚 Provide source-backed responses
- 💬 Act as a sales support assistant
- 📈 Capture potential customer leads
- ⚡ Deliver instant answers from enterprise knowledge

### 🛠 Tech Stack

- FastAPI
- Streamlit
- FAISS Vector Database
- Sentence Transformers
- LangChain
- Retrieval Augmented Generation (RAG)
- Python

### 👨‍⚖️ For Judges

Upload any business document and immediately
chat with it using natural language.

The AI retrieves relevant sections and generates
context-aware answers directly from the uploaded
knowledge base.
"""
    )

# =====================================
# RIGHT SIDE
# =====================================

with right:

    st.markdown(
        """
<div class="login-card">
<h2>🔐 Demo Login</h2>
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="demo-box">
<b>Demo Credentials</b><br><br>

Username: <b>demo</b><br>
Password: <b>demo123</b>
</div>
""",
        unsafe_allow_html=True
    )

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Login",
        use_container_width=True
    ):

        if (
            username == "demo"
            and password == "demo123"
        ):

            st.session_state.logged_in = True

            st.success(
                "Login Successful"
            )

            st.switch_page(
                "pages/chat.py"
            )

        else:

            st.error(
                "Invalid Credentials"
            )

st.divider()

st.caption(
    "SABOT AI • Retrieval Augmented Generation for Enterprise Sales Enablement"
)