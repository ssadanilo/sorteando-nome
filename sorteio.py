# Importando biblioteca random
import random

# Criando lista
nomes = []

# Criando Loop while para inserir quantos nomes desejar
while True:
    nome = input('Digite um nome (ou "sair" para encerrar): ')
    if nome.lower() == 'sair': # Uso do lower aqui para minimizar apenas a palavra sair
        break # Parando o loop
    nomes.append(nome) # Adicionando nomes a lista


sorteado = random.choice(nomes) # Sorteando um nome atraves da função random
nomes.remove(sorteado) # Removendo o sorteado da lista
print(f'O sorteado é: {sorteado}') # Printando apenas o sorteado
print(f'Lista de participantes não sorteados: {nomes}') # Printando a lista dos não sorteados
