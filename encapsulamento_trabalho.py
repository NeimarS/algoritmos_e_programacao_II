class Pessoa:
    def __init__(self,codigo, nome, endereco, telefone):
        self.__codigo = int(codigo)
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone

    def ImprimeNome(self):
        print(self.nome)

    def __ImprimeTelefone(self):
        print(self.__telefone)
        
class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self,codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def imprimeCPF(self):
        print(self.__cpf)
    def __calculaIMC(self):
        return (self.peso/(self.altura * self.altura))

class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, CNPJ, inscricaoEstadual, qtdeFuncionarios):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__CNPJ = CNPJ
        self.__inscricaoEstadual = inscricaoEstadual
        self.qtdeFuncionarios = int(qtdeFuncionarios)
    def imprimeCNPJ(self):
        print(self.__CNPJ)
    def __emitirNotaFiscal(self):
        print("Nota fiscal")
            
M = Pessoa(10, "teste", "rua a", 123)
print(M.ImprimeNome())
        
    



