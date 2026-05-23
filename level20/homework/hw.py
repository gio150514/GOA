password = "kionsegg jesko 123"  
user_input = input('Enter your password: ') 

while password != user_input:
    print('WRONG PASSWORD. Try again')
    user_input = input("Enter your password: ")

print('Correct password') 