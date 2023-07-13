# Email validation in Python(Using Regex)
#a-z
#0-9
# . _ only one time
# @ 1 time
# . 2,3
import re

def validate_email(user_email):
    email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    if re.search(email_condition, user_email):
        return "Right email"
    else:
        return "wrong email"

def validate_user_email():
    user_email = input('Enter your email --> ')
    result = validate_email(user_email)
    print(result)

validate_user_email()
