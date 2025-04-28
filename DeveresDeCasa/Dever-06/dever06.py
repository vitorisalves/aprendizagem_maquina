# Importando as bibliotecas necessárias
from sklearn.datasets import load_iris  # Para carregar o dataset Iris
from sklearn.neighbors import KNeighborsClassifier  # Modelo KNN para classificação

# Carregando o dataset Iris
iris = load_iris()

# X contém as características das flores (comprimento e largura da sépala e pétala)
X = iris.data

# y contém os rótulos (espécies das flores: setosa, versicolor, virginica)
y = iris.target

# Nomes das espécies para traduzir a previsão em nome legível
nomes_especies = iris.target_names

# Criando e treinando o modelo KNN (K-Nearest Neighbors)
modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X, y)  # Treina o modelo com os dados de entrada (X) e saída (y)

# Exibindo as informações do dataset (para entender o que está sendo usado)
print("Características (X):")
print(X)

print("\nRótulos (y):")
print(y)

print("\nNomes das espécies:")
print(nomes_especies)

# Função para garantir que a entrada seja um número float
def obter_entrada_float(pergunta):
    while True:
        try:
            # Solicita a entrada do usuário e tenta convertê-la para float
            return float(input(pergunta))
        except ValueError:
            # Caso o usuário digite algo que não seja um número float
            print("Entrada inválida! Por favor, digite um número válido (ex: 5.1, 3.4, 1.2, etc.).")

# Entrada do usuário para as características da flor
print("\nDigite as características da flor:")

# Pedindo os dados ao usuário e tratando entradas inválidas
comprimento_sepala = obter_entrada_float("Comprimento da sépala (cm): ")
largura_sepala = obter_entrada_float("Largura da sépala (cm): ")
comprimento_petala = obter_entrada_float("Comprimento da pétala (cm): ")
largura_petala = obter_entrada_float("Largura da pétala (cm): ")

# Organiza os dados inseridos pelo usuário em uma lista (formato esperado pelo modelo)
nova_flor = [[comprimento_sepala, largura_sepala, comprimento_petala, largura_petala]]

# Realiza a previsão com base nas entradas do usuário
predicao = modelo.predict(nova_flor)

# Exibe o resultado da previsão
print(f"\nA flor prevista é: {nomes_especies[predicao[0]]}")
