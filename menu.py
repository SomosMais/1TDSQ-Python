import oracledb

# para usuario: cadastrar pedido, atualizar um pedido, cancelar pedido e ver historico

def get_conexao():
    return oracledb.connect(user="rm560485", password="fiap25", dsn="oracle.fiap.com.br/orcl")


def inicio():
    while True:

        try:
            Empresa_ou_usuario = input("\nVocê deseja fazer login como empresa ou como usuário\n1 - Empresa\n2 - Usuário\nR: ")

            if Empresa_ou_usuario not in [1,2]:
                break
            else:
                raise ValueError
            
        except ValueError:
            input("Opção inválida, Pressione enter para continuar.")
    
    if Empresa_ou_usuario == 1:
        login_empresa()
    elif Empresa_ou_usuario == 2:
        login_usuario()


def login_usuario():
    email = input("\nInsira o e-mail: ")

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("SELECT senha_usuario FROM GS_Usuario WHERE email_usuario = :1", (email,))
            captura = cur.fetchone()

    senha = input("\nInsira a senha: ")

    if senha == captura[0]:
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("SELECT id_usuario FROM GS_Usuario WHERE email_usuario = :1", (email,))
                id_usuario = cur.fetchone()[0]
        return id_usuario
    else:
        print("login inválido")
    

def menu(id_usuario):
    
    while True:
        try:
            opcao = input("\nBem Vindo! \nSelecione a opção correspondente a sua necessidade \n\nOpção 1: Cadastrar um Pedido de Ajuda\nOpção 2: Atualizar um pedido\nOpção 3: Cancelar um pedido\nOpção 4: Ver histórico")

            if opcao in [1, 2, 3, 4]:
                break
            else:
                raise ValueError
        
        except ValueError:
            input("Opção inválida, Pressione enter para continuar.")
    
    if opcao == 1:
        cadastrar_pedido()
    elif opcao == 2:
        atualizar_pedido()
    elif opcao == 3:
        cancelar_pedido()
    elif opcao == 4:
        historico()



def cadastrar_pedido():
    pass


def atualizar_pedido():
    pass


def cancelar_pedido():
    pass


def historico():
    pass