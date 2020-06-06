import unittest
import requests
import translator


class YaTests(unittest.TestCase):

    def test_response(self):
        resp = requests.get('http://translate.yandex.ru')
        self.assertEqual(resp.status_code, 200)

    def test_key(self):
        self.assertTrue(translator.API_KEY)

    def test_translate(self):
        test_input = 'This is test message'
        self.assertIsNotNone(translator.translate_it(test_input))

    def test_negativ_status(self):
        resp = requests.get('http://translate.yandex.ru')
        self.assertEqual(resp.status_code, 402, msg='API-ключ заблокирован')

    def test_negativ_translate(self):
        test_input = None
        self.assertIsNotNone(translator.translate_it(test_input), msg='Отсутствует текст для перевода')


