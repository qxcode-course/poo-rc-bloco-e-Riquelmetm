from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, id:int, clienteid:str, saldo_atual:float, tipoid:str):
        self.id = id
        self.clienteid = clienteid
        self.saldo = saldo_atual
        self.tipoid = tipoid

    def despositar(self, saldo:float):
        self.saldo+= saldo
        return

    def saque(self, saque:float):
        if saque > self.saldo:
            print("fail: conta nao encontrada")
            return
        self.saldo -= saque
    