import unittest
import requests
from app import app

local = app.test_client().get('/')
API = 'http://127.0.0.1:5000/api/juego'

class TestStringMethods(unittest.TestCase):

    def test_Get(self):
        assert local.status_code == 200
        assert local.data.decode('utf-8') == 'hello'

    def test_POST(self):
        res = requests.get(API)
        prueba = not str(res.text)
        self.assertFalse(prueba)

    def test_PUT(self):
        res = requests.get(API)
        prueba = not str(res.text)
        self.assertFalse(prueba)

if __name__ == '__main__':
    unittest.main()