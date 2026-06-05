import getpass
import sys
database={
    "berlin": {"password": "BERLIN$1234","role": "admin"},
    "paris": {"password": "eiffel$5678","role": "user"},
    "london": {"password": "bigben$9012","role": "user"},
    "newyork": {"password": "timesquare$3456","role": "developer"}
}
def login(username, password):
    if username in database and password == database[username]["password"]:
        return database[username]["role"]
    else:
        return None
def display(username, role):
    print(f"welcome {username} to the system")
    if role == "admin":
        print("you have admin privileges")
    elif role == "developer":
        print("you have developer privileges")
    else:
        print("you have user privileges")
def main():
    attempt=1
    while attempt<=3:
        print("enter the following details:")
        print("username:")
        username = input().lower().strip()     
        password = getpass.getpass()
        role = login(username, password)
        if role:
            display(username, role)
            break
        else:
            print("invalid username or password")
            attempt+=1
    else:
        print("you have exceeded the maximum number of attempts")
        sys.exit()
main()