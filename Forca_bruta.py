def distanc(inicio,fim):
  distancia = abs(inicio[0]-fim[0]) + abs(inicio[1]-fim[1])
  return distancia

def distancia_total(rota_atual, pontosEntrega):
  count = 0
  
  for index, ponto_atual in enumerate(rota_atual):
    
    if(index == len(rota_atual) - 1):
      return count
    count += distanc(pontosEntrega[ponto_atual], pontosEntrega[rota_atual[index + 1]])

def criando_rotas(rotas, rota_atual, pontosEntrega):
  
  if len(pontosEntrega) == 0:
    rotas.append(rota_atual + "R")
    
  for ponto_atual in pontosEntrega:
    criando_rotas(rotas, rota_atual + ponto_atual, [x for x in pontosEntrega if x != ponto_atual])
  return rotas

pontosEntrega = {}
matriz = []
with open("matriz.txt") as arq:
    valores = arq.readlines()
    valores.pop(0)
    
    for linhas in valores:
      matriz.append(linhas.split())

    for i,line in enumerate(matriz):  
      for j,ponto in enumerate(line):
        if ponto.isnumeric() == False:
          pontosEntrega[ponto] = [i,j]

inicio = pontosEntrega.pop("R")
rotas = criando_rotas([], "R", pontosEntrega)
pontosEntrega["R"] = inicio

count = None
percurso = ''

distancias = {}
for percurso in rotas:

  distancias[percurso] = distancia_total(percurso, pontosEntrega)
  
  if count == None:
    count = distancias[percurso]

  elif count > distancias[percurso]:
    count = distancias[percurso]
    percurso = distancias[percurso]

print(f"A Menor rota é {percurso} com distância de {count}")