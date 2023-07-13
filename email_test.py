import unittest
from Email_vali import validate_email

class EmailValidationTestCase(unittest.TestCase):

    def test_valid_email(self):
        email = "test.email@example.com"
        result = validate_email(email)
        self.assertEqual(result, "email is good to go")

    def test_invalid_email(self):
        email = "invalidemail"
        result = validate_email(email)
        self.assertEqual(result, "wrong Email -3")

    def test_invalid_starting_character(self):
        email = "123@456"
        result = validate_email(email)
        self.assertEqual(result, "wrong Email -2")

    def test_invalid_ending_character(self):
        email = "john.doe@example..com"
        result = validate_email(email)
        self.assertEqual(result, "wrong Email -4")

    def test_invalid_characters(self):
        email = "user name@example.com"
        result = validate_email(email)
        self.assertEqual(result, "wrong Emails -5")

    def test_trailing_whitespace(self):
        email = "test@example.com "
        result = validate_email(email)
        self.assertEqual(result, "wrong Emails -5")

    def test_insufficient_domain(self):
        email = "notenough@"
        result = validate_email(email)
        self.assertEqual(result, "wrong Email -4")

    def test_invalid_domain(self):
        email = "wrongemail@.com"
        result = validate_email(email)
        self.assertEqual(result, "wrong Email -4")

if __name__ == '__main__':
    unittest.main()
