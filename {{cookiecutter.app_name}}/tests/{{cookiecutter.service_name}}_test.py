import unittest

from flask import json

from service import {{cookiecutter.service_name}}


class TestService(unittest.TestCase):
    def setUp(self):
        {{cookiecutter.service_name}}.app.testing = True
        self.app = {{cookiecutter.service_name}}.app.test_client()

    def test_spellchecker_olx(self):
        response = self.app.get('/{{cookiecutter.service_name}}/olx')
        self.assertEqual(json.loads(response.get_data()), ['Hello, olx!'])

    def test_not_found(self):
        """ Test for non-existent path"""
        response = self.app.get("/pathnotexist")
        self.assertEqual(response.status_code, 404,
                         f"Got {response.status_code} but expected 404")


if __name__ == "__main__":
    unittest.main()
