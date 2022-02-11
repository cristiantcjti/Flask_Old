import unittest

from server.app import create_app
from server.util_tests.util_tests import image_base_64


class PostTestCase(unittest.TestCase):

    def setUp(self):
        app = create_app()
        self.client = app.test_client()
        self.url = 'http://127.0.0.1:5000'
        self.post_end_point = '/api/images'
        self.image64_ok = image_base_64('util_tests/picture_test/image1.jpg')
        self.image64_fail = image_base_64('util_tests/picture_test/no_face.jpg')
        self.header = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def test_post_successfully(self):
        data = {
            "data": self.image64_ok
        }

        response = self.client.post(self.post_end_point, json=data, headers=self.header)
        self.assertEqual(response.status_code, 200)

    def test_post_fail_with_a_picture_without_face(self):
        data = {
            "data": self.image64_fail
        }

        response = self.client.post(self.post_end_point, json=data, headers=self.header)
        self.assertEqual(response.status_code, 400)

    def test_post_fail_with_image_data_empty(self):
        data = {
            "data": ''
        }

        response = self.client.post(self.post_end_point, json=data, headers=self.header)
        self.assertEqual(response.status_code, 400)

    def test_post_fail_not_found(self):
        data = {
            "data": self.image64_fail
        }

        response = self.client.post('NotFound', json=data, headers=self.header)
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
