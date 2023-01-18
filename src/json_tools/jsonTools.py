import json
import os

class JsonTools:
    def __init__(self):
        pass


    def connect(self, filepath):

        #formatting
        if ".json" not in filepath: filepath = filepath + ".json"

        #if the file already exists, set self.db to that path.
        #if not, make a new db and set it to self.db
        if os.path.exists(filepath) == True:
            # print("Database found and connected")
            self.db = filepath
        else:
            # print(f"No file found, creating a new database at {filepath}")
            open(filepath, "x")
            self.db = filepath


    
    def read_to_dict(self):
        data = open(self.db, "r")
        data = json.load(data)
        return data


    def dump_sample(self):
        dump = {
            "key1": "value1",
            "key2": "value2",
            "key3": {
                "nested-key1": "nested-value1",
                "nested-key2": "nested-value2",
                "nested-key3": "nested-value3",
            },
            "key4": [
                "list1", 
                "list2",        
                "list3",
            ]
        }
        with open(self.db, "w") as f:
            json.dump(dump, f)