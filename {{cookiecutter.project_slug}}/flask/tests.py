import unittest
from app import app

app.testing = True

class TestApi(unittest.TestCase):
    def test_index(self):
        client = app.test_client(self)
        response = client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, Flask!') 