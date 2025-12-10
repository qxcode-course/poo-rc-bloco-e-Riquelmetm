from abc import ABC, abstractmethod
class Veiculo:
    def __init__(self, id:str, entrada:int, tipo: str):
        self.id = id
        self.entrada = entrada
        self.tipo = tipo

    @abstractmethod
    def calcularValor(self):
        pass

    def __str__(self) -> str:
        return f""
    
class Bike(Veiculo):
    def __init__(self, id: str, entrada: int, tipo: str):
        super().__init__(id, entrada, tipo)

class Moto(Veiculo):
    def __init__(self, id: str, entrada: int, tipo: str):
        super().__init__(id, entrada, tipo)

class Carro(Veiculo):
    def __init__(self, id: str, entrada: int, tipo: str):
        super().__init__(id, entrada, tipo)