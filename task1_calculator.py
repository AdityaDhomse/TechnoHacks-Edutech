def add(a, b):
    result = a + b
    print("\nAddition =" ,result)
    
def subtract(a, b):
    result = a - b
    print("\nSubtraction =" ,result)
    
def multiply(a, b):
    result = a * b
    print("\nMultiplication =" ,result)
    
def division(a, b):
    if (b == 0):
        print("Error ,cannot divide by zero(0)")
    else:
        result = a / b
        print("\nDivision =", result)
    
a = int(input("Enter first no.: "))
b = int(input("Enter second no.: "))

print("\n--------MENU--------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("\nEnter Choice: "))

if (choice == 1):
    add(a, b)
elif (choice == 2):
    subtract(a, b)
elif (choice == 3):
    multiply(a, b)
elif (choice == 4):
    division(a, b)
else:
    print("Wrong choice")
    