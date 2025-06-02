from flask import Flask, jsonify, request
from datetime import date
import oracledb

# app = Flask(__name__)

def get_conexao():
    return oracledb.connect(user="rm560485", password="fiap25", dsn="oracle.fiap.com.br/orcl")


def mostrar_ongs():
    
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("select * from GS_Empresa ORDER BY id_empresa")
            captura_banco = cur.fetchall()
    
    lista_empresas = []

    for empresas in captura_banco:
        id_empresa = empresas[0]
        nome_empresa = empresas[1]
        email_empresa = empresas[2]
        senha_empresa = empresas[3]
        cnpj = empresas[4]
        id_atuacao = empresas[5]
        id_endereco = empresas[6]

        lista_empresas.append({"id": id_empresa, "Nome": nome_empresa, "Email": email_empresa, "CNPJ": cnpj, "id_atuacao": id_atuacao, "id_endereco": id_endereco})

    for i in lista_empresas:
        print(i)


def status_pedido():
    id_pedido = 2

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(f"SELECT p.id_pedido, p.descricao, s.nome_status FROM GS_Pedido_Ajuda p JOIN GS_Status s ON p.id_status = s.id_status WHERE id_pedido = {id_pedido}")
            captura = cur.fetchone()

    pedido = {"id": captura[0], "Descricao": captura[1], "Status": captura[2]}
    
    print(pedido)


def historico_pedido():
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(f"SELECT u.nome_usuario, u.id_usuario, p.id_pedido, p.descricao, p.data_criacao, p.data_aceitacao, p.urgente_pedido, s.nome_status, t.tipo_pedido FROM GS_Pedido_Ajuda p JOIN GS_Usuario u ON p.id_usuario = u.id_usuario LEFT JOIN GS_Status s ON p.id_status = s.id_status LEFT JOIN GS_Tipo_Pedido t ON p.id_tipo_pedido = t.id_tipo_pedido WHERE u.id_usuario = 1 ORDER BY p.data_criacao")
            captura = cur.fetchall()
    
    lista_pedido = []

    for pedidos in captura:
        nome_usuario = pedidos[0]
        id_usuario = pedidos[1]
        id_pedido = pedidos[2]
        descricao = pedidos[3]
        data_criacao = pedidos[4].strftime('%d-%m-%y') # data_criacao
        data_aceitacao = pedidos[5].strftime('%d-%m-%y') # data_aceitacao
        urgente = pedidos[6]
        status = pedidos[7]
        tipo_pedido = pedidos[8]

        lista_pedido.append({"Nome": nome_usuario, "id_usuario": id_usuario, "id_pedido": id_pedido, "descricao": descricao, "data_criacao": data_criacao, "data_aceitacao": data_aceitacao, "urgente": urgente, "status": status, "tipo pedido": tipo_pedido})
    
    print(lista_pedido)


def cancelar_pedido():
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("DELETE FROM GS_Pedido_Ajuda WHERE id_pedido = 5")
            con.commit()


def atualizar_pedido():
    # daria para mudar, descrição, urgência e tipo
    # método patch

    insercao = request

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("")



# @app.route("/historico/cliente/<email>", methods=["GET"])
def historico_pedido(email):

    # mudar de id_usuario para email_usuario

    data_aceitacao = None

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(f"SELECT u.nome_usuario, u.id_usuario, p.id_pedido, p.descricao, p.data_criacao, p.data_aceitacao, p.urgente_pedido, s.nome_status, t.tipo_pedido FROM GS_Pedido_Ajuda p JOIN GS_Usuario u ON p.id_usuario = u.id_usuario LEFT JOIN GS_Status s ON p.id_status = s.id_status LEFT JOIN GS_Tipo_Pedido t ON p.id_tipo_pedido = t.id_tipo_pedido WHERE u.email_usuario = '{email}' ORDER BY p.data_criacao")
            captura = cur.fetchall()
    
    lista_pedido = []

    for pedidos in captura:
        nome_usuario = pedidos[0]
        id_usuario = pedidos[1]
        id_pedido = pedidos[2]
        descricao = pedidos[3]
        data_criacao = pedidos[4].strftime('%d-%m-%y') # data_criacao
            
        if data_aceitacao:
            data_aceitacao = pedidos[5].strftime('%d-%m-%y') # data_aceitacao
        
        urgente = pedidos[6]
        status = pedidos[7]
        tipo_pedido = pedidos[8]

        lista_pedido.append({"Nome": nome_usuario, "id_usuario": id_usuario, "id_pedido": id_pedido, "descricao": descricao, "data_criacao": data_criacao, "data_aceitacao": data_aceitacao, "urgente": urgente, "status": status, "tipo pedido": tipo_pedido})

    if len(lista_pedido) >= 1:
        return (jsonify(lista_pedido), 200)
    else:
       info = {"msg": f"Não existe usuário com o email {email}", "status": 406}
       return (info, 406) 


# @app.route("/numero_ongs", methods=["GET"])
def numero_ongs():

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("SELECT count(*) FROM gs_empresa")
            contagem = cur.fetchone()[0]
    
    print(contagem)



def funcaodetestedasilva(email_empresa):

    insercao = {"urgencia": "S"}

    if insercao.get("urgencia"):
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute(f"SELECT p.id_pedido, p.descricao, p.data_criacao, p.urgente_pedido, p.id_tipo_pedido, u.nome_usuario, e.logradouro, e.numero, e.bairro, e.cidade, e.estado, e.cep FROM GS_Pedido_Ajuda p JOIN GS_Usuario u ON p.id_usuario = u.id_usuario LEFT JOIN GS_Endereco e ON u.id_endereco = e.id_endereco WHERE urgente_pedido = '{insercao["urgencia"]}' ORDER BY id_pedido")
                captura = cur.fetchall()
        
        lista_pedidos = []

        for i in captura:
            id_pedido = i[0]
            descricao = i[1]
            data_criacao = i[2].strftime('%d-%m-%y')
            urgencia = i[3]
            id_tipo_pedido = i[4]
            nome_usuario = i[5]
            logradouro = i[6]
            numero = i[7]
            bairro = i[8]
            cidade = i[9]
            estado = i[10]
            cep = i[11]

            lista_pedidos.append({"id_pedido": id_pedido, "descricao": descricao, "data criacao": data_criacao, "urgencia": urgencia, "id tipo pedido": id_tipo_pedido, "nome do usuario": nome_usuario, "endereco do usuario": [logradouro, numero, bairro, cidade, estado, cep]})
        
    for i in lista_pedidos:
        print(i)



    
    



# @app.route("/aceitar_pedido/<email_empresa>/<int:id_pedido>", methods=["GET"])
def aceitar_pedido(email_empresa, id_pedido: int):

    data_atual = date.today()

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("SELECT id_pedido FROM GS_Pedido_Ajuda")
            captura_pedidos = cur.fetchall()
            cur.execute(f"SELECT id_empresa FROM GS_Empresa WHERE email_empresa = {email_empresa}")
            captura_id_empresa = cur.fetchone()
    
    lista_id_pedidos = []
    
    for tuplas in captura_pedidos:
        lista_id_pedidos.append(tuplas[0])

    if id_pedido in lista_id_pedidos:
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("UPDATE GS_Pedido_Ajuda SET id_empresa = :1, data_aceitacao = :2, id_status = 2 WHERE id_pedido = :3", (id_empresa, data_atual, id_pedido))
                con.commit()
        
        info = {"msg": "Pedido aceito com sucesso!", "Status": 200}
        return (info, 200)
    else:
        info = {"msg": "id de empresa ou id de pedido inexistente", "Status": 406}
        return (info, 406)


funcaodetestedasilva("solu153@gmail.com")



# app.run(debug=True)