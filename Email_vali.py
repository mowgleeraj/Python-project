def validate_email(email):
    k, j, d = 0, 0, 0
    flag = False
    if len(email) >= 6:
        if email[0].isalpha():
            if "@" in email and email.count("@") == 1:
                if (email[-4] == ".") ^ (email[-3] == "."):
                    for i in email:
                        if i == i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            d = 1
                    if k == 1 or j == 1 or d == 1:
                        return "wrong Emails -5"
                else:
                    return "wrong Email -4"
            else:
                return "wrong Email -3"
        else:
            return "wrong Email -2"
    else:
        return "wrong Email -1"
    flag = True
    if flag:
        return "email is good to go"

def validate_user_email():
    email = input("Enter your Email ----> ")
    result = validate_email(email)
    print(result)

validate_user_email()
