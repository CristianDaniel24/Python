#Programar una función que determine si una empresa es microempresa o no (retorno booleano –True o False–).
# Se dice que es microempresa si tiene menos de 50 empleados, factura menos de 30 milones de euros y tiene un balance
# igual o inferior a los 5 millones de euros.

def company():
    employee = int(input("Enter the num of employee:"))
    dinner = int(input("Enter the dinner:"))
    balance = int(input("Enter the balance:"))

    if employee < 50 and dinner < 30000000 and balance <= 5000000:
        microenterprise = True
    else:
        microenterprise = False
    return microenterprise

microenterprise = company()
if microenterprise:
    print("\nYour company is a microbusiness")
else:
    print("\nYour company is not a microbusiness")
