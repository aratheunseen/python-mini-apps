# at least 8 characters with a lowercase, an uppercase and a special symbol

password = input("Enter new password: ")
special_characters = "!@#$%^&*()-+?_=,<>/"
digit = uppercase = lowercase = special_char = False
result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)


for i in password:
    if i.isdigit():
        digit = True
    if i.isupper():
        uppercase = True
    if i.islower():
        lowercase = True
    if any(char in special_characters for char in password):
        special_char = True

result.append(digit)    
result.append(uppercase)
result.append(lowercase)
result.append(special_char)

print(result)

if all(result):
    print("Requrement matched")
else:
    print("Requrement doesn't matched")