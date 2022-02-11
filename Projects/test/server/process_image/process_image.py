import base64
import random
import re
import cv2
import os
import numpy as np

from typing import Optional, Union
from io import BytesIO
from PIL import Image

from server.custom.custom_exceptions import FACE_NOT_RECOGNIZED, EYE_NOT_RECOGNIZED, DATA_EMPTY


class Googlyfier:
    LOAD_ALGORITHM_FACE = cv2.CascadeClassifier(
        os.path.abspath('process_image/haarcascades/haarcascade_frontalface_default.xml'))
    LOAD_ALGORITHM_EYE = cv2.CascadeClassifier(
        os.path.abspath('process_image/haarcascades/haarcascade_eye.xml'))

    PICTURE_HEIGHT = 800
    PICTURE_WIDTH = 600

    GOOGLY_EYES_AVAILABLE = ['googly_eye_a', 'googly_eye_b']

    Int_Float = Union[int, float]

    def __init__(self):
        self._googly_eye_height = 0
        self._googly_eye_width = 0

    def _resize(self, image, height: int, width: int):
        return cv2.resize(image, (height, width))

    def _change_color(self, image, color_convert):
        return cv2.cvtColor(image, color_convert)

    def _get_element(self, algorithm, grey_image, scale_factor: Optional[Int_Float] = 1.05, min_neighbors: int = 3):
        return algorithm.detectMultiScale(grey_image, scale_factor, min_neighbors)

    def _check_no_element(self, element) -> bool:
        number_elements = len(element)
        return True if number_elements < 1 else False

    def _set_googly_size(self, faces):
        limit = 3
        number_faces = len(faces)
        one_face = 0.12
        two_faces = 0.09
        more_faces = 0.03
        number_sizes = [one_face, two_faces, more_faces]
        if number_faces < limit:
            self._googly_eye_height = int(self.PICTURE_HEIGHT * number_sizes[number_faces - 1])
            self._googly_eye_width = int(self.PICTURE_WIDTH * number_sizes[number_faces - 1])
        elif number_faces > limit:
            self._googly_eye_height = int(self.PICTURE_HEIGHT * number_sizes[-1])
            self._googly_eye_width = int(self.PICTURE_WIDTH * number_sizes[-1])

    def _select_googly_eye(self, count: int) -> str:
        googly_eye_left = random.choice(self.GOOGLY_EYES_AVAILABLE)
        googly_eye_right = random.choice(self.GOOGLY_EYES_AVAILABLE)
        return googly_eye_left if count % 2 == 0 else googly_eye_right

    def _change_googly_size(self):
        sizes = [0.85, 0.95, 1, 1.05]
        self._googly_eye_height = int(self._googly_eye_height * random.choice(sizes))
        self._googly_eye_width = int(self._googly_eye_width * random.choice(sizes))

    def _change_picture(self, googly_picture: str, face_area, eye_x: int, eye_y: int):
        googly_eye_picture_path = os.path.abspath(f'process_image/pictures/{googly_picture}.png')
        googly_eye_image = cv2.imread(googly_eye_picture_path)
        googly_eye = self._resize(image=googly_eye_image, height=self._googly_eye_height, width=self._googly_eye_width)
        resized_googly_eye_height, resized_googly_eye_width, _ = googly_eye.shape

        crop = face_area[eye_y:eye_y + resized_googly_eye_height, eye_x:eye_x + resized_googly_eye_width]
        googly_eye_grey = self._change_color(image=googly_eye, color_convert=cv2.COLOR_BGR2GRAY)
        ret, maskeye = cv2.threshold(googly_eye_grey, 255, 255, cv2.THRESH_BINARY)

        background_picture = cv2.bitwise_and(crop, crop, mask=maskeye)
        mask_eye_inv = cv2.bitwise_not(maskeye)
        foreground_googly_eye = cv2.bitwise_and(googly_eye, googly_eye, mask=mask_eye_inv)

        complete_image = cv2.add(background_picture, foreground_googly_eye)
        face_area[eye_y:eye_y + resized_googly_eye_height, eye_x:eye_x + resized_googly_eye_width] = complete_image

    @staticmethod
    def convert_from_base64(data):
        if data:
            encoded_data = re.sub('^data:image/.+;base64,', '', data)
            np_array = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
        else:
            raise DATA_EMPTY

        return cv2.imdecode(np_array, cv2.COLOR_RGB2BGR)

    def generator(self, image_received):
        image_in_process = self._resize(image=image_received, height=self.PICTURE_HEIGHT, width=self.PICTURE_WIDTH)
        grey_face_picture = self._change_color(image=image_in_process, color_convert=cv2.COLOR_BGR2GRAY)
        faces = self._get_element(algorithm=self.LOAD_ALGORITHM_FACE, grey_image=grey_face_picture, scale_factor=1.1,
                                  min_neighbors=4)
        if self._check_no_element(element=faces):
            raise FACE_NOT_RECOGNIZED

        self._set_googly_size(faces=faces)
        for (face_x, face_y, face_width, face_height) in faces:
            face_area_image = image_in_process[face_y:face_y + face_height, face_x:face_x + face_width]
            grey_eyes_image = self._change_color(image=face_area_image, color_convert=cv2.COLOR_BGR2GRAY)
            eyes = self._get_element(algorithm=self.LOAD_ALGORITHM_EYE, grey_image=grey_eyes_image, scale_factor=3.5,
                                     min_neighbors=3)
            if self._check_no_element(element=eyes):
                raise EYE_NOT_RECOGNIZED

            count = 0
            for (eye_x, eye_y, _, _) in eyes:
                self._change_googly_size()
                self._change_picture(
                    googly_picture=self._select_googly_eye(count), face_area=face_area_image, eye_x=eye_x, eye_y=eye_y
                )
                count += 1
        image_ready = self._change_color(image=image_in_process, color_convert=cv2.COLOR_BGR2RGB)

        return image_ready

    @staticmethod
    def convert_to_base64(generated_image):
        image_uint8 = Image.fromarray(generated_image.astype('uint8'))
        raw_bytes = BytesIO()
        image_uint8.save(raw_bytes, 'PNG')
        raw_bytes.seek(0)
        image_base64 = base64.b64encode(raw_bytes.read())

        return 'data:image/jpeg;base64,' + str(image_base64).split('\'')[1]
