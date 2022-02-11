from flask_api import status
from .client_exception import ClientException

FACE_NOT_RECOGNIZED = ClientException(
    status_code=status.HTTP_400_BAD_REQUEST,
    message="It is not possible to recognize a face on the image.")

EYE_NOT_RECOGNIZED = ClientException(
    status_code=status.HTTP_400_BAD_REQUEST,
    message="It is not possible to recognize an eye on the image.")

DATA_EMPTY = ClientException(
    status_code=status.HTTP_400_BAD_REQUEST,
    message="Client sent an empty image data.")
