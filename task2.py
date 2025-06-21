n1 = float(input("Enter n1: "))
n2 = float(input("Enter n2: "))

print("Choose an Arithmetic operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulo Division(%)")

operation = input("Enter the number or symbol of the arithmetic operation (1/+ , 2/-, 3/*, 4/, 5/%): ")

if operation in ['1', '+']:
    result = n1 + n2
    print(f"The result of addition is: {result}")
elif operation in ['2', '-']:
    result = n1 - n2
    print(f"The result of subtraction is: {result}")
elif operation in ['3', '*']:
    result = n1 * n2
    print(f"The result of multiplication is: {result}")
elif operation in ['4', '/']:
    if n2 != 0:
        result = n1 / n2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not possible.")
elif operation in ['5', '%']:    
    result = n1 % n2    
    print(f"The result of Modulo division is:{result}")
else:
    print("Invalid choice.")