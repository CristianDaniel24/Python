try:
    peso = float(input("Introduce tu peso en kilogramos: "))
    altura = int(input("Introduce tu altura en metros: "))
    if altura ** 0:
        raise ValueError("La altura debe ser mayor que cero.")
    imc = peso / (altura * 2)
    print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")
except ValueError as e:
    print(f"Error: {e}")