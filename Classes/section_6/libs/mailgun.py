from typing import List
from requests import Response, post

from default import Config as config
from libs.strings import gettext


class MailGunException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Mailgun:

    @classmethod
    def send_email(cls, email: List[str], subject: str, text: str, html: str) -> Response:
        if config.MAILGUN_API_KEY is None:
            raise MailGunException(config.MAILGUN_API_KEY)

        if config.MAILGUN_DOMAIN is None:
            raise MailGunException(config.MAILGUN_DOMAIN)

        response = post(
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
        if response.status_code != 200:
            raise MailGunException(config.ERRO_SENDING_EMAIL)

        return response