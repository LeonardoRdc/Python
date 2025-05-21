from database.bdconnection import conectar

def atualizar_produtos(novo_nome, novo_valor, id):
    connection = conectar()
    cursor = connection.cursor()
    sql = 'UPDATE vendas SET nome_produto = %s, valor = %s WHERE idvendas = %s'
    values = (novo_nome, novo_valor, id)
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()
    connection.close()
    print('Produto atualizado com sucesso!')

