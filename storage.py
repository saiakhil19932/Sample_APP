import json

class Storage:
    @staticmethod
    def save_to_json(data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def load_from_json(filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def append_to_json(data, filename):
        try:
            with open(filename, 'a') as file:
                json.dump(data, file)
                file.write('\n')
        except FileNotFoundError:
            with open(filename, 'w') as file:
                json.dump(data, file)
                file.write('\n')
