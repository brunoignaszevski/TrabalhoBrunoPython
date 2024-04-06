import psycopg2

conn = psycopg2.connect(
    dbname="loja_de_eletronicos",
    user="postgres",
    password="postgres",
    host="localhost"
)

cur = conn.cursor()

'''
CREATE TABLE produtos (
	produtoID INT,
	nome_do_produto VARCHAR(255),
	quantidade INT
);
'''

dados_a_inserir = [
    (1, "Notebook Dell", 5),
    (2, "Celular Xiaomi", 10),
    (3, "TV LG", 10),
    (4, "Monitor Samsung", 8),
    (5, "Mouse Logitech", 15),
    (6, "Teclado Microsoft", 12),
    (7, "Impressora HP", 6),
    (8, "Fone de Ouvido Sony", 20),
    (9, "Tablet Samsung", 10),
    (10, "Smartwatch Apple", 8),
    (11, "Câmera Canon", 12),
    (12, "Roteador TP-Link", 15)
]

sql = "INSERT INTO produtos (produtoid, nome_do_produto, quantidade) VALUES (%s, %s, %s)"

try:
    for dado in dados_a_inserir:
        cur.execute(sql, dado)
        conn.commit()
        print("Dados inseridos com sucesso!")
except (Exception, psycopg2.DatabaseError) as error:
    print("Erro ao inserir dados:", error)
    conn.rollback()

sql_consulta = "SELECT * FROM produtos"

try:
    cur.execute(sql_consulta)
    
    resultados = cur.fetchall()
    
    for linha in resultados:
        print(linha)

except (Exception, psycopg2.DatabaseError) as error:
    print("Erro ao consultar a tabela:", error)

finally:

    cur.close()
    conn.close()