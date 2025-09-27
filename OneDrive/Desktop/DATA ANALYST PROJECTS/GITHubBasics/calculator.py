#!/usr/bin/env python3
"""
Simple Calculator Program
A basic calculator that performs arithmetic operations
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract second number from first"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide first number by second"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def main():
    """Main function to run the calculator"""
    print("Welcome to Simple Calculator!")
    print("Available operations: +, -, *, /")
    
    while True:
        try:
            # Get user input
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            # Perform calculation
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation!")
                continue
            
            print(f"Result: {result}")
            
            # Ask if user wants to continue
            continue_calc = input("Do you want to perform another calculation? (y/n): ")
            if continue_calc.lower() != 'y':
                break
                
        except ValueError:
            print("Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
