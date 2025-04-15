def suma(a, b):
    return a + b

def calculadora():
    print("Calculadora simple")
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    operacion = input("Ingrese el número de la operación (1/2/3/4): ")

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if operacion == "1":
        resultado = suma(num1, num2)
        print(f"El resultado de la suma es: {resultado}")
    elif operacion == "2":
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    elif operacion == "3":
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif operacion == "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("¡Error! No se puede dividir entre cero.")
    else:
        print("Operación no válida")

calculadora()
