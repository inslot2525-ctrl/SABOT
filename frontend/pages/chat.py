import streamlit as st
import requests
import csv
from pathlib import Path

API_URL = "http://127.0.0.1:8000"

if (
    "logged_in" not in st.session_state
    or not st.session_state.logged_in
):
    st.switch_page("app.py")

st.set_page_config(
    page_title="SalesMind AI",
    page_icon="🚀",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🚀 SalesMind AI")

st.markdown(
    "Upload documents and start chatting with your AI Sales Agent."
)

# ==================================
# DOCUMENT UPLOAD
# ==================================

st.subheader(
    "📄 Upload Documents"
)

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button(
    "Build Knowledge Base"
):

    if uploaded_files:

        files = []

        for file in uploaded_files:

            files.append(
                (
                    "files",
                    (
                        file.name,
                        file,
                        "application/pdf"
                    )
                )
            )

        upload_response = requests.post(
            f"{API_URL}/upload",
            files=files
        )

        if upload_response.status_code == 200:

            build_response = requests.post(
                f"{API_URL}/build-index"
            )

            if build_response.status_code == 200:

                st.success(
                    "Knowledge Base Built Successfully"
                )

            else:

                st.error(
                    "Failed to build index"
                )

        else:

            st.error(
                "Upload failed"
            )

st.divider()

# ==================================
# CHAT
# ==================================

st.subheader(
    "💬 Chat"
)

for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):

        st.markdown(
            msg["content"]
        )

query = st.chat_input(
    "Ask a question..."
)

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message(
        "user"
    ):
        st.markdown(query)

    try:

        response = requests.post(
            f"{API_URL}/chat",
            json={
                "query": query
            },
            timeout=120
        )

        if response.status_code != 200:

            st.error(
                f"Backend Error: {response.status_code}"
            )

            st.code(
                response.text
            )

            st.stop()

        data = response.json()

        answer = data.get(
            "answer",
            "No answer returned."
        )

        source_text = ""

        if data.get(
            "sources"
        ):

            source_text += "\n\n---\n\n### 📚 Sources\n"

            for source in data[
                "sources"
            ]:

                source_text += f"""
#### 📄 {source.get('file')}

> {source.get('snippet')}
"""

        full_response = (
            answer
            + source_text
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": full_response
            }
        )

        with st.chat_message(
            "assistant"
        ):

            st.markdown(
                full_response
            )

        # Lead Capture

        if data.get(
            "lead_capture",
            False
        ):

            st.divider()

            st.subheader(
                "📞 Contact Sales"
            )

            name = st.text_input(
                "Name"
            )

            email = st.text_input(
                "Email"
            )

            company = st.text_input(
                "Company"
            )

            if st.button(
                "Submit"
            ):

                Path(
                    "storage"
                ).mkdir(
                    exist_ok=True
                )

                lead_file = (
                    "storage/leads.csv"
                )

                exists = Path(
                    lead_file
                ).exists()

                with open(
                    lead_file,
                    "a",
                    newline="",
                    encoding="utf-8"
                ) as f:

                    writer = csv.writer(
                        f
                    )

                    if not exists:

                        writer.writerow(
                            [
                                "name",
                                "email",
                                "company",
                                "query"
                            ]
                        )

                    writer.writerow(
                        [
                            name,
                            email,
                            company,
                            query
                        ]
                    )

                st.success(
                    "Lead Saved"
                )

    except Exception as e:

        st.error(
            str(e)
        )