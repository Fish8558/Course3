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
        {"id": 1, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 2, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 4, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 6, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 7, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 8, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""}]

    assert utils.sort_last_five_list(full_list) == last_list

def test_final_information():
    assert utils.final_information('Visa Gold 9447344650495960') == 'Visa Gold 9447 34** **** 5960'
    assert utils.final_information('Visa Platinum 2241653116508487') == 'Visa Platinum 2241 65** **** 8487'
    assert utils.final_information('Visa Classic 7022985698476865') == 'Visa Classic 7022 98** **** 6865'
    assert utils.final_information('Maestro 8045769817179061') == 'Maestro 8045 76** **** 9061'