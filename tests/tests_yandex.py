from unittest import TestCase
from ya_create import create_folder

class TestCreateFolder(TestCase):

    def test_status_code(self):
        code = 201
        result = create_folder('Photo')
        self.assertEqual(code, result.status_code)

    def test_status_code(self):
        code = 409
        result = create_folder('Photo')
        self.assertEqual(code, result.status_code)

    def test_status_code(self):
        code = 401
        result = create_folder('Photo')
        self.assertEqual(code, result.status_code)