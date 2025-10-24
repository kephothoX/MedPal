import os
from dotenv import load_dotenv

load_dotenv()

from twilio.rest import Client

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)


def sendWhatsappMessage(message: str) -> str:
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        content_sid="HXb5b62575e6e4ff6129ad7c8efe1f983e",
        body=f"{ message }",
        to="whatsapp:+254782544020",
    )

    return f"Message with CID: {message.sid } sent successfully."


if __name__ == "__main__":
    test_message = "Hello, this is a test WhatsApp message from MedPal."
    result = sendWhatsappMessage(test_message)
    print(result)
