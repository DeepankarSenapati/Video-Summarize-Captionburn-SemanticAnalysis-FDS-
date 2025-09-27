#!/usr/bin/env python3
"""
Simple Calculator Program
A basic calculator that performs arithmetic operations
"""
import math

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

def power(a, b):
    """Raise first number to the power of second number"""
    return a ** b

def square_root(a):
    """Calculate square root of a number"""
    if a < 0:
        return "Error: Cannot calculate square root of negative number!"
    return math.sqrt(a)

def percentage(a, b):
    """Calculate percentage: a% of b"""
    return (a / 100) * b

def main():
    """Main function to run the calculator"""
    print("Welcome to Advanced Calculator!")
    print("Available operations: +, -, *, /, ^ (power), sqrt (square root), % (percentage)")
    
    while True:
        try:
            # Get user input
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /, ^, sqrt, %): ")
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
            elif operation == '^':
                result = power(num1, num2)
            elif operation == 'sqrt':
                result = square_root(num1)
            elif operation == '%':
                result = percentage(num1, num2)
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
