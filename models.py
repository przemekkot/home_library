import json


class Library:
    def __init__(self):
        try:
            with open("library.json", "r") as f:
                self.home_library = json.load(f)
        except FileNotFoundError:
            self.home_library = []

    def all(self):
        return self.home_library

    def get(self, id):
        return self.home_library[id]

    def create(self, data):
        data.pop('csrf_token')
        self.home_library.append(data)

    def save_all(self):
        with open("library.json", "w") as f:
            json.dump(self.home_library, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.home_library[id] = data
        self.save_all()


home_library = Library()