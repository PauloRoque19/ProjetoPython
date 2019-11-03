import time#biblioteca o programa aguarda um certo tempo para execultar alguma operação.
import os
# listas de armazenamento de dados Temporarios
listaUsuario=["user","adm123","admin","admin","admin1","12345"]
listaDescricao=[]
listaReuniao=[]
listaConviteR=[]
listaAtas=[]




#Mostrar os dados cadastrados
def descricaoDados():
        print("------------------ DESCRIÇÃO DE DADOS ------------------")
        for i in listaDescricao:
            print("-- ", i)
            print("-----------------------------------------------")
        print("---FIM Usuario---")
        time.sleep(10)
        print('\n' * 30)
        v1 = input("Digite (sim)para voltar ao menu: ")
        if v1 == "sim":
            menu()



#Função cadastrar usuario
def cadastrarUsuario():
    contador=0
    qPessoa = int(input(">> você vai Cadastrar quantas Pessoas? "))
    print()
    time.sleep(1)
    print("------------------- INSERINDO DADOS ---------------")
    while contador < qPessoa:
        nomeusuario = input(">> Nome do Usuario: ")
        email = input(">> E-mail: ")
        cpf  = input(">> CPF: ")
        nomeLogin = input(">> Nome de Login: ")
        passwordusuario = input(">> Password:  ")
        contador += 1
        print()
        print()
        listaDescricao.append(nomeusuario)
        listaDescricao.append(email)
        listaDescricao.append(cpf)
        listaDescricao.append(nomeLogin)
        listaDescricao.append(passwordusuario)
        listaUsuario.append(nomeLogin)
        listaUsuario.append(passwordusuario)

        print(">> Cadastro Realizado com Sucesso!")
        print()
        time.sleep(1)
        print()
        resposta = input(">> Deseja Volta para o Menu de Opções? ")
        if resposta == "sim":
           menu()
        else:
           cadastrarUsuario()


#descrição da Reunião Cadastrada.
def descricaoReunião():
    #print('\n' * 100)
    print("------------------ DESCRIÇÃO DE REUNIÕES ------------------")
    for i in listaReuniao:
        print("-- ",i)
        print("-----------------------------------------------")
        #print('\n' * 100)
    time.sleep(30)
    v2 = input("Digite (sim) para voltar ao menu: ")
    if v2 == "sim":
        menu()



#Função cadastrar reuniões..
def cadastrarReunioes():
    contador=0
    print()
    time.sleep(1)
    qR = int(input("Quantas Reuniões deseja Cadastrar? "))
    print()
    time.sleep(1)
    print("------------------ COLETANDO DADOS -------------------")
    while contador < qR:
          tema = input(">> Tema da Reunião: ")
          data = input(">> Data: ")
          horario = input(">> Hora: ")
          qP      = input("Informe quantos Participantes? ")
          if tema != "" and data != "" and qP != "":
              listaReuniao.append(tema)
              listaReuniao.append(data)
              listaReuniao.append(horario)
              listaReuniao.append(qP)

              arq = open(tema,"a")
              arq.write(tema+"\n")
              arq.write(data+"\n")
              arq.write(horario+"\n")
              arq.write(qP+"\n")

              arq.close()

              print()
              time.sleep(1)
              print(">> Reunião Cadastrada com Sucesso!")
              print()
              time.sleep(1)
              resposta = input(">> Deseja Voltar Para o Menu Pricipal? ")
              print()
              time.sleep(1)
              if resposta == "sim":
                  menu()
              else:
                  cadastrarReunioes()




#Menu que quando chamado validando as opções que existem dentro dele
def menu():
    print('\n' * 30)
    for i in range(5):
        print("--------------------- MENU ------------------")
        print("-  1 PARA CADASTRAR USUARIO NO SISTEMA      -")
        print("-  2 PARA CADASTRAR REUNIÕES                -")
        print("-  3 PARA VER DESCRIÇÕES DE USUARIO         -")
        print("-  4 PARA VER DESCRIÇÃO DE REUNIÕES         -")
        print("-  5 PARA LOGAR NO SISTEMA                  -")
        print("-  6 PARA SAIR                              -")
        print("-  7 PARA ESCREVER ATAS                     -")
        print("-  8 PARA VISUALIZAR ATAS                     -")
        print("---------------------------------------------")
        print()
        time.sleep(1)
        opcao = int(input(">> Qual a sua Opção? "))
        if opcao == 1:
           print('\n' * 100)
           cadastrarUsuario()

        elif opcao == 2:
            print('\n' *100)
            cadastrarReunioes()
        elif opcao == 3:
            descricaoDados()

        elif opcao == 4:
             descricaoReunião()
             time.sleep(5)
             v2=input("Digite (sim) para voltar ao menu: ")
             if v2=="sim":
                 menu()
        elif opcao == 5:
             time.sleep(2)
             print('\n' * 100)
             login()
        elif opcao == 6:
             print("Até Mais!")
             exit()
        elif opcao == 7:
            print("-----ATAS DE REUNIÕES--------")
            criarAtasDeReuniões()
        elif opcao == 8:
            print("------VISUALIZAR ATAS DE REUNIÕES------")
            visualizarAtasDeReuniões()

        else:
            print()
            print("Opção Invalida!")
            print()
            time.sleep(1)
            resposta = input("Deseja Sair? ")
            if resposta == "sim":
                break
            else:
                continue

#Função faz com que o usuario seja validado de acordo com o que o usuario digitar.
def login():
    print()
    print()
    print("************************************** TELA DE lOGIN *****************************************")
    print("**************************************    E-MEET     *****************************************")
    login = input(">> Login: ")
    password = input(">> Password: ")
    print("**********************************************************************************************")
    if login == listaUsuario[0] and password == listaUsuario[1] or login == listaUsuario[2] and password == listaUsuario[3] or login == listaUsuario[4] and password == listaUsuario[5]:
        print()
        time.sleep(1)
        print("-------------- Bem-Vindo(a) ----------------")
        menu()
    elif login in listaUsuario:
         time.sleep(1)
         print("1ª Acesso..")
         print()
         time.sleep(1)
         menu()
#Vai Abrir  ou criar uma arquivo texto e pode-se escrevelo, se o arquivo existir os dados dele será excluido, CUIDADO~~
def criarAtasDeReuniões():
    v1=str(input("Escreva nome da reunião: "))
    arq = open(v1,"w")
    n=str(input("Digite algo: "))
    arq.write(n)
    arq.close()

    v2=input("Digite (sim) para voltar para o menu: ")
    print("...")
    time.sleep(2)
    if v2 == "sim":
        menu()
#Serve para Visualizar um Ata, você precisa saber so o nome da Ata ou("Reuniao")
def visualizarAtasDeReuniões():
    v1=str(input("Escreva nome da ata que queira visualizar: "))
    manipulador = open(v1,'r')
    print("\nMétodo read():\n")
    print(manipulador.read())
    manipulador.seek(0)
    v2=input("Digite (sim ) para voltar para menu: ")
    if v2 == "sim":
        menu()

"""def visualizarReuniões():
"""


def sistema():
    login()


sistema()








