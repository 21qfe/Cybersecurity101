import getpass
print("enter the following details:")
print("username:")
username = input()     
password = getpass.getpass()
if username == "Milind" and password == "MILIND$1234":
    print("welcome to the system")
else:
    print("invalid username or password")   