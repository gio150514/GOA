password = "programing 999"
guess = ""

while guess != password:
    guess = input("Enter password: ")
    if password == guess:
        print("password is correct")
    else:
        print("password is incorrect")