
"""
edad = int(input("Enter your age:"))
if edad >=18:
    print("You are of legal age")
else:
    print("You are a minor")
"""
print("TIPOS DE VARIABLES")
var1 = 42
var2 = 3.14
var3 = "Hola mundo"
var4 = [1,2,3,4]
var5 = (True, False)
var6 = {'nombre': 'Juan', 'edad': 25}

print("var 1:",var1,"- Tipo",type(var1))
print("var 2:",var2,"- Tipo",type(var2))
print("var 3:",var3,"- Tipo",type(var3))
print("var 4:",var4,"- Tipo",type(var4))
print("var 5:",var5,"- Tipo",type(var5))
print("var 6:",var6,"- Tipo",type(var6), end= "\n\n")

cadena1 = 'Hola mundo!'
cadena2 = 'Python es &'
cadena3 = 'Esto es un String multilinea'

print("cadena 1:", cadena1)
print("cadena 2:", cadena2)
print("cadena 3:", cadena3)

primer_caracter = cadena1[0]
print("El primer caracter de la cadena 1:", primer_caracter, end= "\n\n")


cadena1 = "Las comillas dobles permiten imprimir texto"
cadena2 = """Cuando se usan las 3 comillas permiten imprimir
Strings multilinea
"""

print("cadena 1:", cadena1)
print("cadena 2:", cadena2)

cadenaMayuscula = cadena1.upper()
print("El metodo .upper perimite transformar un texto en Mayusculas por ejemplo:", cadenaMayuscula)

cadenaReemplazada = cadena1.replace("&","Esta es la cadena reemplazada")
print("Cadena despues de ser reemplazada:",cadenaReemplazada)

