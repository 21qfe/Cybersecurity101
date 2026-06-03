import getpass
database={
    "berlin": "BERLIN$1234",
    "paris": "eiffel$5678",
    "london": "bigben$9012",
    "newyork": "timesquare$3456"
}
attempt=1
while attempt<=3:
    print("enter the following details:")
    print("username:")
    username = input().lower()     
    password = getpass.getpass()
    if username in database and password == database[username]:
        print("welcome to the system")
        break
    else:
        print("invalid username or password")
        attempt+=1
