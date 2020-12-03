import mysql.connector

class Plano:
    def __init__(self, id, nome, carencia, valor):
        self.id = id
        self.nome = nome
        self.carencia = int(carencia)
        self.valor = float(valor)

class Individual(Plano):
    def __init__(self, id, nome, carencia, valor):
        Plano.__init__(self, id, nome, carencia, valor)

    def pl_individual(self):
        conexao = mysql.connector.connect(host='localhost',database='plano_saude',user='root', password='')
        if conexao.is_connected():
            query = "insert into planos(nome, carencia, valor) values('"+self.nome+"',"+str(self.carencia)+","+str(self.valor)+")"
            cursor = conexao.cursor()
            cursor.execute(query)
            conexao.commit()
            cursor.close()
            conexao.close()
            print("Plano cadastrado com sucesso!")
        else:
            print("Não foi possível conectar-se ao banco")
          
class Familiar(Plano):
    def __init__(self, id, nome, carencia, valor, qtde_pessoas):
        Plano.__init__(self, id, nome, carencia, valor)
        self.qtde_pessoas = int(qtde_pessoas)

    def pl_familiar(self):
        conexao = mysql.connector.connect(host='localhost',database='plano_saude',user='root', password='')
        if conexao.is_connected():
            query = "insert into planos(nome, carencia, valor, qtde_pessoas) values('"+self.nome+"',"+str(self.carencia)+","+str(self.valor)+", "+str(self.qtde_pessoas)+")"
            cursor = conexao.cursor()
            cursor.execute(query)
            conexao.commit()
            cursor.close()
            conexao.close()
            print("Plano cadastrado com sucesso!")
        else:
            print("Não foi possível conectar-se ao banco")    

class Empresarial(Plano):
    def __init__(self, id, nome, carencia, valor, qtde_pessoas, qtde_minima_pessoas):
        Plano.__init__(self, id, nome, carencia, valor)
        self.qtde_pessoas = int(qtde_pessoas)
        self.qtde_minima_pessoas = qtde_minima_pessoas

    def pl_empresarial(self):
        conexao = mysql.connector.connect(host='localhost',database='plano_saude',user='root', password='')
        if conexao.is_connected():
            query = "insert into planos(nome, carencia, valor, qtde_pessoas, qtde_minima_pessoas) values('"+self.nome+"',"+str(self.carencia)+","+str(self.valor)+", "+str(self.qtde_pessoas)+","+str(self.qtde_minima_pessoas)+")"
            cursor = conexao.cursor()
            cursor.execute(query)
            conexao.commit()
            cursor.close()
            conexao.close()
            print("Plano cadastrado com sucesso!")
        else:
            print("Não foi possível conectar-se ao banco")    

class Pessoa:
    def __init__(self, id, endereco, telefone):
        self.id = id
        self.endereco = endereco
        self.telefone = telefone

class Fisica(Pessoa):
    def __init__(self, id, endereco, telefone, nome, idade):
        Pessoa.__init__(self, id, endereco, telefone)
        self.nome = nome
        self.idade = int(idade)

    def p_fisica(self):
        conexao = mysql.connector.connect(host='localhost',database='plano_saude',user='root', password='')
        if conexao.is_connected():
            query = "insert into clientes(endereco, telefone, nome, idade) values('"+self.endereco+"','"+self.telefone+"','"+self.nome+"', "+str(self.idade)+")"
            cursor = conexao.cursor()
            cursor.execute(query)
            conexao.commit()
            cursor.close()
            conexao.close()
            print("Plano cadastrado com sucesso!")
        else:
            print("Não foi possível conectar-se ao banco")        

class Juridica(Pessoa):
    def __init__(self, id, endereco, telefone, razaoSocial):
        Pessoa.__init__(self, id, endereco, telefone)
        self.razaoSocial = razaoSocial

    def p_juridica(self):
        conexao = mysql.connector.connect(host='localhost',database='plano_saude',user='root', password='')
        if conexao.is_connected():
            query = "insert into clientes(endereco, telefone, razaosocial) values('"+self.endereco+"','"+self.telefone+"', '"+self.razaoSocial+"')"
            cursor = conexao.cursor()
            cursor.execute(query)
            conexao.commit()
            cursor.close()
            conexao.close()
            print("Plano cadastrado com sucesso!")
        else:
            print("Não foi possível conectar-se ao banco")

class Contratar():
    def __init__(self, id, cliente, plano):
        self.id = id
        self.cliente = int(cliente)
        self.plano = int(plano)

    def pl_contratar(self, id_cliente, id_plano):
        conexao = mysql.connector.connect(host='localhost',database='plano_saude',user='root', password='')
        if conexao.is_connected():
            cursor = conexao.cursor()
            cursor.execute("select * from planos where id = "+str(id_plano))
            result = cursor.fetchall()
            if len(result) == 0:
                print("Id não encontrado!")
            else:
                cursor.execute("select * from clientes where id = "+str(id_cliente))
                result = cursor.fetchall()
                if len(result) == 0:
                    print("Id não encontrado!")
                else:
                    query = "insert into contratos(cliente, plano) values("+str(self.cliente)+","+str(self.plano)+")"
                    cursor = conexao.cursor()
                    cursor.execute(query)
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    print("plano contratado com sucesso!")
        else:
            print("Não foi possível conectar-se ao banco")
        
        
######################## fim das classes ############################            

def plano_individual():
    print("############### CADASTRAR PLANO INDIVIDUAL ###############")
    try:
        nome = input("Digite o nome do plano: ")
        carencia = int(input("Digite a carência do plano em meses: "))
        valor = float(input("Digite o valor do plano: "))
        plano = Individual(0,nome, carencia, valor)
        plano.pl_individual()
        
    except:
        input("Houve erro na digitação de algum valor, verifique e tente novamente.[ENTER]")

def plano_familiar():
    print("############### CADASTRAR PLANO FAMILIAR ###############")
    try:
        nome = input("Digite o nome do plano: ")
        carencia = int(input("Digite a carência do plano em meses: "))
        valor = float(input("Digite o valor do plano: "))
        qtde_pessoas = int(input("Digite a quantidade de pessoas: "))
        plano = Familiar(0,nome, carencia, valor, qtde_pessoas)
        plano.pl_familiar()
        
    except:
        input("Houve erro na digitação de algum valor, verifique e tente novamente.[ENTER]")

def plano_empresarial():
    print("############### CADASTRAR PLANO EMPRESARIAL ###############")
    try:
        nome = input("Digite o nome do plano: ")
        carencia = int(input("Digite a carência do plano em meses: "))
        valor = float(input("Digite o valor do plano: "))
        qtde_pessoas = int(input("Digite a quantidade de pessoas: "))
        qtde_minima_pessoas = int(input("Digite a quantidade mínima de pessoas para esse plano: "))
        plano = Empresarial(0,nome, carencia, valor, qtde_pessoas, qtde_minima_pessoas)
        plano.pl_empresarial()
        
    except:
        input("Houve erro na digitação de algum valor, verifique e tente novamente.[ENTER]")


def pessoa_fisica():
    print("############### CADASTRAR PESSOA FISICA ###############")
    try:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        endereco = input("Digite o endereço: ")
        telefone = input("Digite o telefone: ")
        pf = Fisica(0,endereco, telefone, nome, idade)
        pf.p_fisica()
        
    except:
        input("Houve erro na digitação de algum valor, verifique e tente novamente.[ENTER]")

def pessoa_juridica():
    print("############### CADASTRAR PESSOA JURÍDICA ###############")
    try:
        razaosocial = input("Digite a razão social: ")
        endereco = input("Digite o endereço: ")
        telefone = input("Digite o telefone: ")
        pj = Juridica(0,endereco, telefone, razaosocial)
        pj.p_juridica()
        
    except:
        input("Houve erro na digitação de algum valor, verifique e tente novamente.[ENTER]")
   
def cadastrar_plano():
    
    while True:
        menu = input('''
    ##### ESCOLHA O TIPO DE PLANO #####
    1-Individual
    2-Familiar 
    3-Empresarial
    4-Voltar para o menu anterior
    Escolha: ''')
    
        if menu == '1':
            plano_individual()
        if menu == '2':
            plano_familiar()
        if menu == '3':
            plano_empresarial()
        if menu == '4':
            break

def cadastrar_cliente():
    
    while True:
        menu = input('''
    ##### ESCOLHA O TIPO DE PLANO #####
    1-Pessoa Fisica
    2-Pessoa Jurídica 
    3-Voltar para o menu anterior
    Escolha: ''')
    
        if menu == '1':
            pessoa_fisica()
        if menu == '2':
            pessoa_juridica()
        if menu == '3':
            break
        
             
def contratar_plano():
    try:
        print("##### CONTRATAÇÃO DE PLANOS #####")
        rel_clientes()

        id_cliente = int(input("Escolha o cliente pelo indice: "))
        
        rel_planos()

        id_plano = int(input("Escolha o plano pelo indice: "))
        contrato = Contratar(0, id_cliente, id_plano)
        contrato.pl_contratar(id_cliente, id_plano)
    except:
        input("Houve erro na digitação de algum valor, verifique e tente novamente.[ENTER]")
        
def relatorios():
    while True:
        menu = input('''
    ##### ESCOLHA O TIPO DE RELATORIO #####
    1-Relação de clientes
    2-Relação de planos 
    3-Relação de contratos
    4-Voltar para o menu anterior
    Escolha: ''')
    
        if menu == '1':
            rel_clientes()
        if menu == '2':
            rel_planos()
        if menu == '3':
            rel_contratos()
        if menu == '4':
            break


def rel_clientes():
    conexao = mysql.connector.connect(host='localhost',database='plano_saude',user='root', password='')
    if conexao.is_connected():
        query = "select id, nome, razaosocial from clientes"
        cursor = conexao.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        for linha in result:
            print("Índice:", linha[0], "Nome: ", linha[1],"Razão Social: ", linha[2])
            print("--------------------------------------")
        cursor.close()
        conexao.close()
    else:
        print("Não foi possível conectar-se ao banco")

def rel_planos():
    conexao = mysql.connector.connect(host='localhost',database='plano_saude',user='root', password='')
    if conexao.is_connected():
        query = "select id, nome, carencia, valor from planos"
        cursor = conexao.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        for linha in result:
            print("Índice:", linha[0], "Nome: ", linha[1],"Carência: ", linha[2], "Valor: ", linha[3])
            print("--------------------------------------")
        cursor.close()
        conexao.close()
    else:
        print("Não foi possível conectar-se ao banco")


def rel_contratos():
    conexao = mysql.connector.connect(host='localhost',database='plano_saude',user='root', password='')
    if conexao.is_connected():
        query = "select contratos.id, clientes.nome, razaosocial, planos.nome, carencia, valor from planos, clientes, contratos where contratos.cliente = clientes.id and contratos.plano = planos.id"
        cursor = conexao.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        for linha in result:
            print("Id:",linha[0],"Nome:", linha[1], "Razão Social: ", linha[2],"Nome Plano: ", linha[3], "Carência: ", linha[4], "Valor: ", linha[5])
            print("--------------------------------------")
        cursor.close()
        conexao.close()
    else:
        print("Não foi possível conectar-se ao banco")
    

def excluir():
    while True:
        menu = input('''
    ##### ESCOLHA O TIPO DE EXCLUSÃO #####
    1-Clientes
    2-Planos 
    3-Contratos
    4-Voltar para o menu anterior
    Escolha: ''')
    
        if menu == '1':
            excluir_clientes()
        if menu == '2':
            excluir_planos()
        if menu == '3':
            excluir_contratos()
        if menu == '4':
            break

def excluir_clientes():
    try:
        print("##### EXCLUSÃO DE CLIENTES #####")
        rel_clientes()
        excluir = int(input("Digite o id do cliente: "))
    
        conexao = mysql.connector.connect(host='localhost',database='plano_saude',user='root', password='')
        if conexao.is_connected():
            cursor = conexao.cursor()
            cursor.execute("select * from contratos where cliente = "+str(excluir))
            result = cursor.fetchall()
            if len(result) >0:
                print("Cliente possui contratos em aberto, exclua primeiro o contrato!")
            else:
                cursor.execute("select * from clientes where id = "+str(excluir))
                result = cursor.fetchall()
                if len(result) == 0:
                    print("Id não existente!")
                else:
                    cursor.execute("delete from clientes where id = "+str(excluir))
                    conexao.commit()
                    print("Cliente excluído com sucesso!")
                
            cursor.close()
            conexao.close()
        else:
            print("Não foi possível conectar-se ao banco")
    except:
        input("Houve erro na digitação de algum valor, verifique e tente novamente.[ENTER]")

def excluir_planos():
    try:
        print("##### EXCLUSÃO DE PLANOS #####")
        rel_planos()
        excluir = int(input("Digite o id do plano: "))
    
        conexao = mysql.connector.connect(host='localhost',database='plano_saude',user='root', password='')
        if conexao.is_connected():
            cursor = conexao.cursor()
            cursor.execute("select * from contratos where plano = "+str(excluir))
            result = cursor.fetchall()
            if len(result) >0:
                print("Plano possui contrato(s) com cliente(s) em aberto, exclua primeiro o contrato!")
            else:
                cursor.execute("select * from planos where id = "+str(excluir))
                result = cursor.fetchall()
                if len(result) == 0:
                    print("Id não existente!")
                else:
                    cursor.execute("delete from planos where id = "+str(excluir))
                    conexao.commit()
                    print("Plano excluído com sucesso!")
                
            cursor.close()
            conexao.close()
        else:
            print("Não foi possível conectar-se ao banco")
    except:
        input("Houve erro na digitação de algum valor, verifique e tente novamente.[ENTER]")        

def excluir_contratos():
    try:
        print("##### EXCLUSÃO DE CONTRATOS #####")
        rel_contratos()
        excluir = int(input("Digite o id do contrato: "))
    
        conexao = mysql.connector.connect(host='localhost',database='plano_saude',user='root', password='')
        if conexao.is_connected():
            cursor = conexao.cursor()
            cursor.execute("select * from contratos where id = "+str(excluir))
            result = cursor.fetchall()
            if len(result) == 0:
                print("Id digitado não existe!")
            else:
                cursor.execute("delete from contratos where id = "+str(excluir))
                conexao.commit()
                print("Contrato excluído com sucesso!")
                
            cursor.close()
            conexao.close()
        else:
            print("Não foi possível conectar-se ao banco")
    except:
        input("Houve erro na digitação de algum valor, verifique e tente novamente.[ENTER]")        
        
        '''
        if conexao.is_connected():
        query = "insert into produtos(nome, preco) values('"+nome+"',"+preco+")"
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        cursor.execute("select * from produtos")
        result = cursor.fetchall()
        for linha in result:
            print("Id:", linha[0], "Nome: ", linha[1],"Preço: ", linha[2])
            print("--------------------------------------")
        excluir_id = input("Digite o Id a ser excluído: ")
        cursor.execute("delete from produtos where id = "+excluir_id)
        conexao.commit()
        
        cursor.close()
        conexao.close()
        else:
           print("Não foi possível conectar-se ao banco")
        '''   


conexao = mysql.connector.connect(host='localhost',database='plano_saude',user='root', password='')

while True:
    menu = input('''
    1-Cadastrar Plano de Saúde
    2-Cadastrar cliente
    3-Contratar plano
    4-Excluir cliente/plano/contrato
    5-Relatórios
    6-Finalizar o programa
    Escolha: ''')
    
    if menu == '1':
        cadastrar_plano()
    if menu == '2':
        cadastrar_cliente()
    if menu == '3':
        contratar_plano()
    if menu == '4':
        excluir()
    if menu == '5':
        relatorios()
    if menu == '6':
        break
