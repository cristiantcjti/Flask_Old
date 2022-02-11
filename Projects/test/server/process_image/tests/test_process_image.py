import unittest
import os

from server.custom.client_exception import ClientException
from flask_api import status
from server.process_image.process_image import Googlyfier
from server.util_tests.util_tests import  image_base_64


class ProcessImageTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.image_ok = os.path.abspath('util_tests/picture_test/image1.jpg')
        self.image_fail = os.path.abspath('util_tests/picture_test/no_face.jpg')
        self.image_base64_ok = image_base_64(self.image_ok)
        self.image_base64_fail = image_base_64(self.image_fail)
        self.googlyfier = Googlyfier

    def test_googlyfier_successfully_add_googly_eyes(self) -> None:
        image = self.googlyfier.convert_from_base64(self.image_base64_ok)
        generated_image = self.googlyfier().generator(image)
        base64_string = self.googlyfier.convert_to_base64(generated_image)
        self.assertNotEqual(self.image_base64_ok, base64_string)
        self.assertEqual(type(base64_string), str)

    def test_googlyfier_fail_with_image_without_faces(self) -> None:

        with self.assertRaises(ClientException) as err:
            image = self.googlyfier.convert_from_base64(self.image_base64_fail)
            self.googlyfier().generator(image)

        self.assertIn('It is not possible to recognize a face on the image.', err.exception.message)
        self.assertEqual(err.exception.status_code, status.HTTP_400_BAD_REQUEST)


if __name__ == '__main__':
    unittest.main()
