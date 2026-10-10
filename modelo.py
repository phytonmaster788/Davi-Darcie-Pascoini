print("classes e objetos: programação e objeto")



class Aluno():
    nome = ""
    idade = "42"
    nota = 1000
    anotacoes = ""
    ativo = True

    def _init_(self, nome, idade, nota, anotacoes, ativo):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.anotacoes = anotacoes
        self.ativo = ativo


    def ativar(self):
        self.ativo = True


    def desativar(self):
        self.ativo = False

    def apropriado(self):
        if self.nota >=6:
            return "aprovado"
        else:
            return "reprovado"


aluno1 = Aluno(nome = "davi" 
nota = "999"
anotacoes = ""
ativo = True)

print(aluno1)

print("desativando aluno")
aluno1.desativar()

passou = aluno1.aprovado()
print(f"Não sobrou nada pro beta: (passou)")
