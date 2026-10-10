print("aula abstração poliamifero")

class Animal:
    nome = ""
    def nome(self):
        print("Animal")

    def oquecome(self):
        print("comida")

    def habitachi(self):
        print("ondevive")

Animal = Animal()
Animal.nome()
Animal.oquecome()
Animal.habitachi()

