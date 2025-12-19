from abc import ABC, abstractmethod
class Animal:
    def __init__(self, nome:str):
        self.nome = nome

    
    def apresentar(self):
        return f"Eu sou um {self.nome}"
    
    @abstractmethod
    def fazer_som(self):
        pass
    
    @abstractmethod
    def mover(self):
        pass


class Gato(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)
    
    def fazer_som(self):
        print("Miau")
        return
    
    def mover(self):
        print("Andar ")
        return