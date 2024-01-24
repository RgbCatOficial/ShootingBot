*Importando bibliotecas*
import numpy as np
import random

Criando lista de recompensas*
rewards = [
[-1, 1, 1, 1, 1, 1], # Lugar maior para atirar = menos pontos
[-1, -1, 10, 10, 10, 10],
[-1, -1, -1, 100, 100, 100],
[-1, -1, -1, -1, 1000, 1000],
[-1, -1, -1, -1, -1, 10000] # Lugar menor para atirar = mais pontos
]

Esta função randomiza o nível de tiro
def set_shooting_level():
return np.random.randint(0, 5)

Imprimindo um exemplo do nível de tiro:
print("Exemplo: nível de tiro randomizado como", set_shooting_level())

O primeiro tiro para a primeira experiência
first_shoot = set_shooting_level()

Criando uma função que pode obter uma ação aleatória (se algo for alcançado, o bot recebe recompensas)
def get_action(current_state, reward):
avaiable_action = []
print("Recompensas disponíveis:\n", reward)
print("Tentando nível", current_state, "de tiro:")
tries = 1
for action in enumerate(reward[current_state]):
print("Número da tentativa", tries)
print("Tiro: ", action)
if action[1] != -1:
avaiable_action.append(action[0])
tries += 1

Chamando a função
get_action(first_shoot, rewards)

Explicação do código:
O objetivo é criar um bot de tiro funcional;
O bot tenta um nível aleatório de tiro, que pode ser fácil ou difícil;
Com base na dificuldade do nível escolhido, o bot recebe mais pontos do que em um nível mais fácil;
Em todos os níveis, se o bot errar, ele perde 1 ponto