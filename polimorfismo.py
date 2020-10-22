class Veiculo:
    def __init__(self,marca, qtdRodas, modelo, velocidade=0):
        self.__marca = marca
        self.__qtdRodas = int(qtdRodas)
        self.__modelo = modelo
        self.__velocidade = velocidade
    def imprimirInformacoes(self):
        print("Marca: " + self.__marca)
        print("Quantidade rodas: " + str(self.__qtdRodas))
        print("Modelo: " + self.__modelo)
        print("Velocidade: " + str(self.__velocidade))
    def acelerar(self, valor):
        self.__velocidade = valor
    def frear(self, valor):
        self.__velocidade = valor
        
class Bicicleta(Veiculo):
    def __init__(self,marca,qtdRodas, modelo, velocidade, numMarchas, bagageiro):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.__numMarchas = int(numMarchas)
        self.__bagageiro = bool(bagageiro)
    def imprimirInformacoes(self):
        Veiculo.imprimirInformacoes(self)
        print("Número de marchas: " +str(self.__numMarchas))
        print("Tem bagageiro: " +str(self.__bagageiro))

class Automovel(Veiculo):
    def __init__(self,marca, qtdRodas, modelo, velocidade, potenciaDoMotor):
        Veiculo.__init__(self, marca,qtdRodas, modelo, velocidade)
        self.__potenciaDoMotor = float(potenciaDoMotor)
    def imprimirInformacoes(self):
        Veiculo.imprimirInformacoes(self)
        print("Potência do motor: " + str(self.__potenciaDoMotor))

class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor,partidaEletrica):
        Automovel.__init__(self,marca, qtdRodas, modelo, velocidade,potenciaDoMotor)
        self.__partidaEletrica = bool(partidaEletrica)
    def imprimirInformacoes(self):
        Automovel.imprimirInformacoes(self)
        print("Partida Eletrica: " + str(self.__partidaEletrica))

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, qtdPortas):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.__qtdPortas = int(qtdPortas)
    def imrpimirInformacoes(self):
        Automovel.imprimirInformacoes(self)
        print("Quantidade de Portas: " +str(self.__qtdPortas))

veiculo = Veiculo("fiat",4,"2011", 80)
veiculo.acelerar(90)
veiculo.frear(40)
veiculo.imprimirInformacoes()
print("===================================================")
bicicleta = Bicicleta("Caloi",2,"Caloi",20,20,True)
bicicleta.imprimirInformacoes()
print("===================================================")
automovel = Automovel("ford", 4, "Vectra",85, 400)
automovel.imprimirInformacoes()
print("===================================================")
moto = Moto("yamaha", 2, "fazer 250",67, 250, True)
moto.imprimirInformacoes()
print("===================================================")
carro = Carro("toyota", 4, "corolla", 89, 550, 4)
carro.imprimirInformacoes()
