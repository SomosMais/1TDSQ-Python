import oracledb
from datetime import date

# para usuario: cadastrar pedido, atualizar um pedido, cancelar pedido e ver historico

def get_conexao():
    return oracledb.connect(user="rm560485", password="fiap25", dsn="oracle.fiap.com.br/orcl")


def login_usuario():
    email = input("\nInsira o e-mail: ")

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("SELECT senha_usuario FROM GS_Usuario WHERE email_usuario = :1", (email,))
            captura = cur.fetchone()

    senha = input("\nInsira a senha: ")

    try:
        if senha == captura[0]:
            with get_conexao() as con:
                with con.cursor() as cur:
                    cur.execute("SELECT id_usuario FROM GS_Usuario WHERE email_usuario = :1", (email,))
                    id_usuario = cur.fetchone()[0]
            return id_usuario, menu(id_usuario)
        else:
            print("\nTentativa de Login inválida")
    except TypeError:
        print("\nTentativa de Login inválida")
    

def menu(id_usuario):
    
    while True:
        try:
            opcao = input("\nBem Vindo! \nSelecione a opção correspondente a sua necessidade \n\nOpção 1: Cadastrar um Pedido de Ajuda\nOpção 2: Atualizar um pedido\nOpção 3: Cancelar um pedido\nOpção 4: Ver histórico\nR: ")

            if opcao in ["1", "2", "3", "4"]:
                break
            else:
                raise ValueError
        
        except ValueError:
            input("Opção inválida, Pressione enter para continuar.")
    
    if opcao == "1":
        cadastrar_pedido(id_usuario)
    elif opcao == "2":
        atualizar_pedido(id_usuario)
    elif opcao == "3":
        cancelar_pedido(id_usuario)
    elif opcao == "4":
        historico(id_usuario)


def cadastrar_pedido(id_usuario):

    while True:
        try:
            descricao = input("\nDescreva o seu pedido: ")

            if descricao.isspace() == False:
                break
            elif descricao == "":
                raise ValueError
        
        except ValueError:
            input("Entrada inválida, Pressione enter para continuar.")
    
    while True:
        try:
            urgente = input("\nSeu pedido é urgente?\nR: ").upper()

            if urgente in ["S", "N"]:
                break
            else:
                raise ValueError
        
        except ValueError:
            input("Entrada inválida, responda com \"S\" ou \"N\". Pressione enter para continuar.")
    
    while True:
        try:
            tipo_pedido = int(input("\nEscolha o tipo que melhor define seu pedido\n1 - Resgate de Vítimas\n2 - Resgate de Animais\n3 - Ajuda Humanitária\n4 - Apoio em Enchentes\n5 - Apoio em Deslizamentos\n6 - Transporte de Vítimas\n7 - Busca e Salvamento\n8 - Atendimento Médico\n9 - Doação de Alimentos\n10 - Doação de Roupas\n11 - Solicitação de Abrigo\n12 - Acesso a Água Potável\n13 - Fornecimento de Energia Emergencial\nR: "))

            if tipo_pedido in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
                break
            else:
                raise ValueError
        except ValueError:
            input("Entrada inválida, escolha uma das opções apresentadas.")
    
    data_criacao = date.today()

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES (:1, :2, :3, :4, 1, 1, :5)", (descricao, data_criacao, urgente, id_usuario, tipo_pedido))
            con.commit()
    
    input("\nPedido recebido com sucesso!\nPressione Enter para continuar.")
    
    menu(id_usuario)


def atualizar_pedido(id_usuario):
    
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("SELECT u.nome_usuario, p.id_pedido FROM GS_Pedido_Ajuda p JOIN GS_Usuario u ON p.id_usuario = u.id_usuario LEFT JOIN GS_Status s ON p.id_status = s.id_status LEFT JOIN GS_Tipo_Pedido t ON p.id_tipo_pedido = t.id_tipo_pedido WHERE u.id_usuario = :1 ORDER BY p.data_criacao", (id_usuario,))
            captura_pedidos = cur.fetchall()
    
    lista_verificacao = []

    print("\nQual pedido você deseja alterar?")
    for tuplas in captura_pedidos:
        print(f"Pedido - ID: {tuplas[1]}")
        lista_verificacao.append(tuplas[1])
    
    print(lista_verificacao)

    


def cancelar_pedido(id_usuario):
    print("cancelar")


def historico(id_usuario):
    print("historico")


login_usuario()