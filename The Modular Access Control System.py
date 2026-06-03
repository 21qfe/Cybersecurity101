import getpass
database={
    "berlin": "BERLIN$1234",
    "paris": "eiffel$5678",
    "london": "bigben$9012",
    "newyork": "timesquare$3456"
}
#to add new user to the database
def add_user():
    print("enter new username:")
    new_username = input().lower().strip()
    print("enter new password:")
    new_password = getpass.getpass()
    database[new_username] = new_password
    print("new user added successfully")
#to initiate the login process
def login():
    attempt=1
    while attempt<=3:
        print("enter the following details:")
        print("username:")
        username = input().lower().strip()     
        password = getpass.getpass()
        if username in database and password == database[username]:
            print("welcome to the system")
            print("Do you want to add a new user? (yes/no)")
            response = input().lower().strip()
            if response == "yes":
               add_user()
            return True
        else:
            print("invalid username or password")
            attempt+=1
    print("you have exceeded the maximum number of attempts")
    return False

def main():
    login() 

main()
