from database.bdconnection import conectar

def criar_produto(nome_produto, valor):
    connection = conectar()
    cursor = connection.cursor()
    sql = 'INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)'
    values = (nome_produto, valor)
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()
    connection.close()
    print('Produto criado com sucesso!')

