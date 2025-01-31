import random

def add(x, y):
    return x + y + random.choice(range(-3, 4))

def subtract(x, y):
    return x - y + random.choice(range(-3, 4))

def multiply(x, y):
    return x * y + random.choice(range(-5, 6))

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y + random.choice(range(-2, 3))

def calculator():
    print("Whimsical Calculator")
    print("Choose your magical operation:")
    print("1. Add with a twist")
    print("2. Subtract with a surprise")
    print("3. Multiply with a mystery")
    print("4. Divide with a dash of randomness")

    choice = input("Enter your whimsical choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first magical number: "))
        num2 = float(input("Enter the second magical number: "))

        if choice == '1':
            print(f"The magical sum is: {add(num1, num2)}")

        elif choice == '2':
            print(f"The mysterious difference is: {subtract(num1, num2)}")

        elif choice == '3':
            print(f"The enchanted product is: {multiply(num1, num2)}")

        elif choice == '4':
            print(f"The whimsical quotient is: {divide(num1, num2)}")
    else:
        print("Invalid choice! The magic faded away.")

if __name__ == "__main__":
    calculator()