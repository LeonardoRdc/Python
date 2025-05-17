def pesquisa_binaria (lista, item):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        palpite = lista[meio]

        if palpite == item:
            return meio
        elif palpite > item:
            fim = meio - 1
        else:
            inicio = meio + 1
    return None

minha_lista = [1, 2, 5, 4, 9, 10, 11, 15, 25, 18]
print(pesquisa_binaria(minha_lista, 5))
print(pesquisa_binaria(minha_lista, 25))
