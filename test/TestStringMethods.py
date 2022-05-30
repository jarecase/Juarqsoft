import unittest
import requests

API = 'http://127.0.0.1:5000/api/juego'

class TestStringMethods(unittest.TestCase):

    def test_Get(self):
        res = requests.get(API)
        prueba = not str(res.text)
        self.assertFalse(prueba)

    def test_POST(self):
        res = requests.get(API)
        prueba = not str(res.text)
        self.assertFalse(prueba)

if __name__ == '__main__':
    unittest.main()