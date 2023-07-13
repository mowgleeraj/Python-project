import unittest
import re
from Email_Regex import validate_email

def validate_email(user_email):
    email_condition = "^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if re.search(email_condition, user_email):
        return "Right email"
    else:
        return "wrong email"

class EmailValidationTestCase(unittest.TestCase):

    def test_valid_email(self):
        email = "test.email@example.com"
        result = validate_email(email)
        self.assertEqual(result, "Right email")

    def test_invalid_email(self):
        email = "invalidemail"
        result = validate_email(email)
        self.assertEqual(result, "wrong email")

    def test_invalid_characters(self):
        email = "user name@example.com"
        result = validate_email(email)
        self.assertEqual(result, "wrong email")

    def test_invalid_domain(self):
        email = "wrongemail@.com"
        result = validate_email(email)
        self.assertEqual(result, "wrong email")

if __name__ == '__main__':
    unittest.main()
