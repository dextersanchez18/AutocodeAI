import os
import unittest


class TestIndexPage(unittest.TestCase):
    def setUp(self):
        self.filepath = os.path.join(os.path.dirname(__file__), "index.html")

    def test_index_file_exists(self):
        self.assertTrue(
            os.path.exists(self.filepath),
            "index.html does not exist in root directory",
        )

    def test_index_contains_heading(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn(
            "Hello from AutocodeAI",
            content,
            "index.html does not contain 'Hello from AutocodeAI'",
        )

    def test_index_contains_viewport_meta(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn(
            'name="viewport"',
            content,
            "index.html does not contain viewport meta tag",
        )


if __name__ == "__main__":
    unittest.main()
