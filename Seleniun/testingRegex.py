import re

check = input("Enter the message: ")

pattern = re.compile(r"awurudu|new|year|happy")

if pattern.search(check):
    print("Yes it is in")
else:
    print("NOOOOOOO")