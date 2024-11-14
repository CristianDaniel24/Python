"""
TODO: TENEMOS LA PANTALLA DEL MOVIL BLOQUEADA. PARTIENDO DE UN PIN_SECRETO INTENTAREMOS DESBLOQUEAR LA PANTALLA.
TODO: TENEMOS HASTA 3 INTENTOS SIMULA EL PROCESO CON PYTHON. EN CASO DE ACCEDER LANZA AL USUARIO
"""

#NUMERO DE INTENTOS
attempts = 3
i = 0
while i < attempts:
    i += 1
    # PIN: 123
    pin = input("Enter the pin for unlock the phone:")
    if pin == "123":
        print("Login correct")
        break
    else:
        print("Pin incorrect")