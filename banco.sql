-- 1-) Criação das tabelas --

CREATE TABLE GS_Endereco (
    id_endereco NUMBER(11) GENERATED AS IDENTITY PRIMARY KEY,
    logradouro VARCHAR2(120) NOT NULL,
    numero VARCHAR2(6),
    cep VARCHAR2(9),
    bairro VARCHAR2(100),
    cidade VARCHAR2(50),
    estado VARCHAR2(60)
);

CREATE TABLE GS_Usuario (
    id_usuario NUMBER(11) GENERATED AS IDENTITY PRIMARY KEY,
    nome_usuario VARCHAR2(100) NOT NULL,
    email_usuario VARCHAR2(255) NOT NULL UNIQUE,
    senha_usuario VARCHAR2(255) NOT NULL,
    cpf CHAR(11) NOT NULL UNIQUE,
    id_endereco NUMBER (11)
);

CREATE TABLE GS_Empresa (
    id_empresa NUMBER(11) GENERATED AS IDENTITY PRIMARY KEY,
    nome_empresa VARCHAR2(100),
    email_empresa VARCHAR2(255) UNIQUE,
    senha_empresa VARCHAR2(255),
    cnpj CHAR(14) UNIQUE,
    id_atuacao NUMBER(11),
    id_endereco NUMBER (11)
);

CREATE TABLE GS_Pedido_Ajuda (
    id_pedido NUMBER(11) GENERATED AS IDENTITY PRIMARY KEY,
    descricao VARCHAR2(255),
    data_criacao DATE,
    data_aceitacao DATE,
    urgente_pedido CHAR(1),
    id_usuario NUMBER(11),
    id_empresa NUMBER(11),
    id_status NUMBER(11),
    id_tipo_pedido NUMBER(11)
);

CREATE TABLE GS_Status (
    id_status NUMBER(11) GENERATED AS IDENTITY PRIMARY KEY,
    nome_status VARCHAR2(15)
);

CREATE TABLE GS_Area_Atuacao (
    id_atuacao NUMBER(11) GENERATED AS IDENTITY PRIMARY KEY,
    area_atuacao VARCHAR2(50)
);

CREATE TABLE GS_Tipo_Pedido(
    id_tipo_pedido NUMBER(11) GENERATED AS IDENTITY PRIMARY KEY,
    tipo_pedido VARCHAR2(50)
);


-- 2-) Adição das chaves estrangeiras --

ALTER TABLE GS_Usuario ADD CONSTRAINT FK_ID_ENDERECO_USUARIO FOREIGN KEY (id_endereco) REFERENCES GS_Endereco(id_endereco);
ALTER TABLE GS_Empresa ADD CONSTRAINT FK_ID_ENDERECO_EMPRESA FOREIGN KEY (id_endereco) REFERENCES GS_Endereco(id_endereco);

ALTER TABLE GS_Empresa ADD CONSTRAINT FK_ID_ATUACAO_EMPRESA FOREIGN KEY (id_atuacao) REFERENCES GS_Area_Atuacao(id_atuacao);

ALTER TABLE GS_Pedido_Ajuda ADD CONSTRAINT FK_ID_USUARIO_PEDIDO FOREIGN KEY (id_usuario) REFERENCES GS_Usuario(id_usuario);
ALTER TABLE GS_Pedido_Ajuda ADD CONSTRAINT FK_ID_EMPRESA_PEDIDO FOREIGN KEY (id_empresa) REFERENCES GS_Empresa(id_empresa);
ALTER TABLE GS_Pedido_Ajuda ADD CONSTRAINT FK_ID_STATUS_PEDIDO FOREIGN KEY (id_status) REFERENCES GS_Status(id_status);
ALTER TABLE GS_Pedido_Ajuda ADD CONSTRAINT FK_ID_TIPO_PEDIDO FOREIGN KEY (id_tipo_pedido) REFERENCES GS_Tipo_Pedido(id_tipo_pedido);


-- 3-) Inserts nas tabelas --

INSERT INTO GS_Status (nome_status) VALUES ('Pendente');
INSERT INTO GS_Status (nome_status) VALUES ('Em Andamento');
INSERT INTO GS_Status (nome_status) VALUES ('Concluído');


INSERT INTO GS_Area_Atuacao (area_atuacao) VALUES ('Enchentes');
INSERT INTO GS_Area_Atuacao (area_atuacao) VALUES ('Deslizamentos de Terra');
INSERT INTO GS_Area_Atuacao (area_atuacao) VALUES ('Terremotos');
INSERT INTO GS_Area_Atuacao (area_atuacao) VALUES ('Incêndios Florestais');
INSERT INTO GS_Area_Atuacao (area_atuacao) VALUES ('Secas');
INSERT INTO GS_Area_Atuacao (area_atuacao) VALUES ('Resposta a Emergências e Crises Humanitárias');


INSERT INTO GS_Tipo_Pedido (tipo_pedido) VALUES ('Resgate de Vítimas');
INSERT INTO GS_Tipo_Pedido (tipo_pedido) VALUES ('Resgate de Animais');
INSERT INTO GS_Tipo_Pedido (tipo_pedido) VALUES ('Ajuda Humanitária');
INSERT INTO GS_Tipo_Pedido (tipo_pedido) VALUES ('Apoio em Enchentes');
INSERT INTO GS_Tipo_Pedido (tipo_pedido) VALUES ('Apoio em Deslizamentos');
INSERT INTO GS_Tipo_Pedido (tipo_pedido) VALUES ('Transporte de Vítimas');
INSERT INTO GS_Tipo_Pedido (tipo_pedido) VALUES ('Busca e Salvamento');
INSERT INTO GS_Tipo_Pedido (tipo_pedido) VALUES ('Atendimento Médico');
INSERT INTO GS_Tipo_Pedido (tipo_pedido) VALUES ('Doação de Alimentos');
INSERT INTO GS_Tipo_Pedido (tipo_pedido) VALUES ('Doação de Roupas');
INSERT INTO GS_Tipo_Pedido (tipo_pedido) VALUES ('Solicitação de Abrigo');
INSERT INTO GS_Tipo_Pedido (tipo_pedido) VALUES ('Acesso a Água Potável');
INSERT INTO GS_Tipo_Pedido (tipo_pedido) VALUES ('Fornecimento de Energia Emergencial');


INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('N/A', '000', '00000-000', 'N/A', 'N/A', 'N/A');

INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua Alpes', '186', '12357-324', 'Jardim Governador Senna', 'Guarulhos', 'São Paulo');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Alameda Paulista', '4738', '16973-582', 'Parque Bonsucesso', 'Belo Horizonte', 'Minas Gerais');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Viela dos Palmares', '193', '56356-838', 'Puntiperi', 'Blumenau', 'Santa Catarina');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Avenida Caminho Dourado', '2689', '28645-031', 'Vila Campavari', 'Campos do Jordão', 'São Paulo');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua da Silva', '829', '58674-392', 'Copacabana', 'Rio de Janeiro', 'Rio de Janeiro');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua das Laranjeiras', '102', '74000-123', 'Setor Central', 'Goiânia', 'Goiás');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Travessa do Sol', '59', '69075-210', 'Adrianópolis', 'Manaus', 'Amazonas');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Avenida Atlântica', '4200', '22070-002', 'Copacabana', 'Rio de Janeiro', 'Rio de Janeiro');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua Boa Esperança', '315', '79021-400', 'Jardim dos Estados', 'Campo Grande', 'Mato Grosso do Sul');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua das Acácias', '12', '30150-930', 'Savassi', 'Belo Horizonte', 'Minas Gerais');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Avenida do Contorno', '9876', '30110-001', 'Funcionários', 'Belo Horizonte', 'Minas Gerais');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua Tiradentes', '234', '80020-010', 'Centro', 'Curitiba', 'Paraná');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua das Violetas', '87', '65065-654', 'Cohama', 'São Luís', 'Maranhão');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Alameda das Palmeiras', '445', '88040-000', 'Trindade', 'Florianópolis', 'Santa Catarina');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua Beija-Flor', '134', '72000-000', 'Taguatinga Sul', 'Brasília', 'Distrito Federal');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua Vitória Régia', '127', '72890-234', 'Jardim Tropical', 'Anápolis', 'Goiás');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Avenida das Gaivotas', '933', '49037-492', 'Atalaia', 'Aracaju', 'Sergipe');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Travessa Boa Vista', '211', '68903-491', 'Centro', 'Macapá', 'Amapá');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua 15 de Novembro', '400', '64000-900', 'Centro', 'Teresina', 'Piauí');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Avenida dos Expedicionários', '1877', '60411-381', 'Montese', 'Fortaleza', 'Ceará');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua das Andorinhas', '512', '78085-030', 'CPA II', 'Cuiabá', 'Mato Grosso');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Alameda das Magnólias', '389', '76829-852', 'Nova Floresta', 'Porto Velho', 'Rondônia');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua Padre Cícero', '95', '63010-010', 'Centro', 'Juazeiro do Norte', 'Ceará');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua São João', '376', '69301-708', 'Centro', 'Boa Vista', 'Roraima');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua das Acácias', '142', '77060-052', 'Plano Diretor Sul', 'Palmas', 'Tocantins');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua Lago Azul', '221', '59900-000', 'Zona Rural', 'Pau dos Ferros', 'Rio Grande do Norte');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Avenida Brasil Sul', '618', '65911-000', 'Vila Lobão', 'Imperatriz', 'Maranhão');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua Marechal Floriano', '789', '88010-100', 'Centro', 'Florianópolis', 'Santa Catarina');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Rua do Comércio', '333', '69900-970', 'Bosque', 'Rio Branco', 'Acre');
INSERT INTO GS_Endereco (logradouro, numero, cep, bairro, cidade, estado) VALUES ('Avenida Independência', '412', '69800-000', 'Centro', 'Eirunepé', 'Amazonas');


INSERT INTO GS_Empresa (nome_empresa, email_empresa, senha_empresa, cnpj, id_atuacao, id_endereco) VALUES ('N/A', 'N/A', 'N/A', '00000000000000', 1, 1);

INSERT INTO GS_Usuario (nome_usuario, email_usuario, senha_usuario, cpf, id_endereco) VALUES ('Cleyton Enrike de Oliveira', 'cleyton777@gmail.com', 'JQj124v6WIGp', '85610124042', 2);
INSERT INTO GS_Usuario (nome_usuario, email_usuario, senha_usuario, cpf, id_endereco) VALUES ('Pedro Henrique de Souza Sena', 'pedro189@hotmail.com', 'bV8q0e56N21v', '46575609058', 3);
INSERT INTO GS_Usuario (nome_usuario, email_usuario, senha_usuario, cpf, id_endereco) VALUES ('Matheus Henrique Nascimento de Freitas', 'math1983@gmail.com', 'mBm48inJe2XN', '75720983040', 4);
INSERT INTO GS_Usuario (nome_usuario, email_usuario, senha_usuario, cpf, id_endereco) VALUES ('Leticia Almeida dos Santos', 'lele1143@hotmail.com', 'RpA7AGe0b4Ff', '33618375026', 5);
INSERT INTO GS_Usuario (nome_usuario, email_usuario, senha_usuario, cpf, id_endereco) VALUES ('Samira Roberta da Silva', 'srsilva198@gmail.com', '7N2kjoe7T406', '78735593008', 6);
INSERT INTO GS_Usuario (nome_usuario, email_usuario, senha_usuario, cpf, id_endereco) VALUES ('Bruno César Martins Ferreira', 'bruno.martins@gmail.com', 'Xv6Pl90AkDe7', '12345678001', 7);
INSERT INTO GS_Usuario (nome_usuario, email_usuario, senha_usuario, cpf, id_endereco) VALUES ('Amanda Cristina Lopes Souza', 'amandacris@yahoo.com', 'Yt9Klp23WqZ5', '23456789012', 8);
INSERT INTO GS_Usuario (nome_usuario, email_usuario, senha_usuario, cpf, id_endereco) VALUES ('Lucas Gabriel Rocha Lima', 'lucasg.lima@hotmail.com', 'Za81LdN40vHt', '34567890123', 9);
INSERT INTO GS_Usuario (nome_usuario, email_usuario, senha_usuario, cpf, id_endereco) VALUES ('Juliana Marques dos Anjos', 'juliana.anjos@gmail.com', 'Kt8vLpR64Nz1', '45678901234', 10);
INSERT INTO GS_Usuario (nome_usuario, email_usuario, senha_usuario, cpf, id_endereco) VALUES ('Marcelo Henrique Batista', 'marcelobatista@outlook.com', 'W9uPqMxT28Ly', '56789012345', 11);
INSERT INTO GS_Usuario (nome_usuario, email_usuario, senha_usuario, cpf, id_endereco) VALUES ('Isabela Fernanda Costa Ribeiro', 'isabela.ribeiro@gmail.com', 'Lp90VhB7TxE2', '67890123456', 12);
INSERT INTO GS_Usuario (nome_usuario, email_usuario, senha_usuario, cpf, id_endereco) VALUES ('Carlos Eduardo Tavares', 'carlos.tavares@hotmail.com', 'FrU58Kop31Ls', '78901234567', 13);
INSERT INTO GS_Usuario (nome_usuario, email_usuario, senha_usuario, cpf, id_endereco) VALUES ('Beatriz Mendes de Azevedo', 'bia.azevedo@gmail.com', 'Tk3LvsPq18Nh', '89012345678', 14);
INSERT INTO GS_Usuario (nome_usuario, email_usuario, senha_usuario, cpf, id_endereco) VALUES ('Rafael Augusto Santana', 'rafael.santana@live.com', 'UzQ7nMb28Wl0', '90123456789', 15);
INSERT INTO GS_Usuario (nome_usuario, email_usuario, senha_usuario, cpf, id_endereco) VALUES ('Tatiane Oliveira da Luz', 'tatiane.luz@gmail.com', 'VcP93HyOqTw1', '01234567890', 16);


INSERT INTO GS_Empresa (nome_empresa, email_empresa, senha_empresa, cnpj, id_atuacao, id_endereco) VALUES ('Soluções Ágeis', 'solu153@gmail.com', 'r0865F3zNv4k', '10839482781264', 1, 17);
INSERT INTO GS_Empresa (nome_empresa, email_empresa, senha_empresa, cnpj, id_atuacao, id_endereco) VALUES ('Silva Soluções', 'silvasolucoes@hotmail.com', 'Fd5VO6Vkq3W0', '56616458000124', 2, 18);
INSERT INTO GS_Empresa (nome_empresa, email_empresa, senha_empresa, cnpj, id_atuacao, id_endereco) VALUES ('Almeida e Souza LTDA', 'alsilva@gmail.com', '913BHWUkSEfZ', '88504301000101', 3, 19);
INSERT INTO GS_Empresa (nome_empresa, email_empresa, senha_empresa, cnpj, id_atuacao, id_endereco) VALUES ('All Help SA', 'allhelp@gmail.com', 'p478trLe7gz6', '62326718000120', 4, 20);
INSERT INTO GS_Empresa (nome_empresa, email_empresa, senha_empresa, cnpj, id_atuacao, id_endereco) VALUES ('Life Suport', 'lifesuport@outlook.com', '1RgBOL0K5zP3', '22520827000169', 5, 21);
INSERT INTO GS_Empresa (nome_empresa, email_empresa, senha_empresa, cnpj, id_atuacao, id_endereco) VALUES ('TecnoNorte Ltda', 'tecnonorte@gmail.com', 'Hs8T9lpD3xVz', '10432896000195', 6, 22);
INSERT INTO GS_Empresa (nome_empresa, email_empresa, senha_empresa, cnpj, id_atuacao, id_endereco) VALUES ('Inova Solutions', 'contato@inovasol.com', 'Kp2VlE7gRm01', '50732806000140', 2, 23);
INSERT INTO GS_Empresa (nome_empresa, email_empresa, senha_empresa, cnpj, id_atuacao, id_endereco) VALUES ('Delta Tech', 'deltatech@empresa.com', 'T93WmLq8ZcVy', '32874610000103', 3, 24);
INSERT INTO GS_Empresa (nome_empresa, email_empresa, senha_empresa, cnpj, id_atuacao, id_endereco) VALUES ('Vision Systems', 'vision@vsystems.com', 'Nb5Lp92FqzvA', '97865023000129', 1, 25);
INSERT INTO GS_Empresa (nome_empresa, email_empresa, senha_empresa, cnpj, id_atuacao, id_endereco) VALUES ('Master Connect', 'master@connect.com', 'Aa6TfP9ZwL4e', '65324897000100', 5, 26);
INSERT INTO GS_Empresa (nome_empresa, email_empresa, senha_empresa, cnpj, id_atuacao, id_endereco) VALUES ('Futura Inteligência', 'futuraint@empresa.com', 'Zx3Ld7MfT90q', '20198543000117', 4, 27);
INSERT INTO GS_Empresa (nome_empresa, email_empresa, senha_empresa, cnpj, id_atuacao, id_endereco) VALUES ('Global Ware', 'gware@corporate.com', 'Qp1NvbZ46xYt', '81294716000171', 6, 28);
INSERT INTO GS_Empresa (nome_empresa, email_empresa, senha_empresa, cnpj, id_atuacao, id_endereco) VALUES ('SmartWay', 'suporte@smartway.com', 'Mn9Bk4rLdQz3', '72518493000180', 1, 29);
INSERT INTO GS_Empresa (nome_empresa, email_empresa, senha_empresa, cnpj, id_atuacao, id_endereco) VALUES ('NetHelp Brasil', 'nethelp@empresa.com.br', 'Wx0Kz9LpH72o', '41208569000133', 2, 30);
INSERT INTO GS_Empresa (nome_empresa, email_empresa, senha_empresa, cnpj, id_atuacao, id_endereco) VALUES ('Alpha Solutions', 'alpha@solucoes.com', 'Gj2WqlR7Dz5n', '34860185000156', 3, 31);


INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, data_aceitacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES ('Precisamos de ajuda para resgatar as vitimas', '01-01-25', '02-01-25', 'S', 1, 1, 1, 1);
INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, data_aceitacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES ('Precisamos de ajuda para resgatar os animais', '03-01-25', '04-01-25', 'S', 2, 2, 2, 2);
INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, data_aceitacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES ('Precisamos de Ajuda Huminatária', '05-01-25', '06-01-25', 'S', 3, 3, 3, 3);
INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, data_aceitacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES ('Precisamos de ajuda com as enchentes', '07-01-25', '08-01-25', 'S', 4, 4, 1, 4);
INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, data_aceitacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES ('Precisamos de ajuda com os deslizamentos', '09-01-25', '10-01-25', 'S', 5, 5, 2, 5);
INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, data_aceitacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES ('Solicitamos apoio com mantimentos', '11-01-25', '12-01-25', 'S', 6, 6, 3, 6);
INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, data_aceitacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES ('Ajuda médica necessária em abrigo', '13-01-25', '14-01-25', 'N', 7, 7, 1, 7);
INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, data_aceitacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES ('Precisamos de roupas e cobertores', '15-01-25', '16-01-25', 'S', 8, 8, 2, 8);
INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, data_aceitacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES ('Apoio com transporte de vítimas', '17-01-25', '18-01-25', 'N', 9, 9, 3, 9);
INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, data_aceitacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES ('Precisamos de abrigo temporário', '19-01-25', '20-01-25', 'S', 10, 10, 1, 10);
INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, data_aceitacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES ('Ajuda com alimentos não perecíveis', '21-01-25', '22-01-25', 'N', 11, 11, 2, 11);
INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, data_aceitacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES ('Auxílio com medicamentos', '23-01-25', '24-01-25', 'S', 12, 12, 3, 12);
INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, data_aceitacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES ('Precisamos de voluntários para triagem', '25-01-25', '26-01-25', 'S', 13, 13, 1, 13);
INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, data_aceitacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES ('Precisamos de lanternas e pilhas', '27-01-25', '28-01-25', 'N', 14, 14, 2, 1);
INSERT INTO GS_Pedido_Ajuda (descricao, data_criacao, data_aceitacao, urgente_pedido, id_usuario, id_empresa, id_status, id_tipo_pedido) VALUES ('Ajuda com transporte de doações', '29-01-25', '30-01-25', 'S', 15, 15, 3, 2);


commit;


/*

--select * from GS_Area_Atuacao ORDER BY id_atuacao;
--select * from GS_Empresa ORDER BY id_empresa;
--select * from GS_Endereco ORDER BY id_endereco;
--select * from GS_Pedido_Ajuda ORDER BY id_pedido;
--select * from GS_Status ORDER BY id_status;
--select * from GS_Tipo_Pedido ORDER BY id_tipo_pedido;
--select * from GS_Usuario ORDER BY id_usuario;



-- Total de pedidos por empresa com área de atuação --
SELECT 
    e.nome_empresa,
    a.area_atuacao,
    COUNT(p.id_pedido) AS total_pedidos
FROM 
    GS_Empresa e
JOIN 
    GS_Area_Atuacao a ON e.id_atuacao = a.id_atuacao
LEFT JOIN 
    GS_Pedido_Ajuda p ON e.id_empresa = p.id_empresa
GROUP BY 
    e.nome_empresa, a.area_atuacao
HAVING 
    COUNT(p.id_pedido) > 0
ORDER BY 
    total_pedidos DESC;


-- Média de pedidos urgentes por status --
SELECT 
    s.nome_status,
    AVG(CASE WHEN p.urgente_pedido = 'S' THEN 1 ELSE 0 END) AS media_urgentes
FROM 
    GS_Status s
JOIN 
    GS_Pedido_Ajuda p ON s.id_status = p.id_status
GROUP BY 
    s.nome_status
ORDER BY 
    media_urgentes DESC;
    

-- Pedidos urgentes com detalhes --
SELECT 
    p.id_pedido,
    p.descricao,
    p.data_criacao,
    u.nome_usuario,
    s.nome_status
FROM 
    GS_Pedido_Ajuda p
JOIN 
    GS_Usuario u ON p.id_usuario = u.id_usuario
JOIN 
    GS_Status s ON p.id_status = s.id_status
WHERE 
    p.urgente_pedido = 'S'
ORDER BY 
    p.data_criacao DESC;




-- Empresas que já aceitaram pedidos com dados de endereço --
SELECT 
    e.nome_empresa,
    en.logradouro || ', ' || en.numero AS endereco
FROM 
    GS_Empresa e
JOIN 
    GS_Endereco en ON e.id_endereco = en.id_endereco
WHERE 
    EXISTS (
        SELECT 1 
        FROM GS_Pedido_Ajuda p 
        WHERE p.id_empresa = e.id_empresa 
        AND p.data_aceitacao IS NOT NULL
    );


-- Quantidade de pedidos por tipo, apenas os tipos com mais de 2 pedidos --
SELECT 
    t.tipo_pedido,
    COUNT(p.id_pedido) AS qtd_pedidos
FROM 
    GS_Tipo_Pedido t
LEFT JOIN 
    GS_Pedido_Ajuda p ON t.id_tipo_pedido = p.id_tipo_pedido
GROUP BY 
    t.tipo_pedido
HAVING
    COUNT(p.id_pedido) > 1
ORDER BY 
    qtd_pedidos DESC;


-- Pedidos com nome e id do usuário
SELECT 
    u.nome_usuario,
    u.id_usuario,
    p.id_pedido,
    p.descricao,
    p.data_criacao,
    p.data_aceitacao,
    p.urgente_pedido,
    s.nome_status,
    t.tipo_pedido
FROM 
    GS_Pedido_Ajuda p
JOIN 
    GS_Usuario u ON p.id_usuario = u.id_usuario
LEFT JOIN 
    GS_Status s ON p.id_status = s.id_status
LEFT JOIN 
    GS_Tipo_Pedido t ON p.id_tipo_pedido = t.id_tipo_pedido
ORDER BY 
    p.data_criacao;

    

-- Empresas com endereço completo --
SELECT 
    e.id_empresa,
    e.nome_empresa,
    e.email_empresa,
    e.senha_empresa,
    e.cnpj,
    e.id_atuacao,
    
    -- Dados do endereço
    ender.id_endereco,
    ender.logradouro,
    ender.numero,
    ender.cep,
    ender.bairro,
    ender.cidade,
    ender.estado

FROM GS_Empresa e
JOIN GS_Endereco ender ON e.id_endereco = ender.id_endereco;


-- Usuários com endereço completo --
SELECT
    u.id_usuario,
    u.nome_usuario,
    u.email_usuario,
    u.senha_usuario,
    u.cpf,
    u.id_endereco,
    ender.logradouro,
    ender.numero,
    ender.cep,
    ender.bairro,
    ender.cidade,
    ender.estado
FROM
         gs_usuario u
    JOIN gs_endereco ender ON u.id_endereco = ender.id_endereco;

-- numero de empresas --
SELECT COUNT(*) FROM GS_EMPRESA

-- numero de pedidos concluidos --
SELECT COUNT(*) FROM GS_Pedido_Ajuda WHERE id_status = 3


-- Pedidos com Nome e Endereço do usuario --
SELECT
    p.id_pedido,
    p.descricao,
    p.data_criacao,
    p.urgente_pedido,
    p.id_tipo_pedido,
    u.nome_usuario,
    e.logradouro,
    e.numero,
    e.bairro,
    e.cidade, 
    e.estado,
    e.cep 
FROM GS_Pedido_Ajuda p
JOIN GS_Usuario u ON p.id_usuario = u.id_usuario
LEFT JOIN GS_Endereco e ON u.id_endereco = e.id_endereco
ORDER BY id_pedido;


-- Pedidos com endereço completo do usuario com base no id da empresa que aceitou --
SELECT
    p.id_pedido,
    p.descricao,
    p.data_criacao,
    p.data_aceitacao,
    p.urgente_pedido,
    u.nome_usuario,
    e.logradouro,
    e.numero,
    e.bairro, 
    e.cidade,
    e.estado,
    e.cep,
    p.id_tipo_pedido
FROM
    GS_Pedido_Ajuda p
JOIN
    GS_Usuario u ON p.id_usuario = u.id_usuario
LEFT JOIN
    GS_Endereco e ON u.id_endereco = e.id_endereco
WHERE
    p.id_empresa = 2


-- Nome do usuário e id de seus pedidos --
SELECT
    u.nome_usuario,
    p.id_pedido
FROM
         gs_pedido_ajuda p
    JOIN gs_usuario     u ON p.id_usuario = u.id_usuario
    LEFT JOIN gs_status      s ON p.id_status = s.id_status
    LEFT JOIN gs_tipo_pedido t ON p.id_tipo_pedido = t.id_tipo_pedido
WHERE
    u.id_usuario = 1
ORDER BY
    p.data_criacao;
    

-- Excluir --
BEGIN
  FOR t IN (
    SELECT table_name 
    FROM user_tables 
    WHERE table_name LIKE 'GS_%'
  ) LOOP
    EXECUTE IMMEDIATE 'DROP TABLE "' || t.table_name || '" CASCADE CONSTRAINTS';
  END LOOP;
END;
*/