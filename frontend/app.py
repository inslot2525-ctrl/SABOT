import streamlit as st
import requests

st.title("AI Sales Representative")

query = st.text_input(
    "Ask a question"
)

if st.button("Send"):

    response = requests.post(
        "http://localhost:8000/chat",
        json={"query": query}
    )

    data = response.json()

    st.write("Intent:", data["intent"])

    st.write(data["answer"])

    if data["lead_capture"]:
        st.success(
            "High buying intent detected"
        )