# prompt: Crie um arquivo CSV com 10 entradas conhecidas indicando:
# IMC, Obeso (true/false)

import csv
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = [
    [20, False],
    [25, False],
    [30, True],
    [35, True],
    [22, False],
    [28, False],
    [40, True],
    [27, False],
    [32, True],
    [24, False]
]

with open('imc_data.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['IMC', 'Obeso'])
  writer.writerows(data)

print("Arquivo 'imc_data.csv' criado com sucesso!")

# prompt: Crie um arquivo CSV com 10 entradas conhecidas indicando:
# IMC, Obeso (true/false)
# Treine uma máquina
# Pergunte a ela se um dado IMC (fora do range das entradas) é obeso ou não.



# Carregar os dados do arquivo CSV
data = []
with open('imc_data.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  next(reader)  # Ignorar o cabeçalho
  for row in reader:
    if len(row) >= 2 and row[0] and row[1]:  # Verifica se há pelo menos duas colunas e se não estão vazias
        try:
            peso = float(row[0].strip())

            # Se o valor da segunda coluna for 'True' ou 'False', converte para 1 ou 0
            if row[1].strip().lower() == "true":
                categoria = 1
            elif row[1].strip().lower() == "false":
                categoria = 0
            else:
                categoria = int(row[1].strip())  # Continua a conversão normal se for um número

            data.append([peso, categoria])

        except ValueError as e:
            print(f"Erro ao converter linha {row}: {e}")


# Separar os dados em features (IMC) e target (Obeso)
X = [row[0] for row in data]
y = [row[1] for row in data]

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar um modelo de regressão logística
model = LogisticRegression()
model.fit( [ [x] for x in X_train ], y_train)

# Perguntar ao modelo se um dado IMC é obeso ou não
novo_imc = 38  # IMC a ser classificado
previsao = model.predict([[novo_imc]])

if previsao[0] == 1:
  print(f"Um IMC de {novo_imc} indica que a pessoa é considerada obesa.")
else:
  print(f"Um IMC de {novo_imc} indica que a pessoa não é considerada obesa.")