from default import Config as config
from typing import List
from requests import Response, post

class Mailgun:

    @classmethod
    def send_email(cls, email: List[str], subject: str, text: str, html: str) -> Response:
        return post(
            f"https://api.mailgun.net/v3/{config.MAILGUN_DOMAIN}/messages",
            auth=("api", config.MAILGUN_API_KEY),
            data={
                "from": f"{config.FROM_TITLE} <{config.FROM_EMAIL}>",
                "to": email,
                "subject": subject,
                "text": text,
                "html": html,
            },
        )