import os

class Config:
    """
    Base configuration, this class contains most of the variables and default values.
    """
    DATA_BASE_URI = os.environ.get('DATA_BASE_URI')
    APP_SECRET_KEY = os.environ.get('APP_SECRET_KEY')

    USER_ALREADY_EXISTS = os.environ.get('USER_ALREADY_EXISTS')
    EMAIL_ALREADY_EXISTS = os.environ.get('EMAIL_ALREADY_EXISTS')
    SUCCESS_REGISTER_MESSAGE = os.environ.get('SUCCESS_REGISTER_MESSAGE')
    USER_NOT_FOUND = os.environ.get('USER_NOT_FOUND')
    USER_DELETED = os.environ.get('USER_DELETED')
    INVALID_CREDENTIALS = os.environ.get('INVALID_CREDENTIALS')
    USER_LOGGED_OUT = os.environ.get('USER_LOGGED_OUT')
    NOT_CONFIRMED_ERROR = os.environ.get('NOT_CONFIRMED_ERROR')
    USER_CONFIRMED = os.environ.get('USER_CONFIRMED')
    FAILED_TO_CREATE = os.environ.get('FAILED_TO_CREATE')

    NAME_ALREADY_EXISTS = os.environ.get('NAME_ALREADY_EXISTS')
    ERROR_INSERTING = os.environ.get('ERROR_INSERTING')
    STORE_NOT_FOUND = os.environ.get('STORE_NOT_FOUND')
    STORE_DELETED = os.environ.get('STORE_DELETED')

    MAILGUN_DOMAIN =  os.environ.get('MAILGUN_DOMAIN')
    MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
    FROM_TITLE = os.environ.get('FROM_TITLE')
    FROM_EMAIL = os.environ.get('FROM_EMAIL')
    FAILED_LOAD_API_KEY = os.environ.get('FAILED_LOAD_API_KEY')
    FAILED_LOAD_DOMAIN = os.environ.get('FAILED_LOAD_DOMAIN')
    ERRO_SENDING_EMAIL = os.environ.get('ERRO_SENDING_EMAIL')

    NOT_FOUND = os.environ.get('NOT_FOUND')
    EXPIRED = os.environ.get('EXPIRED')
    ALREADY_CONFIRMED = os.environ.get('ALREADY_CONFIRMED')
    RESEND_SUCCESSFUL = os.environ.get('RESEND_SUCCESSFUL')
    RESEND_FAIL = os.environ.get('RESEND_FAIL')
    CONFIRMATION_EXPIRATION_DELTA = os.environ.get('CONFIRMATION_EXPIRATION_DELTA')