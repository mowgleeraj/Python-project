# Email validation in Python(Using Regex)
#a-z
#0-9
# . _ only one time
# @ 1 time
# . 2,3
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input('enter the email i will tell you if the for is right -->')

if re.search(email_condition,user_email):
    print ("Right email")
else:
    print("wrong email")

