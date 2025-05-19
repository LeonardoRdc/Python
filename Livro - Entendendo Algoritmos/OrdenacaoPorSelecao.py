def buscaMenor(arr):
    menor_valor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor_valor:
            menor_valor = arr[i]
            menor_indice = i
    return menor_indice
    
def ordenacaoPorSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoPorSelecao([21, 15, 38, 17, 26, 2, 10, 98, 55, 40]))
