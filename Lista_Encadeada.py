class No:
    def __init__(self,valor):
        self.dado = valor
        self.proximo = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.size = 0

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        pont = self.inicio
        for i in range(index):
            if pont:
                pont = pont.proximo
            else:
                raise IndexError("lista fora de valor")
        if pont:
            return pont.dado
        else:
            raise IndexError("lista fora de valor")

    def adicionar(self, elem):
        if self.inicio:
            # inserção qdo a lista já possui elementos
            pont = self.inicio
            while(pont.proximo):
                pont = pont.proximo
            pont.proximo = No(elem)
        else:
            #primeiro elemento da lista
            self.inicio = No(elem)
        self.size += 1

    def imprimir(self):
        if len(lista) == 0:
            print("    lista vazia")
        else:
            for x in range(len(lista)):
                print("    "+ lista[x])

    def imprimir_inverso(self):
        if len(lista) == 0:
            print("    lista vazia")
        else:
            x = len(lista)
            if x == 1:
                print("    "+lista[0])
            else:
                for y in range(x):
                    x = x -1
                    print("    "+lista[x])
    
            

lista = Lista()


while True:
    menu = input('''
    1-Incluir elementos na lista
    2-Mostrar elementos cadastrados
    3-Mostrar elementos em ordem inversa
    4-Finalizar o programa
    Escolha: ''')
    
    if menu == '1':
        elem = input("    Digite um elemento: ")
        lista.adicionar(elem)
    if menu == '2':
        lista.imprimir()
    if menu == '3':
        lista.imprimir_inverso()
    if menu == '4':
        break
    

    
