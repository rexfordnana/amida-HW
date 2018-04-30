import re
import json
import os


class JsonParser:
    def __init__(self):
        self.name = {}
        self.dob = ""
        self.address = []
        self.city = ""
        self.state = ""
        self.zip = ""
        self.phone = ""
        self.email = ""
        self.coverage = {}

    def parsse(self, file):
        for line in file.read().decode("utf-8").splitlines():
            if line.__contains__("Emergency Contact"):
                break

            tokens = line.split(": ")
            if tokens[0] == "Name": self.name_converter(tokens[1])
            if tokens[0].__contains__("Birth"): self.dob = tokens[1]
            if tokens[0].__contains__("Address"): self.address.append(tokens[1])
            if tokens[0] == "City": self.city = tokens[1]
            if tokens[0] == "State": self.state = tokens[1]
            if tokens[0] == "Zip": self.zip = tokens[1]
            if tokens[0].__contains__("Phone"): self.phone = tokens[1]
            if tokens[0] == "Email": self.email = tokens[1]
            if tokens[0].__contains__("Part"): self.coverage[tokens[0]] = tokens[1]

        self.address_converter(self.address)
        self.coverage_converter(self.coverage)

        self.display()
        self.save()

    def name_converter(self, names):
        names = names.split(" ")
        self.name = {"first_name": names[0], "last_name": names[1]}

    def coverage_converter(self, coverage):
        self.coverage = []

        for key, value in coverage.items():
            print(key)
            key = re.findall("Part \w", key)
            print("Key ---> ", key)
            self.coverage.append({"type": key[0], "effective_ date": value})

    def address_converter(self, address):
        self.address = []
        [self.address.append(data) for data in address if data !=""]

    def save(self):
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'post.json'), 'w') as f:
            json.dump(self.__dict__, f, indent=4)

    def display(self):
        print(self.__dict__)