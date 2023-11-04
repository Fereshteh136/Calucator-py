# Request user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display the menu of available operations
print("Please select the operation you want to perform:")
print("1. Addition (+) ")
print("2. Subtraction (-) ")
print("3. Multiplication (*) ")
print("4. Division (/) ")

# Request user's choice of operation
choice = input("Enter the operation number (1/2/3/4): ")

# Perform the operation based on the user's choice
if choice == '1':
    result = num1 + num2
    operation = 'addition'
elif choice == '2':
    result = num1 - num2
    operation = 'subtraction'
elif choice == '3':
    result = num1 * num2
    operation = 'multiplication'
elif choice == '4':
    if num2 == 0:
        result = "Division by zero is not allowed"
        operation = 'division'
    else:
        result = num1 / num2
        operation = 'division'
else:
    result = "Invalid choice"
    operation = 'unknown operation'

# Display the result
if operation == 'division':
    print(f"{num1} divided by {num2} is equal to {result}")
else:
    print(f"The result of {operation} is {result}")
