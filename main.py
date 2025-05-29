# 👤 USUÁRIO (Afetado)
# •    ✅ Cadastro de pedido de ajuda
# •    ✅ Mostrando quantas ONGs
# •    ✅ Visualização de status do pedido (Pendente, Em andamento, Concluído).
# •    ✅ Histórico de pedidos anteriores
# •    ✅ Cancelar ou atualizar pedido

# •    ✅ Gráficos sobre enchentes



# 🏥 ONG (ou admin)
# •    ✅ Aceitar pedido
# •    ✅ Visualizar todos os pedidos abertos (com filtros: tipo, urgência, local)

# •    ✅ Gráficos e estatísticas por tipo de pedido, localização e status



from flask import Flask, jsonify, request
from datetime import date
import oracledb

app = Flask(__name__)


def get_conexao():
    return oracledb.connect(user="rm560485", password="fiap25", dsn="oracle.fiap.com.br/orcl")


@app.route("/cadastro_pedido_ajuda", methods=["POST"])
def cadastro_ajuda():

    insercao = request.get_json()
    
    if not insercao.get("descricao") or not insercao.get("urgente") or not insercao.get("id_usuario") or not insercao.get("id_empresa") or not insercao.get("id_status") or not insercao.get("tipo_pedido"):
        info = {"msg": "Não foi encontrada uma das informações necessárias", "status": 406}
        return (info, 406)
    
    data_atual = date.today()
    descricao = insercao["descricao"]
    urgente_pedido = insercao["urgente"]
    tipo_pedido = insercao["tipo_pedido"]
    usuario = insercao["id_usuario"]

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(f"INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES (:1, :2, :3, :4, 1, 1, :5)", (descricao, data_atual, urgente_pedido, usuario, tipo_pedido))
            con.commit()
    
    info = {"msg": "Pedido recebido", "status": 201}
    return jsonify(info), 201


    # Exemplo de dicionário

    # {
    #     "descricao": "[descricao]"
    #     "urgente": "[S ou N]"
    #     "id_usuario": [id do usuario logado]
    #     "id_empresa": [1, nenhuma empresa aceitou ainda]
    #     "id_status": [1, sempre vai entrar como pendente]
    #     "tipo_pedido": [de 1 a 13]
    # }


@app.route("/mostrar_ongs", methods=["GET"])
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
    
    return (jsonify(lista_empresas), 200)


@app.route("/status_pedido/<int:id>", methods=["GET"])
def status_pedido(id: int):

    try: 
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute(f"SELECT p.id_pedido, p.descricao, s.nome_status FROM GS_Pedido_Ajuda p JOIN GS_Status s ON p.id_status = s.id_status WHERE id_pedido = {id}")
                captura = cur.fetchone()

        pedido = {"id": captura[0], "Descricao": captura[1], "Status": captura[2]}

        return (jsonify(pedido), 200)
    
    except TypeError:
        info = {"msg": f"Não existe pedido com o id {id}", "status": 406}
        return (info, 406)


@app.route("/historico/cliente/<int:id>", methods=["GET"])
def historico_pedido(id: int):

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(f"SELECT u.nome_usuario, u.id_usuario, p.id_pedido, p.descricao, p.data_criacao, p.data_aceitacao, p.urgente_pedido, s.nome_status, t.tipo_pedido FROM GS_Pedido_Ajuda p JOIN GS_Usuario u ON p.id_usuario = u.id_usuario LEFT JOIN GS_Status s ON p.id_status = s.id_status LEFT JOIN GS_Tipo_Pedido t ON p.id_tipo_pedido = t.id_tipo_pedido WHERE u.id_usuario = {id} ORDER BY p.data_criacao")
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

    if len(lista_pedido) >= 1:
        return (jsonify(lista_pedido), 200)
    else:
       info = {"msg": f"Não existe usuário com o id {id}", "status": 406}
       return (info, 406) 
    



app.run(debug=True)