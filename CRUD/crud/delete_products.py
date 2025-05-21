from database.bdconnection import conectar

def deletar_produtos(nome_produto):
    connection = conectar()
    cursor = connection.cursor()
    sql = 'DELETE FROM vendas WHERE nome_produto = %s'
    values = (nome_produto)
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()
    connection.close()
    print('Produto deletado com sucesso!')

