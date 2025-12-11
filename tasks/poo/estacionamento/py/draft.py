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

    def calcularValor(self, saida: int) -> float:
        calculo = 3
        return calculo

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
        calculo = saida - super().entrada
        calculo = calculo/10
        int(calculo)
        if calculo <= 5:
            calculo = 5
        return calculo

class Estacionamento:
    def __init__(self):
        self.veiculo: list[Veiculo] = []
        self.horaatual:int = 0
    
    def __str__(self) -> str:
        if not self.veiculo:
            return f"{self.horaatual}"

        return f"{self.veiculo}"
    

estacionamento = Estacionamento()

while True:
    a = input()
    args = a.split(" ")

    if args[0] == "show":

