import streamlit as st


def render():
    with st.sidebar:
        st.subheader("Contact Creator")
        choice = st.radio(
            "Select preferred medium?",
            ["Email", "WhatsApp DM"],
            captions=["Send an email", "You Prefer whatsapp?"],
        )

        if choice == "Email":
            st.write(
                """
                    - :e-mail: [wed3v@sammykingx.com.ng](mailto:hellosammy@sammykingx.com.ng)
                """
            )

        elif choice == "WhatsApp DM":
            st.write(
                """
                    - :left_speech_bubble: [Let's Talk](https://wa.link/vlfk1a)
                """
            )

        else:
            st.write(
                """
                    :upside_down_face: You didn't select any option.
                """
            )

        st.link_button(
            ":heart: Support Wy Work",
            "https://selar.co/showlove/sammykingx",
            help="show some love for the workwiz project :white_check_mark:",
            type="primary",
        )
