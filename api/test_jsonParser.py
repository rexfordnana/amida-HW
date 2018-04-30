from unittest import TestCase
from . import jsonparser
import os, json


class TestJsonParser(TestCase):
    jparser = jsonparser.JsonParser()

    def test_parse(self):
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "cms_sample.txt"), "r") as f:
            self.jparser.parsse(f)

    def test_jsonRead(self):
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "post.json"), 'r') as f:
            jsonfile = json.loads(f.read())

        print(jsonfile)
