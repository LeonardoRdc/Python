def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        menores = [i for i in arr[1:] if i <= pivot]
        maiores = [i for i in arr [1:] if i > pivot]
    
    return quicksort(menores) + [pivot] + quicksort(maiores)
    
print(quicksort([2,1,6,7,9,3,4]))

# Criar uma tabela de multiplicação com todos os elementos do array. Assim caso o seu array seja [2,3,7,8,10], primeiro multiplicará cada elemento por 2, depois 3, depois 7 e assim por diante.

def tabela(arr):
    for i in arr:
        line = []
        for j in arr:
            line.append(i*j)
        print(f'Multiplicação por {i}: ', line)   

tabela([2,3,7,8,10])