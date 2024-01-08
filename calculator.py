# Definición de Funciones de Operaciones Matemáticas
def sumar (x,y):
    return x+y

def restar(x,y):
    return x-y

def multiplicar(x,y):
    return x*y

def dividir(x,y):
    if y == 0:
        return "Error: No se puede dividir por cero"
    return x/y

# Menú de Usuario
def mostrar_menu():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    eleccion = input("Ingresa tu eleccion (1/2/3/4/5): ")
    return eleccion

# Ejecución de Operaciones y Mostrar Resultados
def main():
    while True:
        eleccion = mostrar_menu()

        if eleccion in ['1', '2', '3', '4']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if eleccion == '1':
                print("Resultado:", sumar(num1, num2))
            elif eleccion == '2':
                print("Resultado:", restar(num1, num2))
            elif eleccion == '3':
                print("Resultado:", multiplicar(num1, num2))
            elif eleccion == '4':
                print("Resultado:", dividir(num1, num2))

        elif eleccion == '5':
            print("Saliendo de la calculadora...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
