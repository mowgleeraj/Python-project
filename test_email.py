import unittest
import re
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

    # ... (other test methods)

if __name__ == '__main__':
    unittest.main()
