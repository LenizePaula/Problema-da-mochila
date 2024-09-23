import random

# Geração da população inicial
def gerar_populacao(num_individuos, tamanho):
    return [[random.randint(0, 1) for _ in range(tamanho)] for _ in range(num_individuos)]

# Função de avaliação dos idivíduos (fitness)
def fitness(individuo, pesos_e_valores, peso_maximo):
    valor_total = 0
    peso_total = 0
    for i in range(len(individuo)):
        if individuo[i] == 1:
            peso_total += pesos_e_valores[i][0]
            valor_total += pesos_e_valores[i][1]
    if peso_total > peso_maximo:
        return 0 
    return valor_total

# Seleção por roleta
def selecao_por_roleta(populacao, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i in range(len(populacao)):
        current += fitnesses[i]
        if current > pick:
            return populacao[i]

# Função de cruzamento
def crossover(pai1, pai2):
    ponto = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

# Função de mutação
def mutacao(individuo, taxa_mutacao):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i] 

# Algoritmo Genético
def algoritmo_genetico(pesos_e_valores, peso_maximo, num_individuos, num_geracoes, taxa_mutacao):
    tamanho = len(pesos_e_valores)
    populacao = gerar_populacao(num_individuos, tamanho)
    melhor_por_geracao = []
    
    for geracao in range(num_geracoes):
        fitnesses = [fitness(ind, pesos_e_valores, peso_maximo) for ind in populacao]
        
        # Guarda o melhor da geração
        melhor_individuo = populacao[fitnesses.index(max(fitnesses))]
        melhor_por_geracao.append([max(fitnesses), melhor_individuo])
        
        
        nova_populacao = []
        
        # Gerar nova população
        while len(nova_populacao) < num_individuos:
            pai1 = selecao_por_roleta(populacao, fitnesses)
            pai2 = selecao_por_roleta(populacao, fitnesses)
            filho1, filho2 = crossover(pai1, pai2)
            mutacao(filho1, taxa_mutacao)
            mutacao(filho2, taxa_mutacao)
            nova_populacao.append(filho1)
            nova_populacao.append(filho2)
        
        populacao = nova_populacao[:num_individuos]
    
    # Melhor solução encontrada
    fitnesses_finais = [fitness(ind, pesos_e_valores, peso_maximo) for ind in populacao]    
    return melhor_por_geracao

# Parâmetros de entrada
pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]]
peso_maximo = 100
numero_de_cromossomos = 150
geracoes = 50
taxa_mutacao = 0.05  # Taxa de mutação de 5%

# Executa o algoritmo genético
melhor_por_geracao = algoritmo_genetico(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes, taxa_mutacao)

print("Melhores por geração:")
for geracao, melhor in enumerate(melhor_por_geracao):
    print(f"Geração {geracao+1}: {melhor}")
