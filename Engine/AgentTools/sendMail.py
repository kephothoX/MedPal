import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

SENDER_MAIL = f"{os.environ.get('DEV_EMAIL')}"
SENDER_PASSWORD = f"{os.environ.get('DEV_EMAIL_APP_PASSWORD')}"


def sendEmail(receiver_email: str, subject: str, body: str) -> str:
    """
    Send an email to the specified receiver.

    Args:
        receiver_email (str): The email address of the receiver.
        subject (str): The subject of the email.
        body (str): The body content of the email.
    Returns:
        str: Status message indicating success or failure.
    """
    # Create message container
    message = MIMEMultipart()
    message["From"] = SENDER_MAIL
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the email body as plain text
    message.attach(MIMEText(body, "plain"))

    server = None
    try:
        # Connect to SMTP server with TLS encryption (example using Gmail SMTP)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        if not SENDER_MAIL or not SENDER_PASSWORD:
            raise ValueError(
                "Sender email or password not set in environment variables."
            )
        server.login(SENDER_MAIL, SENDER_PASSWORD)

        # Send email and close connection
        server.send_message(message)
        return "Email sent successfully."
    except Exception as e:
        return f"Failed to send email: {e}"
    finally:
        if server is not None:
            try:
                server.quit()
            except Exception:
                pass
