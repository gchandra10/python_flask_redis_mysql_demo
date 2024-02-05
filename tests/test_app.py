import unittest
from app import app


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        # Test the index route
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, World!", response.data)


if __name__ == "__main__":
    unittest.main()
