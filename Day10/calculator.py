##Calculator
from art import logo 
print(logo)

def add (n1,n2):
    return n1 + n2

def subtract (n1,n2):
    return n1 - n2

def multiply (n1,n2):
    return n1 * n2

def divide (n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide 

}
should_continue = False
   
num1 = float(input("Enter the first number "))
for symbol in operations:
    print(symbol)

while not should_continue:
    operation_symbol = input("Enter the Operation symbol from the above lines ")
    num2 = float(input("Enter the next number "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
    print (f"{num1} {operation_symbol} {num2} = {answer}")

    user_input = input(f"Do you want to continue another operation with {answer}, Type 'Y' to continue or Type 'N' to stop ").lower()
    
    if user_input == 'y':
        num1 = answer
        #num3 = input("Enter the next number for operation")
    else:
        print("Good Bye ")
        should_continue = True 
        