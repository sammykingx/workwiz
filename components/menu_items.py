import streamlit as st


def render(page: str = None) -> None:
    """display the menu items and returns the selected option"""

    with st.sidebar:
        selected = st.selectbox(
                "__:orange[Select Tool]__",
                options = ["Make your Choice",
                           "Cost Estimator",
                           "Invoice Generator",
                           "Resume Builder",
                        ],
                placeholder = "Choose an option",
                help = "choose a tool you'll like to use on workwiz"
            )

        if not page:
            if st.button(":house: Home", type="primary", key="home-page"):
                st.switch_page("main.py")

    match selected:
        case "Cost Estimator":
            st.switch_page("pages/pricing_calc.py")

        case "Invoice Generator":
            st.switch_page("pages/invoice_generator.py")

        case "Resume Builder":
            st.switch_page("pages/resume_builder.py")
