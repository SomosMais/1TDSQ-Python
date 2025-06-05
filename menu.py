import oracledb
import json as js
from datetime import date


def get_conexao():
    try: 
        return oracledb.connect(user="rm560485", password="fiap25", dsn="oracle.fiap.com.br/orcl")
    
    except oracledb.DatabaseError as e:
        erro, = e.args
        print(f"Erro ao conectar com o banco de dados: {erro.code} - {erro.message}")
        return None


def login_usuario():
    email = input("\nInsira o e-mail: ")

    try: 
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
    
    except oracledb.DatabaseError as e:
        erro, = e.args
        print(f"Erro ao conectar com o banco de dados: {erro.code} - {erro.message}")
        return None
    

def menu(id_usuario):
    
    while True:
        try:
            opcao = input("\nBem Vindo! \nSelecione a opção correspondente a sua necessidade \n\nOpção 1: Cadastrar um Pedido de Ajuda\nOpção 2: Atualizar um pedido\nOpção 3: Cancelar um pedido\nOpção 4: Ver histórico\nOpção 5: Encerrar\nR: ")

            if opcao in ["1", "2", "3", "4", "5"]:
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
    elif opcao == "5":
        exit()


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

    try: 
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES (:1, :2, :3, :4, 1, 1, :5)", (descricao, data_criacao, urgente, id_usuario, tipo_pedido))
                con.commit()
        
        input("\nPedido recebido com sucesso!\nPressione Enter para continuar.")
    
    except oracledb.DatabaseError as e:
        erro, = e.args
        print(f"Erro ao conectar com o banco de dados: {erro.code} - {erro.message}")
        return None
    
    menu(id_usuario)


def atualizar_pedido(id_usuario):
    
    try:
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("SELECT u.nome_usuario, p.id_pedido FROM GS_Pedido_Ajuda p JOIN GS_Usuario u ON p.id_usuario = u.id_usuario LEFT JOIN GS_Status s ON p.id_status = s.id_status LEFT JOIN GS_Tipo_Pedido t ON p.id_tipo_pedido = t.id_tipo_pedido WHERE u.id_usuario = :1 ORDER BY p.id_pedido", (id_usuario,))
                captura_pedidos = cur.fetchall()
    
    except oracledb.DatabaseError as e:
        erro, = e.args
        print(f"Erro ao conectar com o banco de dados: {erro.code} - {erro.message}")
        return None
    
    lista_verificacao = []

    print("\nQual pedido você deseja alterar?")
    for tuplas in captura_pedidos:
        print(f"Pedido - ID: {tuplas[1]}")
        lista_verificacao.append(tuplas[1])
    
    while True:
        try: 
            opcao = int(input("R: "))

            if opcao in lista_verificacao:
                break
            else:
                raise ValueError

        except ValueError:
            input("Opção inválida. Pressione enter para continuar.")

    while True:
        try:
            nova_descricao = input("\nNova descrição do pedido: ")

            if nova_descricao.isspace() == False:
                break
            elif nova_descricao == "":
                raise ValueError
        
        except ValueError:
            input("Entrada inválida, Pressione enter para continuar.")

    while True:
        try:
            novo_urgente = input("\nSeu pedido é urgente?\nR: ").upper()

            if novo_urgente in ["S", "N"]:
                break
            else:
                raise ValueError
        
        except ValueError:
            input("Entrada inválida, responda com \"S\" ou \"N\". Pressione enter para continuar.")
    
    while True:
        try:
            novo_tipo_pedido = int(input("\nEscolha o tipo que melhor define seu pedido\n1 - Resgate de Vítimas\n2 - Resgate de Animais\n3 - Ajuda Humanitária\n4 - Apoio em Enchentes\n5 - Apoio em Deslizamentos\n6 - Transporte de Vítimas\n7 - Busca e Salvamento\n8 - Atendimento Médico\n9 - Doação de Alimentos\n10 - Doação de Roupas\n11 - Solicitação de Abrigo\n12 - Acesso a Água Potável\n13 - Fornecimento de Energia Emergencial\nR: "))

            if novo_tipo_pedido in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
                break
            else:
                raise ValueError
        except ValueError:
            input("Entrada inválida, escolha uma das opções apresentadas.")
    
    try: 
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("UPDATE GS_Pedido_Ajuda SET descricao = :1, urgente_pedido = :2, id_tipo_pedido = :3 WHERE id_pedido = :4", (nova_descricao, novo_urgente, novo_tipo_pedido, opcao))
                con.commit()
    
    except oracledb.DatabaseError as e:
        erro, = e.args
        print(f"Erro ao conectar com o banco de dados: {erro.code} - {erro.message}")
        return None
    
    input(f"\nO Pedido com id: {opcao} foi atualizado com sucesso!\nPressione enter para continuar.")

    menu(id_usuario)


def cancelar_pedido(id_usuario):

    try: 
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("SELECT u.nome_usuario, p.id_pedido FROM GS_Pedido_Ajuda p JOIN GS_Usuario u ON p.id_usuario = u.id_usuario LEFT JOIN GS_Status s ON p.id_status = s.id_status LEFT JOIN GS_Tipo_Pedido t ON p.id_tipo_pedido = t.id_tipo_pedido WHERE u.id_usuario = :1 ORDER BY p.id_pedido", (id_usuario,))
                captura_pedidos = cur.fetchall()
    
    except oracledb.DatabaseError as e:
        erro, = e.args
        print(f"Erro ao conectar com o banco de dados: {erro.code} - {erro.message}")
        return None
    
    lista_verificacao = []

    print("\nQual pedido você deseja cancelar?")
    for tuplas in captura_pedidos:
        print(f"Pedido - ID: {tuplas[1]}")
        lista_verificacao.append(tuplas[1])
    
    while True:
        try: 
            opcao = int(input("R: "))

            if opcao in lista_verificacao:
                break
            else:
                raise ValueError

        except ValueError:
            input("Opção inválida. Pressione enter para continuar.")

    try: 
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("DELETE FROM GS_Pedido_Ajuda WHERE id_pedido = :1", (opcao,))
                con.commit()
    
    except oracledb.DatabaseError as e:
        erro, = e.args
        print(f"Erro ao conectar com o banco de dados: {erro.code} - {erro.message}")
        return None
    
    input(f"\nO Pedido com id: {opcao} foi cancelado com sucesso!\nPressione enter para continuar.")

    menu(id_usuario)


def historico(id_usuario):

    try: 
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("SELECT p.id_pedido, p.descricao, p.data_criacao, p.data_aceitacao, p.urgente_pedido, s.nome_status, t.tipo_pedido FROM GS_Pedido_Ajuda p JOIN GS_Usuario u ON p.id_usuario = u.id_usuario LEFT JOIN GS_Status s ON p.id_status = s.id_status LEFT JOIN GS_Tipo_Pedido t ON p.id_tipo_pedido = t.id_tipo_pedido WHERE u.id_usuario = :1 ORDER BY p.id_pedido", (id_usuario,))
                captura = cur.fetchall()
    
    except oracledb.DatabaseError as e:
        erro, = e.args
        print(f"Erro ao conectar com o banco de dados: {erro.code} - {erro.message}")
        return None
    
    lista_pedidos = []

    for pedidos in captura:
        print("\n")
        print(f"ID: {pedidos[0]}")
        print(f"Descrição: {pedidos[1]}")
        print(f"Data de Criação: {pedidos[2].strftime('%d-%m-%y')}")

        if pedidos[3] == None:
            print(f"Data de Aceitação: {pedidos[3]}")
        else:
            print(f"Data de Aceitação: {pedidos[3].strftime('%d-%m-%y')}")

        print(f"Urgência: {pedidos[4]}")
        print(f"Status: {pedidos[5]}")
        print(f"Tipo de Pedido: {pedidos[6]}")

        lista_pedidos.append({
        "ID": pedidos[0],
        "Descrição": pedidos[1],
        "Data de Criação": pedidos[2].strftime('%d-%m-%Y') if pedidos[2] else "",
        "Data de Aceitação": pedidos[3].strftime('%d-%m-%Y') if pedidos[3] else "",
        "Urgência": pedidos[4],
        "Status": pedidos[5],
        "Tipo de Pedido": pedidos[6]
        })


    while True:
        try:
            pergunta_impressao = input("\nVocê deseja imprimir esta resposta?\n1 - Sim\n2 - Não\nR:")

            if pergunta_impressao in ["1", "2"]:
                break
            else:
                raise ValueError
            
        except ValueError:
            input("\nOpção inválida!\nPressione enter para continuar.")

    if pergunta_impressao == "1":
        with open("historico.json", mode="w", encoding="utf-8") as arquivo:
            js.dump(lista_pedidos, arquivo, indent=4, ensure_ascii=False)

        print("\nSeu histórico foi impresso!")

    input("\nPressione enter para voltar ao menu.")

    menu(id_usuario)
    

login_usuario()