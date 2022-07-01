import os
import base64


def image_base_64(image_path=None) -> str:

    image_path = os.path.abspath(image_path)
    with open(image_path, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read())
        base64_string = 'data:image/jpeg;base64,' + str(image_base64).split('\'')[1]
        print("base64_string", base64_string)
        return base64_string
