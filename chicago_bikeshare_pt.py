# coding: utf-8

# Começando com os imports
import csv
from collections import Counter, defaultdict
from typing import Tuple, List, Any, Dict

import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for l in data_list[:20]:
    print(l)

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for l in data_list[:20]:
    print(l[6])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")


# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index, as_type=None):
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice,
    # e dar append para uma lista
    for line in data:
        value = as_type(line[index]) if as_type else line[index]
        column_list.append(value)
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[
    1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = len([x for x in column_to_list(data_list, 6) if x == 'Male'])
female = len([x for x in column_to_list(data_list, 6) if x == 'Female'])

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos,
# 15 Femininos)
def count_gender(data_list):
    male = 0
    female = 0
    for line in data_list:
        if line[6] == 'Male':
            male += 1
        elif line[6] == 'Female':
            female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[
    1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_l):
    answer = ""
    genders = (gender.lower() for gender in column_to_list(data_l, 6))
    c = Counter(genders)
    gender_first, gfc = c.most_common(2)[0]
    gender_second, gsc = c.most_common(2)[1]
    if gender_first == "":
        answer = "Igual"
    elif gender_first == "male":
        answer = "Masculino"
    elif gender_first == "female":
        answer = "Feminino"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")


def count_user_types(data_l):
    subscriber = 0
    customer = 0
    for line in data_l:
        if line[-3] == 'Subscriber':
            subscriber += 1
        elif line[-3] == 'Customer':
            customer += 1
    return customer, subscriber


user_types_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
quantity = count_user_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos de usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipos de Usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque existem lacunas nas informações, não são todos os registros " \
         "que possuem a informação de gênero. Alguns registros a informação de " \
         "gênero está vazia('')"
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2, as_type=int)


def extract_min_and_max_from_list(members: List[int]) -> Tuple[int, int]:
    """
    Extrai o valor mínimo e máximo da lista informada como parâmetro
    :param members: Lista de inteiros de onde será extraido os valores mínimos e máximos
    :return: Retorna uma tupla onde valor_minimo, valor_maximo
    """
    min_value = 0
    max_value = 0
    for duration in members:
        if not min_value and not max_value:
            min_value = max_value = duration
            continue
        if duration < min_value:
            min_value = duration
        elif duration > max_value:
            max_value = duration
    return min_value, max_value


def calculate_mean_from_list(members: List[int]) -> int:
    """
    Calcula média aritmética a partir de uma lista de inteiros
    Implementação baseada no link: https://stackoverflow.com/questions/7716331/calculating-arithmetic-mean-average-in-python
    :param members: Lista com os números inteiros
    :return: um inteiro com a média
    """
    return int(round(sum(members) / len(members)))


def calculate_median_from_list(members: List[int]) -> int:
    """
    Calcula a mediana a partir de uma lista
    Implementação baseada no link: https://stackoverflow.com/questions/24101524/finding-median-of-list-in-python
    :param members: Lista de inteiros usados para o calculo
    :return:
    """
    members.sort()
    middle_index = len(members) // 2

    if not len(members) % 2:
        median = int((members[middle_index - 1] + members[middle_index]) / 2.0)
    else:
        median = int(members[middle_index])
    return median


min_trip, max_trip = extract_min_and_max_from_list(trip_duration_list)
mean_trip = calculate_mean_from_list(trip_duration_list)
median_trip = calculate_median_from_list(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = {s for s in column_to_list(data_list, 3)}

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada,
# a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#     """
#     Função de exemplo com anotações.
#     Argumentos:
#         param1: O primeiro parâmetro.
#         param2: O segundo parâmetro.
#     Retorna:
#         Uma lista de valores x.
#
#     """
def count_occurrences(members: List[Any]) -> Dict[Any, int]:
    """
    Função para contar ocorrências dos valores em uma determinada lista
    :param members: Lista de qualquer tipo
    :return: Dicionário com as ocorrências como chaves e o valores com a quantidade
    """
    return {c[0]: c[1] for c in Counter(members).most_common()}


occurrences_stations = count_occurrences(column_to_list(data_list, 3))
print(occurrences_stations)
occurrences_genders = count_occurrences(column_to_list(data_list, -2))
print(occurrences_genders)


input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"


def count_items(column_list):
    item_types_and_count = defaultdict(int)
    for item in column_list:
        item_types_and_count[item] += 1
    return item_types_and_count.keys(), item_types_and_count.values()


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
