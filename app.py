# 👤 USUÁRIO (Afetado)
# •    ✅ Cadastro de pedido de ajuda
# •    ✅ Mostrando quantas ONGs
# •    ✅ Visualização de status do pedido (Pendente, Em andamento, Concluído).
# •    ✅ Histórico de pedidos anteriores
# •    ✅ Cancelar ou atualizar pedido
# API de todos os clientes
# número de ongs
# número de pedidos concluídos


# •    ✅ Gráficos sobre enchentes



# 🏥 ONG (ou admin)
# •    ✅ Aceitar pedido
# •    ✅ Visualizar todos os pedidos abertos (com filtros: tipo, urgência, local)

# •    ✅ Gráficos e estatísticas por tipo de pedido, localização e status



from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import date
import oracledb
import os

app = Flask(__name__)
CORS(app)


def get_conexao():
    return oracledb.connect(user="rm560485", password="fiap25", dsn="oracle.fiap.com.br/orcl")


@app.route("/cadastro_pedido_ajuda", methods=["POST"])
def cadastro_ajuda():

    insercao = request.get_json()
    
    if not insercao.get("descricao") or not insercao.get("urgencia") or not insercao.get("email_usuario") or not insercao.get("tipo"):
        info = {"msg": "Não foi encontrada uma das informações necessárias", "status": 406}
        return (info, 406)
    
    data_atual = date.today()
    descricao = insercao["descricao"]
    urgente_pedido = insercao["urgencia"]
    tipo = insercao["tipo"]
    usuario = insercao["email_usuario"]

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("SELECT id_usuario FROM gs_usuario WHERE email_usuario = :1", (usuario,))
            captura_id_usuario = cur.fetchone()
    
    id_usuario = captura_id_usuario[0]

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES (:1, :2, :3, :4, 1, 1, :5)", (descricao, data_atual, urgente_pedido, id_usuario, tipo))
            con.commit()
    
    info = {"msg": "Pedido recebido", "status": 201}
    return jsonify(info), 201


@app.route("/numero_ongs", methods=["GET"])
def numero_ongs():

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("SELECT count(*) FROM gs_empresa")
            contagem = cur.fetchone()[0]
    
    dicionario = {"Numero de empresas": contagem}

    return (jsonify(dicionario), 200)


@app.route("/numero_pedidos_concluidos", methods=["GET"])
def numero_pedidos_concluidos():

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM GS_Pedido_Ajuda WHERE id_status = 3")
            contagem = cur.fetchone()[0]
    
    dicionario = {"Numero de pedidos concluidos": contagem}

    return (jsonify(dicionario), 200)    


@app.route("/mostrar_usuarios", methods=["GET"])
def mostrar_usuarios():

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("SELECT u.id_usuario, u.nome_usuario, u.email_usuario, u.senha_usuario, u.cpf, u.id_endereco, ender.logradouro, ender.numero, ender.cep, ender.bairro, ender.cidade, ender.estado FROM GS_Usuario u JOIN GS_Endereco ender ON u.id_endereco = ender.id_endereco")

            captura_banco = cur.fetchall()

    lista_usuarios = []

    for usuarios in captura_banco:
        id_usuario = usuarios[0]
        nome_usuario = usuarios[1]
        email_usuario = usuarios[2]
        senha_usuario = usuarios[3]
        cpf = usuarios[4]
        id_endereco = usuarios[5]
        logradouro = usuarios[6]
        numero = usuarios[7]
        cep = usuarios[8]
        bairro = usuarios[9]
        cidade = usuarios[10]
        estado = usuarios[11]

        lista_usuarios.append({"id": id_usuario, "Nome": nome_usuario, "Email": email_usuario, "CPF": cpf, "id_endereco": id_endereco, "endereco": [logradouro, numero, cep, bairro, cidade, estado]})
    
    return(jsonify(lista_usuarios), 200)


@app.route("/mostrar_ongs", methods=["GET"])
def mostrar_ongs():

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("SELECT e.id_empresa, e.nome_empresa, e.email_empresa, e.senha_empresa, e.cnpj, e.id_atuacao, ender.id_endereco, ender.logradouro, ender.numero, ender.cep, ender.bairro, ender.cidade, ender.estado FROM GS_Empresa e JOIN GS_Endereco ender ON e.id_endereco = ender.id_endereco")

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
        logradouro = empresas[7]
        numero = empresas[8]
        cep = empresas[9]
        bairro = empresas[10]
        cidade = empresas[11]
        estado = empresas[12]

        lista_empresas.append({"id": id_empresa, "Nome": nome_empresa, "Email": email_empresa, "CNPJ": cnpj, "id_atuacao": id_atuacao, "id_endereco": id_endereco, "endereco": [logradouro, numero, cep, bairro, cidade, estado]})
    
    return (jsonify(lista_empresas), 200)


@app.route("/status_pedido/<int:id>", methods=["GET"])
def status_pedido(id: int):

    try: 
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("SELECT p.id_pedido, p.descricao, s.nome_status FROM GS_Pedido_Ajuda p JOIN GS_Status s ON p.id_status = s.id_status WHERE id_pedido = :1", (id,))
                captura = cur.fetchone()

        pedido = {"id": captura[0], "Descricao": captura[1], "Status": captura[2]}

        return (jsonify(pedido), 200)
    
    except TypeError:
        info = {"msg": f"Não existe pedido com o id {id}", "status": 406}
        return (info, 406)


@app.route("/historico/empresa/<email>", methods=["GET"])
def historico_pedido_empresa(email):

    try:
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("SELECT id_empresa FROM GS_Empresa WHERE email_empresa = :1", (email,))
                id_empresa = cur.fetchone()[0]
        
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("SELECT p.id_pedido, p.descricao, p.data_criacao, p.data_aceitacao, p.urgente_pedido, u.nome_usuario, e.logradouro, e.numero, e.bairro, e.cidade, e.estado, e.cep, p.id_tipo_pedido FROM GS_Pedido_Ajuda p JOIN GS_Usuario u ON p.id_usuario = u.id_usuario LEFT JOIN GS_Endereco e ON u.id_endereco = e.id_endereco WHERE p.id_empresa = :1", (id_empresa,))
                captura_banco = cur.fetchall()
        
        lista_pedido = []

    
        for pedidos in captura_banco:
            id_pedido = pedidos[0]
            descricao = pedidos[1]
            data_criacao = pedidos[2].strftime('%d-%m-%y')
            data_aceitacao = pedidos[3].strftime('%d-%m-%y')
            urgente = pedidos[4]
            nome_usuario = pedidos[5]
            logradouro = pedidos[6]
            numero = pedidos[7]
            bairro = pedidos[8]
            cidade = pedidos[9]
            estado = pedidos[10]
            cep = pedidos[11]
            tipo_pedido = pedidos[12]

            lista_pedido.append({"id_pedido": id_pedido, "descricao": descricao, "data criacao": data_criacao, "data aceitacao": data_aceitacao, "urgente": urgente, "nome usuario": nome_usuario, "endereco usuario": [logradouro, numero, bairro, cidade, estado, cep], "tipo pedido": tipo_pedido})

        if len(lista_pedido) >= 1:
            return (jsonify(lista_pedido), 200)
        else:
            info = {"msg": "Nenhum pedido foi encontrado", "Status": 200}
            return (info, 200)
    
    except TypeError:
        info = {"msg": f"Nenhuma empresa com o email {email}", "Status": 406}
        return (info, 406)


@app.route("/historico/cliente/<email>", methods=["GET"])
def historico_pedido_usuario(email):

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("SELECT u.nome_usuario, u.id_usuario, p.id_pedido, p.descricao, p.data_criacao, p.data_aceitacao, p.urgente_pedido, s.nome_status, t.tipo_pedido FROM GS_Pedido_Ajuda p JOIN GS_Usuario u ON p.id_usuario = u.id_usuario LEFT JOIN GS_Status s ON p.id_status = s.id_status LEFT JOIN GS_Tipo_Pedido t ON p.id_tipo_pedido = t.id_tipo_pedido WHERE u.email_usuario = :1 ORDER BY p.data_criacao", (email,))
            captura = cur.fetchall()
    
    if not captura:
        info = {"msg": f"Não existe usuário com o email {email}", "status": 406}
        return (info, 406)

    lista_pedido = []

    for pedidos in captura:
        nome_usuario = pedidos[0]
        id_usuario = pedidos[1]
        id_pedido = pedidos[2]
        descricao = pedidos[3]
        data_criacao = pedidos[4].strftime('%d-%m-%y') # data_criacao
                
        if pedidos[5]:
            data_aceitacao = pedidos[5].strftime('%d-%m-%y')
        else:
            data_aceitacao = None
            
        urgente = pedidos[6]
        status = pedidos[7]
        tipo_pedido = pedidos[8]

        lista_pedido.append({"Nome": nome_usuario, "id_usuario": id_usuario, "id_pedido": id_pedido, "descricao": descricao, "data_criacao": data_criacao, "data_aceitacao": data_aceitacao, "urgente": urgente, "status": status, "tipo pedido": tipo_pedido})

    if len(lista_pedido) >= 1:
        return (jsonify(lista_pedido), 200)
    else:
        info = {"msg": "Nenhum pedido feito por esse usuário", "status": 200}
        return (info, 200)

    
@app.route("/cancelar_pedido/<int:id>", methods=["GET"])
def cancelar_pedido(id: int):

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("DELETE FROM GS_Pedido_Ajuda WHERE id_pedido = :1", (id,))
            linhas_afetadas = cur.rowcount
            con.commit()
        
    if linhas_afetadas != 0:
        info = {"msg": "Pedido cancelado com sucesso!", "status": 200}
        return (info, 200)
    else:
        info = {"msg": f"Não existe pedido com o id {id}", "status": 406}
        return (info, 406)


@app.route("/atualizar_pedido/<int:id>", methods=["PATCH"])
def atualizar_pedido(id: int):

    insercao = request.get_json()

    if insercao.get("descricao"):
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("UPDATE GS_Pedido_Ajuda SET descricao = :1 WHERE id_pedido = :2", (insercao["descricao"], id))
                linhas_afetadas = cur.rowcount
                con.commit()
        
    if insercao.get("urgencia"):
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("UPDATE GS_Pedido_Ajuda SET urgente_pedido = :1 WHERE id_pedido = :2", (insercao["urgencia"], id))
                linhas_afetadas = cur.rowcount
                con.commit()
        
    if insercao.get("tipo"):
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("UPDATE GS_Pedido_Ajuda SET id_tipo_pedido = :1 WHERE id_pedido = :2", (insercao["tipo"], id))
                linhas_afetadas = cur.rowcount
                con.commit()
        
    if not insercao.get("descricao") and not insercao.get("urgencia") and not insercao.get("tipo"):
        info = {"msg": "não foi encontrada nenhuma informação necessária", "status": 406}
        return (info, 406)

    if linhas_afetadas != 0:
        info = {"msg": "Pedido atualizado com sucesso!", "status": 200}
        return (info, 200)
    else:
        info = {"msg": f"Não existe pedido com o id {id}", "status": 406}
        return (info, 406)    


@app.route("/aceitar_pedido/<email_empresa>/<int:id_pedido>", methods=["GET"])
def aceitar_pedido(email_empresa, id_pedido: int):

    data_atual = date.today()

    with get_conexao() as con:
        with con.cursor() as cur:

            cur.execute("SELECT id_empresa FROM GS_Empresa WHERE email_empresa = :1", (email_empresa,))
            captura_id_empresa = cur.fetchone()
            
            cur.execute("SELECT id_pedido FROM GS_Pedido_Ajuda")
            captura_pedidos = cur.fetchall()
    
    if captura_id_empresa == None:
        info = {"msg": "Empresa inexistente", "Status": 406}
        return (info, 406)
    
    lista_id_pedidos = []

    for tuplas in captura_pedidos:
        lista_id_pedidos.append(tuplas[0])

    if id_pedido in lista_id_pedidos:
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("UPDATE GS_Pedido_Ajuda SET id_empresa = :1, data_aceitacao = :2, id_status = 2 WHERE id_pedido = :3", (captura_id_empresa[0], data_atual, id_pedido))
                con.commit()
        
        info = {"msg": "Pedido aceito com sucesso!", "Status": 200}
        return (info, 200)
    else:
        info = {"msg": "Pedido inexistente", "Status": 406}
        return (info, 406)


@app.route("/visualizar_pedidos", methods=["POST"])
def visualizar_pedidos():
    # falta retornar só os pedidos pendentes
    insercao = request.get_json()

    if not insercao:
        info = {"msg": "Nenhum filtro aplicado", "Status": 406}
        return (info, 406)

    if len(insercao) > 1 or len(insercao) < 1:
        info = {"msg": "Mais ou menos de um filtro aplicado", "Status": 406}
        return (info, 406)
    
    if insercao.get("urgencia"):
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("SELECT p.id_pedido, p.descricao, p.data_criacao, p.urgente_pedido, p.id_tipo_pedido, u.nome_usuario, e.logradouro, e.numero, e.bairro, e.cidade, e.estado, e.cep FROM GS_Pedido_Ajuda p JOIN GS_Usuario u ON p.id_usuario = u.id_usuario LEFT JOIN GS_Endereco e ON u.id_endereco = e.id_endereco WHERE urgente_pedido = :1 ORDER BY id_pedido", (insercao["urgencia"],))
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
        
        return(jsonify(lista_pedidos), 200)
    

    elif insercao.get("tipo"):
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute("SELECT p.id_pedido, p.descricao, p.data_criacao, p.urgente_pedido, p.id_tipo_pedido, u.nome_usuario, e.logradouro, e.numero, e.bairro, e.cidade, e.estado, e.cep FROM GS_Pedido_Ajuda p JOIN GS_Usuario u ON p.id_usuario = u.id_usuario LEFT JOIN GS_Endereco e ON u.id_endereco = e.id_endereco WHERE id_tipo_pedido = :1 ORDER BY id_pedido", (insercao["tipo"],))
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
        
        return(jsonify(lista_pedidos), 200)
    
    elif not insercao.get("urgencia") and not insercao.get("tipo"):
        info = {"msg": "Não foi encontrado nenhum filtro", "Status": 406}
        return (info, 406)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)