import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

if (
    "logged_in" not in st.session_state
    or not st.session_state.logged_in
):
    st.switch_page("app.py")

st.title("📄 Upload Documents")

uploaded_files = st.file_uploader(
    "Upload PDF Documents",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button(
    "Upload Documents"
):

    if uploaded_files:

        for file in uploaded_files:

            requests.post(
                f"{API_URL}/upload",
                files={
                    "file": (
                        file.name,
                        file,
                        "application/pdf"
                    )
                }
            )

        st.success(
            "Documents uploaded successfully"
        )

if st.button(
    "Build Knowledge Base"
):

    response = requests.post(
        f"{API_URL}/build-index"
    )

    if response.status_code == 200:

        st.success(
            "Knowledge Base Built Successfully"
        )

    else:

        st.error(
            response.text
        )

if st.button(
    "⬅ Back to Dashboard"
):

    st.switch_page(
        "pages/Dashboard.py"
    )