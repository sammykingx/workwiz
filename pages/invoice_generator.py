import streamlit as st
from components import app_sidebar, contact_form, menu_items


def render() -> None:
    """renders page content"""

    # render sidebar
    menu_items.render()
    app_sidebar.render()
    contact_form.render()

    # page body
    st.subheader(":white_heart: Focus on what really matters")

    st.title(":scroll: Invoice Generator")
    st.write(" - It's sleek, effective and reliable :hugging_face:")

    st.info(":ok_hand: still cooking here")

    if st.button(":house: Home"):
        st.switch_page("main.py")


if __name__ == "__main__":
    st.set_page_config(
        page_title="WorkWiz - Invoice Generator",
        page_icon=":star:",
        layout="wide",
    )

    with open("assets/style.css", "r") as css_file:
        st.markdown(
            f"<style>{css_file.read()}</style>",
            unsafe_allow_html=True,
        )

    render()
