import json
import os

class Database:
    def __init__(self, filename="db.json"):
        self.filename = filename
        self.data = {}
        self._load()

    def _load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.data = json.load(f)
            except json.JSONDecodeError:
                self.data = {}
        else:
            self.data = {}

    def _save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def set(self, key, value):
        self.data[key] = value
        self._save()

    def get(self, key, default=None):
        return self.data.get(key, default)

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self._save()
            return True
        return False

    def keys(self):
        return list(self.data.keys())
