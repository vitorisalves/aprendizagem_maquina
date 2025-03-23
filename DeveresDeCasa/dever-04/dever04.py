# prompt: Crie um arquivo chamado
# minhas_frutas.txt e grave nele os
# nomes das frutas do conjunto, com
# uma quantidade aleatória entre 0 e
# 100 para cada registro.

import random

lista_frutas = ["maçã", "banana", "laranja", "uva", "maçã", "melão", "mamão", "banana"]

with open('minhas_frutas.txt', 'w') as f:
    for fruta in lista_frutas:  # Não remover duplicatas antes de escrever
        quantidade = random.randint(0, 100)
        f.write(f"{fruta}: {quantidade}\n")


# prompt: Abra o arquivo, leia e exiba seu
# conteúdo no console através de
# um Data Frame com os nomes
# das colunas: Fruta e quantidade
# Atente-se que há frutas repetidas
# no arquivo e as suas quantidades
# devem ser somadas.

import pandas as pd

frutas_dict = {}

with open('minhas_frutas.txt', 'r') as f:
    for line in f:
        fruta, quantidade = line.strip().split(': ')
        quantidade = int(quantidade)
        
        if fruta in frutas_dict:
            frutas_dict[fruta] += quantidade  # Soma a quantidade se a fruta já existir
        else:
            frutas_dict[fruta] = quantidade  # Adiciona nova fruta

# Criar DataFrame
df = pd.DataFrame(frutas_dict.items(), columns=['Fruta', 'Quantidade'])

# Exibir DataFrame
print(df)
