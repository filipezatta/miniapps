import re

with open(r'C:\Users\filip\OneDrive\Programação\GIT\miniapps\whatsapp text open\texts\Conversa do WhatsApp com Prospect Suelen Filhas 11 e 13 Anos 2023_02.txt') as arquivo:
    dados = arquivo.read()
    
    dados = dados.split('\n')
    print(dados[1], '\n')
    #cabeçalho = ['datahora', 'name' ,'msg']

    #cabeçalhodict = {k:[] for k in cabeçalho}
    lista_dados = list(map(lambda x: re.split('[" - "]+', x), dados))
    lista_dados.pop(0)
    print(lista_dados)
"""    
def associar(index):
    counter=0
    
    for i in range(1, len(lista_dados[index])):
        if i != lista_dados[index][0]:

            lista_dados[index][i] = int(lista_dados[index][i])

    for i in cabeçalho:
        if i == cabeçalho[-1]:
            cabeçalhodict[i] = round(sum(sorted(lista_dados[index][1:6], reverse=True)[0:3])/(len(cabeçalho)-4), 2)
            return(cabeçalhodict)
            
        cabeçalhodict[i] = lista_dados[index][counter]
        counter += 1
    return(cabeçalhodict)

def printar_todos_dados():
    for i in range(0, len(lista_dados)):
        current = associar(i)
        nome = current['nome']
        notas = (sorted(lista_dados[i][1:6], reverse=True))[0:3]
        media = round(sum((sorted(list(current.values())[1:6], reverse=True)[0:3]))/(len(cabeçalho)-4), 2)
        print(str('Nome: {nome} Notas: {notas} Média: {media}'.format(nome=nome, notas=notas, media=media)))
    
def printar_um_dado(i):
    current = associar(i)
    nome = current['nome']
    notas = (sorted(lista_dados[i][1:6], reverse=True))[0:3]
    media = round(sum((sorted(list(current.values())[1:6], reverse=True)[0:3]))/(len(cabeçalho)-4), 2)
    
    print(str('Nome: {nome} Notas: {notas} Média: {media}'.format(nome=nome, notas=notas, media=media)))
    
printar_todos_dados()
"""


input('a')