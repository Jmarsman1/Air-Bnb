#!/usr/bin/python3
"""
Contains the FileStorage class
"""
from os.path import exists
import json


class FileStorage:
    """File Storage Class"""

    # string - path to the JSON file
    __file_path = 'file.json'
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """return content of __objects attribute"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode="w",
                  encoding="utf-8") as outinstances:
            json.dump(
                    {
                        key: (value.to_dict() if not isinstance(value, dict) else value)
                        for (key, value) in self.__objects.items()
                    }, outinstances)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
        if exists(self.__file_path):
            with open(self.__file_path, encoding='utf-8') as ininstances:
                self.__objects = json.load(ininstances)
