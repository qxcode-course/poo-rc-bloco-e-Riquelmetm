from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, id:int, clienteid:str, saldo_atual:float, tipoid:str):
        self.id = id
        self.clienteid = clienteid
        self.saldo = saldo_atual
        self.tipoid = tipoid

    