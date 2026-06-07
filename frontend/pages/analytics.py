import streamlit as st

if (
    "logged_in" not in st.session_state
    or not st.session_state.logged_in
):
    st.switch_page("app.py")

st.title("📈 Analytics")

questions = len(
    st.session_state.get(
        "messages",
        []
    )
)

st.metric(
    "Messages",
    questions
)

st.info(
    "More analytics coming soon."
)