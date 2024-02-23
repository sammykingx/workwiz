from email.message import EmailMessage
from dotenv import load_dotenv
import streamlit as st
import jinja2, json, os, random, smtplib


load_dotenv()


@st.cache_resource
def load_json_file(file_path: str) -> dict:
    """loads the json file and returns a dict"""

    with open(file_path, "r") as file:
        file_data = json.load(file)

    return file_data


def get_otp() -> int:
    """returns a 5 digit integer"""

    return random.randint(10000, 99999)


def send_email(message, to_addr, subject, attachment=None) -> bool:
    """send email to a user mail addres using tls"""

    mail_msg = EmailMessage()
    load_dotenv()

    mail_msg["from"] = os.getenv("SMTP_MAIL")
    mail_msg["to"] = to_addr
    mail_msg["subject"] = subject
    mail_msg.add_alternative(message, subtype="html")

    try:
        with smtplib.SMTP_SSL(
            os.getenv("SMTP_HOST"), os.getenv("SMTP_PORT"), timeout=5
        ) as mail_server:
            try:

                mail_server.login(
                    os.getenv("SMTP_MAIL"), os.getenv("SMTP_PWD")
                )

                resp = mail_server.send_message(mail_msg)

            except smtplib.SMTPConnectError:
                st.error(
                    "Could not establish a connection with "
                    "mail server"
                )
                return False

            except smtplib.SMTPServerDisconnected as err:
                st.error("Disconnected from mail server")
                return False

            except smtplib.SMTPException as err:
                st.error("Email service unavailble")
                return False

    except TimeoutError as err:
        st.error(f"{err}: check internet connection")
        return False

    except Exception as err:
        st.error(f"{err}, check back later")
        return False

    return True


def load_email_template(template, **kwargs) -> str:
    """
    loads email template

    @template: the html template to load
    @kwargs: dynamic data to pass to html template
    """

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader("./templates")
    )
    template_obj = env.get_template(template)
    dynamic_data = template_obj.render(**kwargs)
    return dynamic_data


def send_user_otp(
    template: str, subject: str, email: str, **kwargs: dict
) -> bool:
    """
    loads the specified email 'template' with dynamic data specified
    by '**kwargs'.

    :template: the template name to load.
    :subject: The email subject.
    :email: Users Email address
    :kwargs: a dictionary or keyword args of the dyanmic data to
             render in email template.
    """

    msg = load_email_template(template, **kwargs)
    return send_email(msg, email, subject)
