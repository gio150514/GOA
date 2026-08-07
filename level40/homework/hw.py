# 1) ფუნქცია, რომელიც პრინტავს "Hello, World!"

def hello():
    print("Hello, World!")

hello()


# 2) ფუნქცია, რომელიც იღებს სახელს და პრინტავს მისალმებას

def greet(name):
    print("Hello,", name)

greet("Nika")


# 3) ფუნქცია, რომელიც იღებს ორ რიცხვს და პრინტავს მათ ჯამს

def sum_numbers(a, b):
    print(a + b)

sum_numbers(5, 10)


# 4) ფუნქცია, რომელიც ამოწმებს რიცხვი ლუწია თუ კენტი

def check_number(number):
    if number % 2 == 0:
        print("ლუწი")
    else:
        print("კენტი")

check_number(7)


# 5) ფუნქცია, რომელიც რიცხვს აორმაგებს

def double(number):
    print(number * 2)

double(8)