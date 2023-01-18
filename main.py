import os

# os.system('pip install --upgrade pip')
# os.system('pip install wheel')
# os.system('pip install twine')
# os.system('python example_project/setup.py sdist bdist_wheel')
# os.system('twine upload dist/*')

from src.json_tools.jsonTools import JsonTools

j = JsonTools()

j.connect("newDB.json")
j.dump_sample()
data = j.load_to_dict()
print(data)

# j.dump_sample()
# print(j.db)