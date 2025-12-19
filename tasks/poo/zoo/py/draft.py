from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, nome:str):
        self.nome = nome

    
    def apresentar(self):
        print(f"Eu sou um {self.nome}")
        return
    
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
        print("Andar e dormir")
        return
class Cachorro(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)
    
    def fazer_som(self):
        print("Auau")
        return
    
    def mover(self):
        print("Correr e comer")
        return


class Passarinho(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)
    
    def fazer_som(self):
        print("Piupiu")
        return
    
    def mover(self):
        print("Voar")
        return
    
def apresentar(animal:Animal):
    animal.apresentar()
    animal.fazer_som()
    animal.mover()
gato = Gato("Gato")
cachorro = Cachorro("Cachorro")
passarinho = Passarinho("Passarinho")

animais = [
    gato ,
    cachorro,
    passarinho
    ]
for i in animais:
    apresentar(i)