import json

class File:

    def __innit__(self, file_path):

        self.file_path = file_path

    def load(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {
                "Coins": 0,
                "Coal": 0,
                "Copper Ore": 0,
                "Iron Ore": 0,
                "Gold Ore": 0,
                "Diamonds": 0,
                "Copper Bar": 0,
                "Iron Bar": 0,
                "Gold Bar": 0,
            }

    def save(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)