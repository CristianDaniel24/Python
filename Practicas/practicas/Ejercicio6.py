
num = int(input("Enter the number positive:"))

if num > 0:
    suma = sum(range(1, num + 1))
    print(f"The sum of all integers from 1 to {num} is: {suma}")
else:
    print("Error, enter the number positive, please")