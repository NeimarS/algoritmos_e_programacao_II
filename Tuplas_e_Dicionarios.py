#Exercício 1
def m_num():
    num = "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"
    try:
        numero = int(input("Digite um número de 0 a 9: "))
        print(num[numero])
    except:
        print("Valor digitado é inválido")
        m_num()

#Exercício 2
def dic():
    try:
        nome = input("Digite seu nome: ")
        if nome:
            nota1 = float(input("Digite a nota 1: "))
            if nota1:
                nota2 = float(input("Digite a nota 2: "))
            else:
                input("Valor digitado é invalido [ENTER]")
                dic()
        else:
            input("Valor digitado é invalido [ENTER]")
            dic()
        dicionario = {"nome": nome, "nota1": nota1,"nota2":nota2}
        nota_final = (nota1 + nota2) /2
        dicionario["nota final"] = nota_final
        print("------ Dados do Aluno ------")
        for key in dicionario:
            print(str(key) + " : " + str(dicionario[key]))
        
    except:
        input("Valor digitado é invalido [ENTER]")
        dic()      
    
while True:
    menu = input('''
    1-Exercício 1
    2-Exercício 2
    3-Sair
    Escolha: ''')
    if menu == '1':
        m_num()
    if menu == '2':
        dic()
    if menu == '3':
        break

    
