
weight = float(input("Enter your weight in Kg:"))

stature = float(input("Enter your stature in centimeters:"))

# Convertir la estatura de centimetros a metros
stature = stature / 100

imc = weight / (stature ** 2)

imcRedondeado = round(imc, 2)

print(f"Your body mass is:{imcRedondeado}")