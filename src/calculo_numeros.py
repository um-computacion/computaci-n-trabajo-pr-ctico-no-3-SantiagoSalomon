from src.exceptions import ValueError, NumeroDebeSerPositivo

def ingrese_numero():
    try:
        numero = float(input("Ingrese un número: "))
        if numero < 0:
            raise NumeroDebeSerPositivo("El número debe ser positivo")
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un número válido")