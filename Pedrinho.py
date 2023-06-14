import numpy as np
import matplotlib.pyplot as plot
import math

Qtd_nos = int(input("Quantos nós serão utilizados: "))

vetor_x = list(range(Qtd_nos))
vetor_y = list(range(Qtd_nos))
nos = []
for i in range(0, Qtd_nos):
    vetor_x[i] = int(input(f"Digite a coordenada X do nó {i}: "))
    vetor_y[i] = int(input(f"Digite a coordenada Y do nó {i}: "))
    nos.append([vetor_x[i],vetor_y[i]])
print()

for i in range(0, Qtd_nos):
    print(f"Nó {i} = {nos[i]}")
    
print()
barras = list(range(Qtd_nos))
for i in range(0, Qtd_nos):
    barras[i] = int(input(f"Deseja conectar o nó {i} {nos[i]} a qual nó: "))    

Qtd_apoios = ("Digite a quantidade de apoios: ")
apoios = list(range(Qtd_apoios))
for i in range(0, Qtd_apoios):
    apoios = print(f"Digite em qual nó o apoio se encontra: ")
dif_y = list(range(Qtd_nos))
dif_x = list(range(Qtd_nos))

for i in range(0, Qtd_nos):
    dif_x[i] = vetor_x[barras[i]] - vetor_x[i]
    dif_y[i] = vetor_y[barras[i]] - vetor_y[i]
    dif_x[i] = abs(dif_x[i])
    dif_y[i] = abs(dif_y[i])

dif_x2 = list(range(Qtd_nos))
dif_y2 = list(range(Qtd_nos))
soma_2 = list(range(Qtd_nos))
tamanho_barra = list(range(Qtd_nos))

for i in range(0, Qtd_nos):
    dif_x2[i] = dif_x[i] ** 2
    dif_y2[i] = dif_y[i] ** 2

for i in range(0, Qtd_nos):
    soma_2[i] = dif_x2[i] + dif_y2[i]
    tamanho_barra[i] =  math.sqrt(soma_2[i])

print(tamanho_barra)
 
