class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print("Código: " + self.codigo)
        print("Nome: " + self.nome)
        print("Matrícula: " + str(self.matricula))
        
class AluEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        Aluno.imprimir(self)
        print("Ano: " + str(self.ano))

class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        Aluno.imprimir(self)
        print("Semestre: " + str(self.semestre))
    
A = Aluno("111", "João", 123)
AeM = AluEnsinoMedio("222","Maria",124, 8)
AG = AlunoGraduacao("333", "Jose", 127, 5)

print("----------Aluno-----------")
A.imprimir()
print("----------Aluno Ensino Médio-----------")
AeM.imprimir()
print("----------Aluno Graduação-----------")
AG.imprimir()

