import re


def email_parse(email_address):
    output = re.findall(r"(^\w+)@((\w+).(\w{2,}))$", email_address)
    if not output:
        raise ValueError(f"wrong email: {email_address}")
    print(dict(zip(["username", "domain"], output[0])))


while True:
    user_input = input("Enter your email address. For exit press q: ")
    if user_input == 'q':
        break
    else:
        try:
            email_parse(user_input)
        except ValueError as e:
            print(e)
