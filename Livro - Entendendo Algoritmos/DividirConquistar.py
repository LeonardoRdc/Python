
# Escreva o código para a função soma, vista anteriormente
# Pegue uma Lista, Se a Lista estiver vazia, retorne zero. Caso contrário, a soma total será o primeiro número da Lista + a soma restante da Lista

def soma(arr):
   if not arr:
      return 0
   else:
        somatotal = arr[0] + soma(arr[1:])
        return somatotal
   
print(soma([1,2,3]))
   
# Escreva uma função recursiva que conte o número de itens em uma lista

def contagem(arr):
    
    if not arr:
        return 0
    else:
        contador = 1 + contagem(arr[1:])
        return contador
    
print(contagem([2,5,7,9,10,11,15,18,20]))

# Encontre o valor mais alto em uma lista

def procura_valor(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        maior_valor = procura_valor(arr[1:])
        return arr[0] if arr[0] > maior_valor else maior_valor
    

print(procura_valor([1,10,15,25]))