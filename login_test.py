
import unittest


def login(username, password):
    """Simple login function for testing."""
    if username == "admin" and password == "admin123":
        return "Login successful"
    return "Invalid username or password"


class TestLogin(unittest.TestCase):

    def test_valid_login(self):
        result = login("admin", "admin123")
        self.assertEqual(result, "Login successful")

    def test_invalid_password(self):
        result = login("admin", "wrong123")
        self.assertEqual(result, "Invalid username or password")

    def test_invalid_username(self):
        result = login("user", "admin123")
        self.assertEqual(result, "Invalid username or password")

    def test_empty_credentials(self):
        result = login("", "")
        self.assertEqual(result, "Invalid username or password")


if __name__ == "__main__":
    unittest.main()
