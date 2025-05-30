from datetime import date
import oracledb




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


cancelar_pedido()