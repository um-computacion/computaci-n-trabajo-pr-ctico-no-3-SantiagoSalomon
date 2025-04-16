class ValueError(Exception):
    def __init__(self, message="La entrada debe ser un número válido"):
        self.message = message
        super().__init__(self.message)

class NumeroDebeSerPositivo(Exception):
    def __init__(self, message="El número debe ser positivo"):
        self.message = message
        super().__init__(self.message)