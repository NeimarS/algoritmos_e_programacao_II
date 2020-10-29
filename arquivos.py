# encoding: utf-8

import os.path

def comprar_produtos():
    #carregar lista carrinho
    if len(carrinho) == 0:
        if os.path.isfile('produto.txt'):
            arquivo = open("produto.txt","r")
            for linha in arquivo:
                valor = str(linha.split())#tira linha em branco mas adiciona colchetes, transforma em string
                val = valor[2:len(valor)-2]#remover colchetes 
                carrinho.append(val)
            arquivo.close()
    #listar produtos a venda        
    for i in range(len(lista_produtos)):
        print(i,lista_produtos[i])  
    try:
        escolha = int(input("Escolha o produto pelo código: "))
        if lista_produtos[escolha]:
            carrinho.append(lista_produtos[escolha])
            #salvar lista carrinho no arquivo
            arq = open("produto.txt","w")
            for x in range(len(carrinho)):
                arq.write(carrinho[x]+"\n")
            arq.close()
            print("Produto adicionado na lista!")      
    except:
        input("Código inexistente!")
        comprar_produtos()

def alterar_produto():
    l = 0
    if os.path.isfile('produto.txt'):
       carrinho.clear() 
       arquivo = open('produto.txt', 'r')
       for linha in arquivo:
           valor = str(linha.split())#tira linha em branco mas adiciona colchetes, transforma em string
           val = valor[2:len(valor)-2]#remover colchetes 
           carrinho.append(val)
           print(str(l)+"-"+val)
           l = l + 1
       arquivo.close()
       try:
           escolha = int(input("Escolha o produto a ser substituido: "))    
           try:
               if carrinho[escolha]:
                   for i in range(len(lista_produtos)):
                       print(i,lista_produtos[i])
                   novo_produto = int(input("Escolha o novo produto para adicionar: "))
                   carrinho[escolha] = lista_produtos[novo_produto]
                   arquivo = open("produto.txt","w")
                   for x in range(len(carrinho)):
                       arquivo.write(carrinho[x]+"\n")
                   arquivo.close()
                   print("Produto alterado com sucesso!")
               else:
                   input("indice inválido!")
           except:
               input("indice inválido!")
       except:
           input("Indice escolhido é inválido!")
    else:
        print("Lista de produtos não foi criada ainda.")
    
lista_produtos = ['banana', 'maçã', 'abacaxi', 'abacate', 'mamão', 'laranja', 'bergamota', 'pitaya', 'ameixa']
carrinho = []

while True:
    menu = input('''
##### MENU #####
0- Finalizar o Programa
1- Comprar Produtos
2- Alterar produtos 
Escolha: ''')
    if menu == '0':
        break
    if menu == '1':
        comprar_produtos()
    if menu == '2':
        alterar_produto()
        
