import random

def distanc(inicio, fim):
  return abs(inicio[0] - fim[0]) + abs(inicio[1] - fim[1])

def percurso(rota_atual, pontosEntrega):
  count = 0
  for index, ponto_atual in enumerate(rota_atual):
    if(index == len(rota_atual) - 1):
      return count

    count += distanc(pontosEntrega[ponto_atual], pontosEntrega[rota_atual[index + 1]])

def populacaoInicial(coordenadas):
  coordenadas_validas = [x for x in coordenadas if x != "R"]
  populacao_inicial = []

  for i in range(0, 4):
    novo_individuo = {'individuo': None, 'percurso': 0}
    novo_individuo['individuo'] = random.sample(coordenadas_validas, len(coordenadas_validas))

    while novo_individuo['individuo'] in populacao_inicial:
      novo_individuo['individuo'] = random.sample(coordenadas_validas, len(coordenadas_validas))

    novo_individuo['individuo'].insert(0, 'R')
    novo_individuo['individuo'].append('R')
    novo_individuo['percurso'] = percurso(novo_individuo['individuo'], coordenadas)

    populacao_inicial.append(novo_individuo)

  return populacao_inicial

def selecionaoMelhores(populacao):
  populacao.sort(key=lambda individuo : individuo['percurso'])
  return [populacao[0], populacao[1]]

def criarFilho(pool):
  pool = random.sample(pool, len(pool))
  filho = {'individuo' : [], 'percurso': 0}

  for gene in pool:
    if gene not in filho['individuo']:
      filho['individuo'].append(gene)
  
  filho['individuo'].insert(0, 'R')
  filho['individuo'].append('R')
  filho['percurso'] = percurso(filho['individuo'], pontosEntrega)

  return filho

def mutacao(filho):
  index = random.randint(1, 4)
  index2 = random.randint(1, 4)
  if index != index2:
    filho['individuo'][index], filho['individuo'][index2] = filho['individuo'][index2], filho['individuo'][index]

  return filho

def crossover(pai, mae):
  gene_pai = pai['individuo'][1:5]
  gene_mae = mae['individuo'][1:5]
  pool = gene_pai + gene_mae

  filho1 = criarFilho(pool)
  filho2 = criarFilho(pool)
  filho1 = mutacao(filho1)
  filho2 = mutacao(filho2)

  return [pai, mae, filho1, filho2]

def imprimeGeracao(geracao, i):
  print("Geracao {}".format(i))
  for individuo in geracao:
    print("Individuo: {} - percurso: {}".format(individuo['individuo'], individuo['percurso']))

  print()

def inicia(geracao):
  pai, mae = selecionaoMelhores(geracao)
  nova_geracao = crossover(pai, mae)
  imprimeGeracao(geracao, 2)
  
  for i in range(3, 6):
    pai, mae = selecionaoMelhores(nova_geracao)
    nova_geracao = crossover(pai, mae)
    imprimeGeracao(nova_geracao, i)

    
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
          

populacao_inicial = populacaoInicial(pontosEntrega)
imprimeGeracao(populacao_inicial, 1)
inicia(populacao_inicial)
