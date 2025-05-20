import mysql.connector
from create_products import criar_produto
from list_products import listar_produtos
from update_products import atualizar_produtos
from delete_products import deletar_produtos

def conectar():
    return mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '42866824mar.',
    database = 'bdfirst',
)

criar_produto('Coca-Cola', 6)
listar_produtos()
atualizar_produtos('Coca-Cola', 7, 2)
deletar_produtos(['Coca-Cola'])



















