from src.utils import sort_last_five_list, final_information, json_load
from config import TEST_FILE_PATH


def test_json_load():
    operations = json_load(TEST_FILE_PATH)
    assert operations == [{"1": 1, "2": 2, "3": 3}]
