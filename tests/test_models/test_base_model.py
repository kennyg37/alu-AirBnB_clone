#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
import datetime
import json
import os

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        i = BaseModel()
        self.assertEqual(type(i), BaseModel)

    def test_kwargs(self):
        i = BaseModel()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_save(self):
        i = BaseModel()
        i.save()
        key = f'{i.__class__.__name__}.{i.id}'
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        i = BaseModel()
        expected_str = f'[{i.__class__.__name__}] ({i.id}) {i.__dict__}'
        self.assertEqual(str(i), expected_str)

    def test_todict(self):
        i = BaseModel()
        self.assertEqual(i.to_dict(), i.to_dict())

    def test_id(self):
        new = BaseModel()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        new = BaseModel()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        new = BaseModel()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

if __name__ == '__main__':
    unittest.main()
