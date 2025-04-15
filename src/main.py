from operaciones import sumar, restar, multiplicar, dividir

def main():
    while True:
        operacion = input("Escribe una operación (ej. 2 + 2) o 'c' para limpiar: ")

        if operacion.lower() == 'c':
            print("Operación borrada.")
            continue

        try:
            partes = operacion.strip().split()
            if len(partes) != 3:
                print("Formato inválido. Usa: número operador número (ej. 5 + 3)")
                continue

            num1 = float(partes[0])
            operador = partes[1]
            num2 = float(partes[2])

            if operador == '+':
                resultado = sumar(num1, num2)
            elif operador == '-':
                resultado = restar(num1, num2)
            elif operador == '*':
                resultado = multiplicar(num1, num2)
            elif operador == '/':
                resultado = dividir(num1, num2)
            else:
                print("Operador no reconocido.")
                continue

            print(f"Resultado: {resultado}\n")

        except ValueError:
            print("Error: asegúrate de escribir números válidos.")
        except ZeroDivisionError:
            print("Error: división por cero.")

if __name__ == "__main__":
    main()
