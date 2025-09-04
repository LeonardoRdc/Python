lista_telefonica = {}

lista_telefonica['Jenny'] = 8675309
lista_telefonica['Emergency'] = 911

print(lista_telefonica['Jenny'])


votou = {}

def verifica_eleitor(nome):
    if votou.get(nome):
        print(f'{nome}: Mete teu pézinho!')
    else:
        votou[nome] = True
        print(f'{nome}: Apto a votar!')


verifica_eleitor('Renanzola')
verifica_eleitor('Arthurzola')
verifica_eleitor('Arthurzola')