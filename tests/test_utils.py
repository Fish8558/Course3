from config import TEST_FILE_PATH
from main import all_operation_list
from src import utils


def test_json_load():
    operations = json_load(TEST_FILE_PATH)
    assert operations == [{"1": 1, "2": 2, "3": 3}]


def test_sort_last_five_list():
    full_list = [
        {"id": 1, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 2, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 3, "state": "CANCELED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 4, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 5, "state": "CANCELED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 6, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 7, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 8, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 9, "state": "EXECUTED", "date": "", "": "", "to": "", "description": "", "operationAmount": ""}]
    last_list = [
        {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'},
    {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'},
    {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614', 'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 7810846596785568', 'to': 'Счет 43241152692663622869'},
    {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051', 'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794', 'to': 'Счет 46765464282437878125'},
    {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725', 'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'}
       ]
    assert utils.sort_last_five_list(full_list) == last_list


def test_final_information():
    assert utils.final_information('Visa Gold 9447344650495960') == 'Visa Gold 9447 34** **** 5960'
    assert utils.final_information('Visa Platinum 2241653116508487') == 'Visa Platinum 2241 65** **** 8487'
    assert utils.final_information('Visa Classic 7022985698476865') == 'Visa Classic 7022 98** **** 6865'
    assert utils.final_information('Maestro 8045769817179061') == 'Maestro 8045 76** **** 9061'
