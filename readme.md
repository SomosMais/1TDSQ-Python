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