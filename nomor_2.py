import re

def is_username_valid(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    length = len(string)
    if length >= 5 and length <= 9 and not string[0].isdigit() and regex.search(string[0]) == None:
        upper = re.findall(r'[A-Z]', string)
        lower = re.findall(r'[a-z]', string)
        number = re.findall(r'[0-9]',string)
        if len(upper) > 0 and len(lower) > 0 and len(number) > 0:
            return True
            
    return False

def is_password_valid(string):
    regex = re.compile('[=]')
    length = len(string)
    if length >= 8 and regex.search(string) != None:
        upper = re.findall(r'[A-Z]', string)
        lower = re.findall(r'[a-z]', string)
        number = re.findall(r'[0-9]',string)
        if len(upper) > 0 and len(lower) > 0 and len(number) > 0:
            return True
    return False  

print(is_username_valid("Xrutaf888"))
print(is_username_valid("1Diana"))
print(is_password_valid("passW0rd="))
print(is_password_valid("C0d3YourFuture!#"))
