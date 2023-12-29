from config import OPERATIONS_PATH
from src.utils import json_load, sort_last_five_list, final_information

all_operation_list = json_load(OPERATIONS_PATH)
last_five_sorted = sort_last_five_list(all_operation_list)
for i in last_five_sorted:
    print(i)
final_information_list = final_information(last_five_sorted)

for operation in final_information_list:
    print(operation)