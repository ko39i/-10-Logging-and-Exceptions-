import math
import logging

logging.basicConfig(level=logging.DEBUG, filename="info.log", filemode="a")


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponentiation(x, y):
    return x ** y

def root(x):
    return math.sqrt(x)

def percentage(x, y):
    return x / 100 * y



while True:
    num1 = float(input("Enter first number: "))
    logging.info("Input nub1")

    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exponentiation")
    print("6.Root")
    print("7.Percentage")
    choice = input("Enter choice(1/2/3/4/5/6/7): ")
    logging.info("Input choice")



    if choice in ('1', '2', '3', '4', '5', '7'):
        num2 = float(input("Enter second number: "))
        logging.info("Input nub2")
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            logging.info("start of addition function")

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            logging.info("start of subtract function")

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            logging.info("start of multiply function")

        elif choice == '4':
            try:
                print(num1, "/", num2, "=", divide(num1, num2))
                logging.info("start of divide function")
            except:
                print("float division by zero")
                logging.error("float division by zero")

        elif choice == '5':
            print(num1, "^", num2, "=", exponentiation(num1, num2))
            logging.info("start of exponentiation function")
        elif choice == '7':
            print(num1, "%", num2, "=", percentage(num1, num2))
            logging.info("start of percentage function")
        break
    elif choice in ('6'):
            choice == '6'
            print("√", num1, "=", root(num1))
            logging.info("start of root function")

    else:
        print("Invalid Input")