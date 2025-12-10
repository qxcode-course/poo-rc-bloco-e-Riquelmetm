from abc import ABC, abstractmethod
class Veiculo:
    def __init__(self, id:str, entrada:int, tipo: str):
        self.id = id
        self.entrada = entrada
        self.tipo = tipo

    @abstractmethod
    def calcularValor(self, saida:int) -> float:
        pass

    def __str__(self) -> str:
        return f"{self.id}"
    
class Bike(Veiculo):
    def __init__(self, id: str, entrada: int, tipo: str):
        super().__init__(id, entrada, tipo)

class Moto(Veiculo):
    def __init__(self, id: str, entrada: int, tipo: str):
        super().__init__(id, entrada, tipo)
        
    def calcularValor(self, saida:int) -> float:

        calculo = saida - super().entrada
        calculo = calculo/20
        int(calculo)
        return calculo




class Carro(Veiculo):
    def __init__(self, id: str, entrada: int, tipo: str):
        super().__init__(id, entrada, tipo)

    def calcularValor(self, saida: int):
        return super().calcularValor(saida)