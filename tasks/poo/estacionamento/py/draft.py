from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self, id:str, entrada:int, tipo:str):
        self.id = id
        self.entrada = entrada
        self.tipo = tipo

    @abstractmethod
    def calcularValor(self, saida:int) -> float:
        pass

    def __str__(self) -> str:
        return f"{self.tipo:_>10} : {self.id:_>10} : {self.entrada}"
    
class Bike(Veiculo):
    def __init__(self, id: str, entrada: int):
        super().__init__(id, entrada, "Bike")

    def calcularValor(self, saida: int) -> float:
        calculo = 3
        return calculo

class Moto(Veiculo):
    def __init__(self, id: str, entrada: int):
        super().__init__(id, entrada, "Moto")
        
    def calcularValor(self, saida:int) -> float:

        calculo = saida - super().entrada
        calculo = calculo/20
        return calculo




class Carro(Veiculo):
    def __init__(self, id: str, entrada: int):
        super().__init__(id, entrada, "Carro")

    def calcularValor(self, saida: int):
        calculo = saida - super().  entrada
        calculo = calculo/10
        if calculo <= 5:
            calculo = 5
        return calculo

class Estacionamento:
    def __init__(self):
        self.veiculo: list[Veiculo] = []
        self.horaatual:int = 0
    
    def estacionar(self, veiculo: Veiculo):
        self.veiculo.append(veiculo)
    
    def pagar(self, id:str):
        encontrado = None
        for i in self.veiculo:
            if i.id == id:
                encontrado = i

        if encontrado:
            valor = encontrado.calcularValor(self.horaatual)
            print(f"{encontrado.tipo} chegou {encontrado.entrada} saiu {self.horaatual}. Pagar R$ {valor}")
            self.veiculo.remove(encontrado)


    def tempo(self, tempo:int):
        self.horaatual += tempo

    
    def __str__(self) -> str:
        lista = "\n".join([str(i) for i in self.veiculo])
        if not self.veiculo:
            return f"Hora atual: {self.horaatual}"

        return f"{lista} \nHora atual: {self.horaatual}"
    

estacionamento = Estacionamento()

while True:
    a = input()
    print("$" + a)
    args = a.split(" ")

    if args[0] == "end":
        break
    
    elif args[0] == "tempo":
        estacionamento.tempo(int(args[1]))

    elif args[0] == "show":
        print(estacionamento)

    elif args[0] == "estacionar":
        tipo = args[1]
        id = args[2]
        if tipo == "bike":
            bike = Bike(id, estacionamento.horaatual)
            estacionamento.estacionar(bike)
        elif tipo == "carro":
            carro = Carro(id, estacionamento.horaatual)
            estacionamento.estacionar(carro)
        elif tipo == "moto":
            moto = Moto(id, estacionamento.horaatual)
            estacionamento.estacionar(moto)

    elif args[0] == "pagar":
        estacionamento.pagar(args[1])
