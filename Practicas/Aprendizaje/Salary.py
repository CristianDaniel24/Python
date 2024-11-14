print("WELCOME!!")

numEmployee = int(input("Enter the amount of Employee\n"))
i = 1
salary = ()
countSalary = 0
countHigh = 0

while i <= numEmployee:
    salaryEmployee = float(input("Enter the salary of employee:\n"))
    if 100 <= salaryEmployee <= 300:
        countSalary +=1
    else:
        countHigh +=1
    i+=1
print(f"The amount the employee between $100 to $300 is: {countSalary}\n")
print(f"The amount the employee with salary elderly to $300 is: {countHigh}")