class No:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None
        
class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def __getitem__(self, index):
        pont = self.topo
        for i in range(index):
            if pont:
                pont = pont.proximo
            else:
                raise IndexError("lista fora de valor")
        if pont:
            return pont.dado
        else:
            raise IndexError("lista fora de valor")

    def inserir(self, elem):
        no = No(elem)
        no.proximo = self.topo
        self.topo = no
        self.tamanho += 1

    def remover(self):
        if self.tamanho > 0:
            no = self.topo
            self.topo = self.topo.proximo
            self.tamanho -= 1
            return print("Elemento removido do topo")
        else:
            print("A pilha está vazia!")

    def imprimir(self):
        if len(pilha) == 0:
            print("A pilha está vazia!")
        else:
            for x in range(len(pilha)):
                print(pilha[x])
pilha = Pilha()

while True:
    menu = input('''
1-Incluir elementos na pilha
2-Remover elementos da pilha
3-Mostrar elementos da pilha
4-Finalizar o programa
Escolha: ''')
    
    if menu == '1':
        elem = input("Digite um elemento: ")
        if elem != '':
            pilha.inserir(elem)
        else:
            print("Campo não pode ser vazio!")
    if menu == '2':
        pilha.remover()
    if menu == '3':
        pilha.imprimir()
    if menu == '4':
        break
    
