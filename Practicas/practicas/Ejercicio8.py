
num1 = int(input("Enter the dividend:"))

num2 = int(input("Enter the divider:"))

result = num1 / num2
print()

if result != 0:
    quotient = num1 // num2

    resto = num1 % num2
    print(f"The division quotient is:{quotient}")
    print(f"The rest of the division is:{resto}")
else:
    print("Error, cannot be divided by zero")