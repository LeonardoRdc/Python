from main import conectar

def listar_produtos():
    connection = conectar()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM vendas')
    results = cursor.fetchall()

    print('Aqui está a listagem dos produtos:')

    for produto in results:
        id = produto[0]
        nome = produto [1]
        valor = produto [2]
        print(f'ID: {id} | Produto: {nome} | Valor: R${valor}')

    cursor.close()
    connection.close()

