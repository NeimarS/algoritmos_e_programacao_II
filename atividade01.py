#Atividade 01
def incluir():
    try:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        qtde = int(input("Digite a quantidade do produto: "))
        if nome != '' and preco > 0 and qtde > 0:
            lst_nome_produto.append(nome)
            lst_preco_produto.append(preco)
            lst_qtde_produto.append(qtde)
            input("Produto cadastrado com sucesso![ENTER]")
        else:
            input("O nome do produto não pode ser vazio e o preço e quanidade deve ser maior que 0. [ENTER]")
            incluir()
    except:
        input("Ocorreu um erro nos dados informados, tente novamente!")
        incluir()

def mostrar():
    flag = 0
    if len(lst_nome_produto) == 0:
        input("Nenhum produto cadastrado! [ENTER]")
    else:
        print("----------------------------------------")
        print("indice - nome")
        for x in range(len(lst_nome_produto)):
            print(str(x).ljust(9," ") + lst_nome_produto[x])
        try:
            indice = int(input("Digite o índice do produto: "))
            for y in range(len(lst_nome_produto)):
                if y == indice:
                    flag = 1
            if flag == 1:
                print("----------------------------------------")
                print("indice - nome           - quantidade - preço")
                print(str(indice).ljust(9," ") + lst_nome_produto[indice].ljust(22, " ") + str(lst_qtde_produto[indice]).ljust(8," ")+ str(lst_preco_produto[indice]))
                input("[ENTER] para sair")
            else:
                input("Índice não está na lista! [ENTER]")
                mostrar()
        except:
            input("Índice inválido!")
            mostrar()

def remover():
    if len(lst_nome_produto) == 0:
        input("Nenhum produto cadastrado! [ENTER]")
    else:
        print("----------------------------------------")
        print("indice - nome")
        for x in range(len(lst_nome_produto)):
            print(str(x).ljust(9," ") + lst_nome_produto[x])
        try:
            indice = int(input("Digite o índice do produto a remover: "))
            for y in range(len(lst_nome_produto)):
                if y == indice:
                    flag = 1
            if flag == 1:
                del lst_nome_produto[indice]
                del lst_preco_produto[indice]
                del lst_qtde_produto[indice]
                input("Produto removido com sucesso![ENTER]")
            else:
                input("Índice não está na lista! [ENTER]")
                remover()
        except:
            input("Índice inválido! [ENTER]")
            remover()    
                  
lst_nome_produto = []
lst_preco_produto = []
lst_qtde_produto = []

while True:
    menu = input('''
    1-Incluir produto na lista
    2-Mostrar dados do produto cadastrado
    3-Remover produto pelo índice
    4-Finalizar o programa
    Escolha: ''')
    
    if menu == '1':
        incluir()
    if menu == '2':
        mostrar()
    if menu == '3':
        remover()
    if menu == '4':
        break
    
