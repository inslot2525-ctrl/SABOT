import streamlit as st

if (
    "logged_in" not in st.session_state
    or not st.session_state.logged_in
):
    st.switch_page("app.py")

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊"
)

st.title("📊 SalesMind Dashboard")

st.write(
    f"Welcome, {st.session_state.user}"
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "📄 Upload Documents",
        use_container_width=True
    ):
        st.switch_page(
            "pages/Upload.py"
        )

with col2:

    if st.button(
        "💬 Chat Agent",
        use_container_width=True
    ):
        st.switch_page(
            "pages/Chat.py"
        )

st.divider()

if st.button(
    "🚪 Logout",
    use_container_width=True
):
    st.session_state.clear()
    st.switch_page("app.py")