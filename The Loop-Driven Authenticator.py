import getpass
attempt=0
while attempt<=3:
    print("enter the following details:")
    print("username:")
    username = input()     
    password = getpass.getpass()
    if username == "Milind" and password == "MILIND$1234":
        print("welcome to the system")
        break
    else:
        print("invalid username or password")
        attempt+=1
else:
    print("you have exceeded the maximum number of attempts")
