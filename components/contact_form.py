import re, utils, streamlit as st


EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9._-]+@[a-z]+\.[a-z]{2,}$")


def render() -> None:
    """renders the contact form in the side bar"""

    with st.sidebar:
        st.subheader(":label: __Suggest A Feature__")
        with st.form("feature_form"):
            feature_name = st.text_input("Feature Name", max_chars=50)
            email = st.text_input("Your Email")
            description = st.text_area(
                "Give a quick overview so we understand"
            )
            submit = st.form_submit_button(":smiley: Log Feature")

            if submit:
                if not EMAIL_PATTERN.match(email):
                    st.error("Invalid email provided")

                else:
                    with st.spinner(":clock2: Wait a moment"):
                        msg = utils.load_email_template(
                            "feature_request.html",
                            feature_name=feature_name,
                            email=email,
                            description=description,
                        )

                        resp = utils.send_email(
                            msg,
                            st.secrets["CONTACT_EMAIL"],
                            "FEATURE REQUEST - workwiz",
                        )

                        if resp:
                            st.toast(
                                f"Thanks for your suggestion :+1:"
                            )
