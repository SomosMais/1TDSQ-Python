# Endpoints

| Método | Endpoint                                          | Descrição                                                                |
| ------ | ------------------------------------------------- | ------------------------------------------------------------------------ |
| POST   | `/cadastro_pedido_ajuda`                          | Cadastra um novo pedido de ajuda com base nas informações fornecidas.    |
| GET    | `/numero_ongs`                                    | Retorna o número total de ONGs (empresas) cadastradas.                   |
| GET    | `/numero_pedidos_concluidos`                      | Retorna a quantidade de pedidos que estão com status "concluído" (id 3). |
| GET    | `/mostrar_usuarios`                               | Lista todos os usuários com seus respectivos dados e endereços.          |
| GET    | `/mostrar_ongs`                                   | Lista todas as ONGs com seus respectivos dados e endereços.              |
| GET    | `/status_pedido/<int:id>`                         | Retorna a descrição e o status atual de um pedido de ajuda específico.   |
| GET    | `/historico/cliente/<email>`                      | Mostra o histórico de pedidos de ajuda de um usuário (pelo e-mail).      |
| GET    | `/cancelar_pedido/<int:id>`                       | Exclui um pedido de ajuda com base no `id`.                              |
| PATCH  | `/atualizar_pedido/<int:id>`                      | Atualiza a descrição, urgência ou tipo de um pedido de ajuda.            |
| GET    | `/aceitar_pedido/<email_empresa>/<int:id_pedido>` | Aceita um pedido de ajuda pendente, o ligando a uma empresa.             |
| POST   | `/visualizar_pedidos`                             | Mostra os pedidos pendentes com filtro de urgência ou tipo de pedido     |

---

# Link projeto finalizado (Vercel)
- https://1-tdsq-front-comum-t5ae.vercel.app/
- https://1-tdsq-front-empresa-ckak.vercel.app/

---

# Funcionalidades (Usuário)
- Cadastrar um pedido de ajuda.
- Visualizar todas as ONGs disponíveis.
- Visualizar todo o histórico com dados de cada pedido.
- Cancelar um pedido já feito no aplicativo.
- Atualizar a descrição, tipo e/ou urgência de um pedido.
- Visualizar número de ongs cadastradas.
- Visualizar número de pedidos já concluídos em todo aplicativo.

# Funcionalidades (Empresa)
- Visualizar pedidos pendentes com base num filtro.
- Aceitar pedidos pendentes no aplicativo.
- Visualizar todo o histórico com dados de cada pedido.
- Visualizar número de ongs cadastradas.
- Visualizar número de pedidos já concluídos em todo aplicativo.
 
---

# Endpoints úteis (PYTHON RENDER)

* A API hopedada no RENDER

* numero_ongs
* GET https://onetdsq-python.onrender.com/numero_ongs

* numero_pedido_concluidos
* GET https://onetdsq-python.onrender.com/numero_pedidos_concluidos

* mostrar_ongs
* GET https://onetdsq-python.onrender.com/mostrar_ongs

* status_pedido
* GET https://onetdsq-python.onrender.com/status_pedido/<int:id>

* historico_cliente
* GET https://onetdsq-python.onrender.com/historico/cliente/<email>

* canelar_pedido
* GET https://onetdsq-python.onrender.com/cancelar_pedido/<int:id>

* atualizar_pedido
* PATCH https://onetdsq-python.onrender.com/atualizar_pedido/<int:id>

---

# Integrantes
| NOME                                   | RM     | TURMA |
| -------------------------------------- | ------ | ----- |
| Cleyton Enrike de Oliveira             | 560485 | 1TDSQ |
| Pedro Henrique de Souza Sena           | 561178 | 1TDSQ |
| Matheus Henrique Nascimento de Freitas | 560442 | 1TDSQ |

---

# Link do vídeo explicativo
- https://youtu.be/QTpB6ZbxPRE