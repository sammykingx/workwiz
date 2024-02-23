import streamlit as st
from models.pricing_calculator import PricingCalculator
from components import app_sidebar, contact_form, menu_items
from database import db_connection
from streamlit_option_menu import option_menu
import re, time
import utils


EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9._-]+@[a-z]+\.[a-z]{2,}$")
USERS = ["sam@sam.co", "me@samm.com"]


def render() -> None:
    """renders content"""

    # --- render sidebar ---
    menu_items.render()
    app_sidebar.render()
    contact_form.render()

    # --- render page content ---
    st.subheader(
        ":smiley: Cost Estimation now stressfree.", anchor=False
    )
    st.title(":control_knobs: Project Cost Estimator", anchor=False)
    st.write(
        """
            - As a tech freelancer, accurately estimating project budgets is 
            critical to achieving profitability and long-term success. 

            - :orange[WorkWiz] helps freelancers in estimating project costs by 
            factoring in variables such as project timeline, developer experience, 
            skill level, project complexity, inflation, etc. Thereby fostering data-driven 
            decision-making and strategic planning.
        """
    )

    video_col, login_col = st.columns(2, gap="medium")
    if "is_verified" not in st.session_state:
        with video_col:
            "#"
            with st.expander("Getting Started - 01"):
                st.subheader(
                    "Workwiz - User Authentication", anchor=False
                )
                st.video("https://youtu.be/01BMlKl2YX0")

            with st.expander("Using Workwiz Estimator - 02"):
                st.subheader(
                    "Using The Project Estimator", anchor=False
                )
                st.video("https://youtu.be/qgyYAkLJsTE")

        with login_col:
            # "#"
            st.subheader(
                "Help us protect :orange[workwiz] from bots",
                anchor=False,
            )
            # user_email = st.text_input(
            #        ":email: __Enter email__",
            #        help="Enter a valid email address to get passcode",
            #        placeholder = "sammykingx@gmail.com",
            #    )

            if "user_email" not in st.session_state:
                user_email = st.text_input(
                    ":email: __Enter email__",
                    help="Enter a valid email address to get passcode",
                    placeholder="sammykingx@gmail.com",
                )

                if user_email:
                    if not EMAIL_PATTERN.match(user_email):
                        st.error("Invalid email provided")
                        st.stop()

                    verified_email = collection.find_one(
                        {"email": user_email}
                    )
                    # if user_email in USERS:
                    if verified_email:
                        st.session_state["is_verified"] = True
                        st.info(f":white_check_mark: Verified")
                        with st.spinner("Just a moment"):
                            time.sleep(3)

                        st.rerun()

                    st.session_state["user_email"] = user_email
                    st.session_state["user_otp"] = str(
                        utils.get_otp()
                    )

                    with st.spinner("sending passcode to email"):
                        resp = utils.send_user_otp(
                            "email_verification.html",
                            "Email OTP Verification - Action Required",
                            st.session_state["user_email"],
                            user_otp=st.session_state["user_otp"],
                        )

                        # msg = utils.load_email_template(
                        #        "email_verification.html",
                        #        user_otp=st.session_state["user_otp"]
                        #    )
                        # resp = utils.send_email(
                        #        msg,
                        #        st.session_state["user_email"],
                        #        "Email OTP Verification - Action Required")
                    if not resp:
                        st.stop()

                    st.session_state["otp_sent"] = True

            if "user_email" in st.session_state:
                # st.write(f"Passcode = {st.session_state['user_otp']}")
                st.success(
                    f"Passcode sent to {st.session_state['user_email']}, check your email"
                )

                if not st.session_state["otp_sent"]:
                    if st.button("Resend Passcode"):
                        with st.spinner("sending passcode to email"):
                            resp = utils.send_user_otp(
                                "email_verification.html",
                                "Email OTP Verification - Action Required",
                                st.session_state["user_email"],
                                user_otp=st.session_state["user_otp"],
                            )
                            # msg = utils.load_email_template(
                            #        "email_verification.html",
                            #        user_otp=st.session_state["user_otp"]
                            #    )
                            # resp = utils.send_email(
                            #        msg,
                            #        st.session_state["user_email"],
                            #        "Email OTP Verification - Action Required")
                        if not resp:
                            st.stop()

                        st.session_state["otp_sent"] = True

                email_passcode = st.text_input(
                    "__Enter Passcode__",
                    help="Enter most recent passcode sent to your email",
                    placeholder="94567",
                )

                if email_passcode:
                    if email_passcode != st.session_state["user_otp"]:
                        st.error("Invalid Passcode", icon="💔")
                        st.stop()

                    else:
                        collection.insert_one(
                            {"email": st.session_state["user_email"]}
                        )
                        # USERS.append(st.session_state["user_email"])
                        st.session_state["is_verified"] = True
                        del st.session_state["user_email"]
                        del st.session_state["user_otp"]
                        del st.session_state["otp_sent"]
                        st.info(f":white_check_mark: Verified")
                        time.sleep(3)
                        st.rerun()
        "#"

    else:
        render_calculator()
        # st.toast("Congratulations", icon="🎉")
        # selected = option_menu(
        #        menu_title = "Next Up",
        #        options = ["Donate", "Share", "Home"],
        #        icons = ["cup-hot", "share", "house"],
        #        menu_icon = "emoji-smile",
        #        orientation = "horizontal",
        #    )

        # if selected == "Home":
        #    st.switch_page("main.py")


def render_calculator() -> None:
    """render calculator"""

    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader(
                "Let's talk about you first :smiley:", anchor=False
            )

            skill_level = st.selectbox(
                "Your skill Proficeincy",
                options=(
                    "Beginner",
                    "Junior",
                    "Intermediate",
                    "Advanced",
                ),
                index=1,
            )

            if skill_level == "Beginner":
                st.error(
                    "You should focus on learning the basics before taking projects",
                    icon="💝",
                )

            project_experience = st.radio(
                "Project Proficiency",
                options=("Small", "Standard", "Enterpise_Level"),
                help="What type of application have you built",
            )

        with col2:
            st.subheader(
                "Let's know the project scope :mag:", anchor=False
            )
            complexity_level = st.selectbox(
                "Complexity level",
                placeholder="select from dropdwon",
                options=("Easy", "Standard", "Hard"),
            )

            timeline = st.slider(
                "What's the project timeline in weeks?",
                min_value=2,
                max_value=52,
            )

            st.success(f"you selected {timeline} weeks")

        with col3:
            available_currency = {
                "NGN": "₦",
                "USD": "$",
                "GBP": "£",
                "EUR": "€",
            }
            st.subheader("Let's talk cost :moneybag:", anchor=False)
            currency_choice = st.selectbox(
                "Choose the currency",
                options=list(available_currency.keys()),
                index=1,
                placeholder="choose currency",
            )

            project_cost = st.number_input(
                "What's the market cost",
                min_value=150.00,
                step=None,
                placeholder="estimated project worth",
                help="enter price cost based on the project value and timeline",
            )

            st.success(f"{currency_choice} {project_cost:,}")

    # cost calculation
    project_estimator = PricingCalculator(
        skill_level.lower(), project_cost, (timeline * 7)
    )

    project_estimator.increase_rate(
        project_experience.lower(),
        complexity_level.lower(),
    )

    estimated_cost = project_estimator.calculate()
    st.title(
        f":orange[Estimate] = :green[{available_currency[currency_choice]} "
        f"{estimated_cost:,}]",
        anchor=False,
    )
    "#"


if __name__ == "__main__":
    st.set_page_config(
        page_title="WorkWiz - Pricing Calculator",
        page_icon=":star:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    db = db_connection().get_database("workwiz_app")
    collection = db.get_collection("users")
    # st.write(list(collection.find()))

    with open("assets/style.css", "r") as css_file:
        st.markdown(
            f"<style>{css_file.read()}</style>",
            unsafe_allow_html=True,
        )

    render()
