from time import sleep

nomeProduto = ["COCA", "FANTA", "PEPSI", "GUARANA ANTARTICA", "FRUKI"]
precoProduto = ["8,00", "5,00", "5,50", "4,50", "4,00"]
qtdProduto = ["40", "100", "30", "3", "120"]

def joinha():
    print('''    ..Finalizando Programa.. ByeBye     ''') 
    sleep(0.5)
    print('''░░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░''')
    sleep(0.5)
    print('''░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░''')
    sleep(0.5)
    print('''░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░''')
    sleep(0.5)
    print('''░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░''')
    sleep(0.5)
    print('''░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░''')
    sleep(0.5)
    print('''░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██''')
    sleep(0.5)
    print('''░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██''')
    sleep(0.5)
    print('''░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██''')
    sleep(0.5)
    print('''░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██''')
    sleep(0.5)
    print('''██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██''')
    sleep(0.5)
    print('''█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██''')
    sleep(0.5)
    print('''██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░''')
    sleep(0.5)
    print('''░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░''')
    sleep(0.5)
    print('''░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░''')
    sleep(0.5)
    print('''░░████████████░░░█████████████████░░░░░░''')
    print('''           FUNÇÃO JOINHA.               ''')
    print('''© 2021 Edinho Grano. All Rights Reserved.''')

def header():
    print('''
        ----------------------------------------------------------------------------------------        
       | ============== NOME ============== | ====== PREÇO ====== | == QUANTIDADE EM ESTOQUE == | 
       |------------------------------------|---------------------|-----------------------------|''')

def erro():
    print("Digite um valor válido!")

def produto():

    while True:
        nome = input("Digite o nome do produto: ").upper()
        if len(nome) == 0 or nome.isnumeric():
            erro()
        else:
            nomeProduto.append(nome)
            break

def preco():
    while True:
        preco = input("Digite o valor do produto: ")
        if len(preco) == 0 or preco.isalnum():
            erro()
        else:
            precoProduto.append(preco)
            break

def quantidade():
    while True:
        quantidade = input("Digite a quantidade de produtos: ")
        if len(quantidade) == 0 or not quantidade.isnumeric():
            erro()
        else:
            qtdProduto.append(quantidade)
            break

def relatorio():
    # 36,21,29    
    header()
    for x in range(len(nomeProduto)):
        print("       |{:^36}|{:^21}|{:^29}|".format(nomeProduto[x], precoProduto[x], qtdProduto[x]))     
    print("       -------------------------------------|---------------------|-----------------------------")

def indice():
    nomeBusca = input("Digite o nome do produto a ser buscado: ").upper()
    if nomeBusca in nomeProduto:
        produto = nomeProduto.index(nomeBusca)
        header()
        print("       |{:^36}|{:^21}|{:^29}|".format(nomeProduto[produto], precoProduto[produto], qtdProduto[produto]))     
        print("       -------------------------------------|---------------------|-----------------------------")

def deletando(um, dois):
    for x in um:
        x.pop(dois)

def deletar():
    nomeDeletar = input("Qual produto você deseja deletar do banco de dados? ").upper()
    if nomeDeletar in nomeProduto:
        produto = nomeProduto.index(nomeDeletar)
        while True:
            condicao = input("Você deseja realmente deletar {} do banco de dados S/N? ".format(nomeDeletar)).upper()
            if condicao == "S":
                deletando([nomeProduto, precoProduto, qtdProduto], produto)
                break
            elif condicao == "N":
                break
            else:
                erro()


while True:
    menu = input('''Menu
0-	Cadastrar Produto
1-	Preço do Produto
2-	Quantidade do Produto
3-	Relatório do Produto
4-	Busca por Nome
5-	Deletar Produto
6-	Finalizar Programa
Escolha: ''')
    if menu == "0":
        produto()
    elif menu == "1":
        preco()
    elif menu == "2":
        quantidade()
    elif menu == "3":
        relatorio()
    elif menu == "4":
        indice()
    elif menu == "5":
        deletar()
    elif menu == "6":
        joinha()
        break
    