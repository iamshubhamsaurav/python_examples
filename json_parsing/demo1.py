import json


employee_json = '{"id":"09", "name": "Nitin", "department":"Finance"}'

emps = json.loads(employee_json)

print(emps['name'])