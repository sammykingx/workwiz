import streamlit as st
from components import app_sidebar, contact_form, menu_items


def render() -> None:
    """renders page content"""

    # render sidebar
    menu_items.render()
    app_sidebar.render()
    contact_form.render()

    # render page body
    st.subheader(":muscle: stand out and get the gig")

    st.title(":briefcase: WorkWiz Resume Builder")
    st.write("- Making you look professional :pushpin:")

    st.info(":ok_hand: still cooking here")

    if st.button(":house: Home"):
        st.switch_page("main.py")


if __name__ == "__main__":
    st.set_page_config(
        page_title="WorkWiz - Resume Template",
        page_icon=":star:",
        layout="wide",
    )

    with open("assets/style.css", "r") as css_file:
        st.markdown(
            f"<style>{css_file.read()}</style>",
            unsafe_allow_html=True,
        )

    render()
