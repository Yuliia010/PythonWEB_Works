import json
import os

class Directory:
    def __init__(self, filename="directory.json"):
        self.filename = filename
        self.data = []
        self.load_from_file()

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        else:
            self.data = []

    def save_to_file(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=2)

    def is_duplicate(self, entry):
        for existing in self.data:
            if all(existing.get(key) == entry.get(key) for key in entry):
                return True
        return False

    def add_entry(self, name, owner, phone, address, activity):
        entry = {
            "name": name,
            "owner": owner,
            "phone": phone,
            "address": address,
            "activity": activity
        }

        if self.is_duplicate(entry):
            print("The entry already exists. Addition cancelled.")
            return

        self.data.append(entry)
        self.save_to_file()

    def search(self, field, value):
        return [entry for entry in self.data if entry.get(field, '').lower() == value.lower()]

    def show_all(self):
        return self.data



directory = Directory()

directory.add_entry("Test 3", "Ivanov", "156888532", "Address first", "It")
directory.add_entry("Test 4", "Pavlov", "145845", "Address second", "Buh")


print("Search by owner 'Ivanov':")
for entry in directory.search("owner", "Ivanov"):
    print(entry)

print("\nSearch by name 'Test 2':")
for entry in directory.search("name", "Test 2"):
    print(entry)

print("\nSearch by activity 'It':")
for entry in directory.search("activity", "It"):
    print(entry)

print("\nGet All:")
for entry in directory.show_all():
    print(entry)
