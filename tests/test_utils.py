import json

from config import TEST_FILE_PATH, TEST_FILE_SORTED_PATH, TEST_FILE_OPERATION_PATH
from src.utils import json_load, sort_last_five_list, final_information


def test_json_load():
    operations = json_load(TEST_FILE_PATH)
    assert operations == [{"1": 1, "2": 2, "3": 3}]


def test_sort_last_five_list():
    with open(TEST_FILE_OPERATION_PATH, encoding='utf-8') as file_json:
        last_list = json.load(file_json)
    assert sort_last_five_list(last_list) == [{'date': '2019-12-08T22:46:21.935582',
                                               'description': 'Открытие вклада',
                                               'id': 863064926,
                                               'operationAmount': {'amount': '41096.24',
                                                                   'currency': {'code': 'USD', 'name': 'USD'}},
                                               'state': 'EXECUTED',
                                               'to': 'Счет 90424923579946435907'},
                                              {'date': '2019-12-07T06:17:14.634890',
                                               'description': 'Перевод организации',
                                               'from': 'Visa Classic 2842878893689012',
                                               'id': 114832369,
                                               'operationAmount': {'amount': '48150.39',
                                                                   'currency': {'code': 'USD', 'name': 'USD'}},
                                               'state': 'EXECUTED',
                                               'to': 'Счет 35158586384610753655'},
                                              {'date': '2019-11-19T09:22:25.899614',
                                               'description': 'Перевод организации',
                                               'from': 'Maestro 7810846596785568',
                                               'id': 154927927,
                                               'operationAmount': {'amount': '30153.72',
                                                                   'currency': {'code': 'RUB', 'name': 'руб.'}},
                                               'state': 'EXECUTED',
                                               'to': 'Счет 43241152692663622869'},
                                              {'date': '2019-11-13T17:38:04.800051',
                                               'description': 'Перевод со счета на счет',
                                               'from': 'Счет 38611439522855669794',
                                               'id': 482520625,
                                               'operationAmount': {'amount': '62814.53',
                                                                   'currency': {'code': 'RUB', 'name': 'руб.'}},
                                               'state': 'EXECUTED',
                                               'to': 'Счет 46765464282437878125'},
                                              {'date': '2019-11-05T12:04:13.781725',
                                               'description': 'Открытие вклада',
                                               'id': 801684332,
                                               'operationAmount': {'amount': '21344.35',
                                                                   'currency': {'code': 'RUB', 'name': 'руб.'}},
                                               'state': 'EXECUTED',
                                               'to': 'Счет 77613226829885488381'}]


def test_final_information():
    with open(TEST_FILE_SORTED_PATH, encoding='utf-8') as f:
        last_five_sorted = json.load(f)
    assert final_information(last_five_sorted) == ['08.12.2019 Открытие вклада\n'
                                                   'Счет **5907\n41096.24 USD\n',
                                                   '07.12.2019 Перевод организации\n'
                                                   'Visa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD\n',
                                                   '19.11.2019 Перевод организации\n'
                                                   'Maestro 7810 84** **** 5568 -> Счет **2869\n30153.72 руб.\n',
                                                   '13.11.2019 Перевод со счета на счет\n'
                                                   'Счет **9794 -> Счет **8125\n62814.53 руб.\n',
                                                   '05.11.2019 Открытие вклада\nСчет **8381\n21344.35 руб.\n']
