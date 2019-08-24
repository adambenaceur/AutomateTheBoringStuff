try:
    NUMBER = int((input("Enter a number : ")))
except:
    print("Value must be a whole number!")
    exit()

def collatz(number):
    if number % 2 == 1:
        number = (number * 3) + 1
        return int(number)
    elif number % 2 == 0:
        number = number / 2
        return int(number)
    else:
        print("number must be whole number")

NUMBER = collatz(NUMBER)

while NUMBER != 1:
    print(collatz(NUMBER))
    NUMBER = collatz(NUMBER)

