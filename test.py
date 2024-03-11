import json

def function(value):
    with open('Resource/dict_cmd.json', encoding='utf-8') as file:
        data = json.load(file)

    if value in data:
        query = data[value]
        if len(query) > 0:
            function_name = query[0]
            print(f"Calling function: {function_name}")
            # Gọi hàm tương ứng ở đây, ví dụ:
            # exec(function_name + '()')
        else:
            print("Empty function list for the given value.")

function("mở cài đặt mouse")
