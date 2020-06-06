import requests

API_KEY = 'trnsl.1.1.20200410T144441Z.c3da493037e85651.17141e8c1c1797ed89379865149d7492889ccc11'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
        :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': 'en-ru',
    }

    response = requests.get(URL, params=params)
    return response.json()['text']


if __name__ == '__main__':
    input_text = input('Введите текст для перевода на русский: ')
    print(translate_it(input_text))
