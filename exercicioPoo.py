class Retangulo:
    def __init__(self):
        self.altura = None
        self.largura = None
    def calcularArea(self):
        return (self.altura * self.largura)
    def imprimir(self):
        print("Altura: " + str(self.altura) + " Largura: " + str(self.largura))

retangulo = Retangulo()
while True:
    menu = input('''
1-Calcular área do retângulo
2-Imprimir valores da altura e largura
3-Sair
Escolha: ''')
    
    if menu == '1':
        try:
            altura = float(input("Digite a altura: "))
            largura = float(input("Digite a largura: "))
            retangulo.altura = altura
            retangulo.largura = largura
            print(retangulo.calcularArea())
        except:
            input("Valores digitados são inválidos![ENTER]")
    if menu == '2':
        if retangulo.altura:
            retangulo.imprimir()
        else:
            input("É preciso primeiro calcular a área do retângulo![ENTER]")
    if menu == '3':
        break
