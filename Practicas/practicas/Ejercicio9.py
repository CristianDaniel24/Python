
capitalInicial = float(input("Enter the amount to invest:"))

interesAnual = float(input("Enter the annual interest (in %):"))

years = int(input("Enter the numbers of years:"))

capitalFinal = capitalInicial * (1 + (interesAnual / 100)) ** years

print(f"The capital obtained after {years} years is:{capitalFinal:.2f}")