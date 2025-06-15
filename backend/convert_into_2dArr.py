import json
import re

def extract_2d_array_from_string():
    with open("data.txt", 'r', encoding='utf-8') as f:
        data = f.read()
    data_string = data 
    try:
        match = re.search(r'\[.*\]', data_string, re.DOTALL)
        if match:
            json_part = match.group()
            array_2d = json.loads(json_part)
            return array_2d
        else:
            raise ValueError("No list structure found in the string.")
    except json.JSONDecodeError as e:
        raise ValueError("Failed to parse JSON: " + str(e))




# result = extract_2d_array_from_string()
# print(result)
