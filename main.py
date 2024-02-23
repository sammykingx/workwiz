import streamlit as st
from streamlit_lottie import st_lottie
from components import app_sidebar, contact_form, menu_items
import utils


def main() -> None:
    """application Homepage"""

    # sidebar rendering
    menu_items.render("main")
    app_sidebar.render()
    contact_form.render()

    # page body
    st.subheader(
        ":fire: say hello to your secret weapon",
        anchor=False,
    )

    st.title(
        ":blossom: workwiz - Empower Your Freelance Hustle :boom:",
        anchor=False,
    )

    with st.container(height=600, border=True):
        col1, col2 = st.columns(2)

        with col1:
            animation = utils.load_json_file(
                "assets/animations/happy_animations.json"
            )
            st_lottie(animation, height=500)

        with col2:
            "##"

            st.subheader(
                ":smiley: Easy to use project estimator",
                anchor=False,
            )

            st.write(
                """
                    - With our easy-to-use project estimator, estimating project costs has
                    never been simpler. No more guessing games or worrying about
                    undercharging for your hard work. With FreshFreelance, you can create
                    accurate estimates in minutes, giving you confidence and peace of mind.
                """
            )

            st.subheader(
                ":page_facing_up: Sleek invoice generator",
                anchor=False,
            )

            st.write(
                """
                    - Our sleek invoice generator takes the hassle out of
                    billing clients, so you can focus on what really matters: which
                    is __delivering top-quality work__ to your clients.
                """
            )

            st.subheader(
                ":briefcase: Resume Template Guide",
                anchor=False,
            )

            st.write(
                """
                    - Designed to simplify the creation process, __Workwiz__ ensures every
                    essential detail is included. Easily incorporate your unique experiences,
                    skills, and accomplishments and stand out from the competition with a
                    stunning resume that captures attention and leaves a lasting impression.
                """
            )

    st.balloons()

    "---"
    # tools section
    st.markdown(
        "<h2 style='text-align: center'>Available tools</h2>",
        unsafe_allow_html=True,
    )

    st.write("##")
    col1, col2, col3 = st.columns(3)

    with col1:
        animation = utils.load_json_file(
            "assets/animations/cost_animation.json"
        )
        st_lottie(animation, height=300)
        st.markdown(
            "<h3 style='text-align: center'>Cost Calculator</h3>",
            unsafe_allow_html=True,
        )

        if st.button(":muscle: Use Tool", key="tool_1"):
            st.switch_page("pages/pricing_calc.py")

        "#"

    with col2:
        animation = utils.load_json_file(
            "assets/animations/invoice_animation.json"
        )
        st_lottie(animation, height=300)
        st.markdown(
            "<h3 style='text-align: center'>Invoice Generator</h3>",
            unsafe_allow_html=True,
        )

        # st.link_button(":muscle: Use Tool", "/invoice_generator")

        if st.button(":muscle: Use Tool", key="tool_2"):
            st.switch_page("pages/invoice_generator.py")
        "#"

    with col3:
        animation = utils.load_json_file(
            "assets/animations/resume.json"
        )
        st_lottie(animation, height=300)
        st.markdown(
            """
                <h3 style='text-align: center'>Resume Template</h3>
            """,
            unsafe_allow_html=True,
        )

        if st.button(":muscle: Use Tool", key="tool_3"):
            st.switch_page("pages/resume_builder.py")
        "#"

    "---"

    # about creator section
    # st.markdown(
    #    "<h2 style='text-align: center'>Meet The Creator</h2>",
    #    unsafe_allow_html=True,
    # )

    st.image("./assets/images/sammykingx.png", width=200)
    st.markdown(
        "<h2 style='text-align: center'>Sammykingx</h2>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
            <p style='padding: 0 10px; text-align: center; font-size: 20px'>
                Hey there! I'm a skilled Backend Software Engineer who loves
                solving complex challenges and delivering top-notch solutions.
                With a knack for choosing the perfect tech stack, I build scalable
                and efficient systems that wow my clients. And guess what? I made
                <span style='color: #FF8E3A'>WorkWiz</span>, a totally awesome free
                tool to help freelancers up their game!!. Curious to see how I can
                level up your projects? Let's chat!
            </p>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    st.set_page_config(
        layout="wide",
        page_title="WorkWiz - Empower Your Freelance Hustle",
        page_icon=":star:",
        initial_sidebar_state="collapsed",
    )

    with open("assets/style.css", "r") as css_file:
        st.markdown(
            f"<style>{css_file.read()}</style>",
            unsafe_allow_html=True,
        )

    main()
