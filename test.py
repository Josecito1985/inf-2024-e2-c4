


# Solicitar el año de nacimiento
try:
    anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))
    
    # Calcular la edad actual
    anio_actual = 2024
    edad = anio_actual - anio_nacimiento
    
    # Verificar si es mayor de edad
    if edad >= 18:
        print(f"Tienes {edad} años, eres mayor de edad.")
    else:
        print(f"Tienes {edad} años, aún no eres mayor de edad.")

except ValueError:
    print("Por favor, ingresa un número válido para el año de nacimiento.")

