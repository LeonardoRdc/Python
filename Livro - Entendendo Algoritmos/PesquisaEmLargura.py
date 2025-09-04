from collections import deque

grafo = {
    'voce': ['Alice', 'Bob', 'Claire'],
    'Alice': ['Peggy'],
    'Bob': ['Anuj', 'Peggy'],
    'Claire': ['Thom', 'Jonny'],
    'Peggy': [],
    'Anuj': [],
    'Thom': [],
    'Jonny': []
}

def pessoa_e_vendedor(pessoa):
    return pessoa.endswith('m')

def pesquisa(nome):
    fila = deque()
    fila += grafo[nome]
    verificadas = []

    while fila:
        pessoa = fila.popleft()
        if pessoa not in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + ' é um vendedor de manga!')
                return True
            else:
                fila += grafo[pessoa]
                verificadas.append(pessoa)
    
    return False

pesquisa('voce')
