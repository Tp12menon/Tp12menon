import unittest
import os
from database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_db.json"
        self.db = Database(self.test_filename)

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_set_and_get(self):
        self.db.set("name", "Alice")
        self.assertEqual(self.db.get("name"), "Alice")
        self.assertIsNone(self.db.get("age"))

    def test_delete(self):
        self.db.set("city", "London")
        self.assertEqual(self.db.get("city"), "London")
        self.assertTrue(self.db.delete("city"))
        self.assertIsNone(self.db.get("city"))
        self.assertFalse(self.db.delete("nonexistent_key"))

    def test_persistence(self):
        self.db.set("persistent_key", "persistent_value")
        # Create a new instance pointing to the same file
        db_new = Database(self.test_filename)
        self.assertEqual(db_new.get("persistent_key"), "persistent_value")

if __name__ == '__main__':
    unittest.main()
