def saludar(nombre=None):
    "Imprime un saludo en la pantalla"
    if nombre is None:
        print("Hola.")
    else:
        print(f"Hola, {nombre}.")


def sumar(a, b):
    "Suma dos números"
    suma = a + b
    return suma

def main():
    saludar()
    saludar("Jorge")
    print(saludar())
    print(saludar("xyz"))
    print(sumar(3, 5))
    

if __name__ == "__main__":
    main()
