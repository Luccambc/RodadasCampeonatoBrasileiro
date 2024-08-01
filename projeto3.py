import os
from collections import defaultdict

import matplotlib.colors as mcolors
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import networkx as nx

times = {
    "CAP": "Athletico-PR",
    "ACG": "Atlético-GO",
    "CAM": "Atlético-MG",
    "ECB": "Bahia",
    "BFR": "Botafogo",
    "SCCP": "Corinthians",
    "CEC1": "Criciúma",
    "CEC2": "Cruzeiro",
    "CEC3": "Cuiabá",
    "CRF": "Flamengo",
    "FFC": "Fluminense",
    "FSC": "Fortaleza",
    "FBPA": "Grêmio",
    "SCI": "Internacional",
    "ECJ": "Juventude",
    "SEP": "Palmeiras",
    "RBB": "RedBull Bragantino",
    "SPFC": "São Paulo",
    "CRVG": "Vasco da Gama",
    "ECV": "Vitória"
}

restricoes = {
    "CAP": [],
    "ACG": [],
    "CAM": ["CEC2"],
    "ECB": ["ECV"],
    "BFR": ["CRF", "FFC", "CRVG"],
    "SCCP": ["SEP", "SPFC"],
    "CEC1": [],
    "CEC2": ["CAM"],
    "CEC3": [],
    "CRF": ["BFR", "FFC", "CRVG"],
    "FFC": ["CRF", "BFR", "CRVG"],
    "FSC": [],
    "FBPA": ["SCI"],
    "SCI": ["FBPA"],
    "ECJ": [],
    "SEP": ["SPFC", "SCCP"],
    "RBB": [],
    "SPFC": ["SEP", "SCCP"],
    "CRVG": ["CRF", "FFC", "BFR"],
    "ECV": ["ECB"]
}

def round_robin_schedule(teams):
    n = len(teams)
    schedule = []
    
    for i in range(n-1):
        round = []
        for j in range(n // 2):
            home = teams[j]
            away = teams[n - 1 - j]
            round.append((home, away))
        teams.insert(1, teams.pop())
        schedule.append(round)
        
    return schedule

teams = list(times.keys())
schedule_ida = round_robin_schedule(teams)

# Gerar cronograma de volta invertendo os jogos da ida
schedule_volta = []
for round in schedule_ida:
    schedule_volta.append([(away, home) for home, away in round])

full_schedule = schedule_ida + schedule_volta




def adjust_schedule(schedule, restricoes):
    adjusted_schedule = []
    
    for round in schedule:
        state_mandantes = defaultdict(int)
        adjusted_round = []
        
        for match in round:
            home, away = match
            home_restrictions = restricoes[home]
            valid_home = True
            
            for restriction in home_restrictions:
                if state_mandantes[restriction] > 0:
                    valid_home = False
                    break
            
            if valid_home:
                state_mandantes[home] += 1
                adjusted_round.append((home, away))
            else:
                state_mandantes[away] += 1
                adjusted_round.append((away, home))
        
        adjusted_schedule.append(adjusted_round)
    
    return adjusted_schedule

adjusted_schedule = adjust_schedule(full_schedule, restricoes)

# Validação do Cronograma
def validate_schedule(schedule, restricoes):
    for round in schedule:
        state_mandantes = defaultdict(int)
        
        for match in round:
            home, away = match
            home_restrictions = restricoes[home]
            
            for restriction in home_restrictions:
                if state_mandantes[restriction] > 0:
                    return False
            
            state_mandantes[home] += 1
    
    return True

is_valid = validate_schedule(adjusted_schedule, restricoes)
print("Cronograma válido:", is_valid)

def save_schedule_to_file(schedule, times, filename):
    with open(filename, 'w') as file:
        for i, round in enumerate(schedule):
            file.write(f"Rodada {i + 1}:\n")
            for home, away in round:
                file.write(f"{times[home]} (mandante) vs {times[away]} (visitante)\n")
            file.write("\n")

# Salvar o cronograma ajustado em um arquivo .txt
save_schedule_to_file(adjusted_schedule, times, 'cronograma.txt')

def create_graph_from_schedule(schedule, teams):
    G = nx.Graph()
    
    # Adiciona todos os times como nós
    for team in teams:
        G.add_node(team)
    
    # Adiciona arestas para cada partida no cronograma
    for round in schedule:
        for home, away in round:
            if not G.has_edge(home, away):
                G.add_edge(home, away)
    
    return G

def draw_graph(G, times):
    pos = nx.spring_layout(G, seed=42)  # Layout para o grafo
    plt.figure(figsize=(12, 12))
    nx.draw(G, pos, with_labels=True, labels={node: times[node] for node in G.nodes()}, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray')
    plt.title('Visualização do Cronograma de Partidas')
    plt.show()

# Crie o grafo a partir do cronograma ajustado
G = create_graph_from_schedule(adjusted_schedule, times)

# Desenhe o grafo
draw_graph(G, times)



def find_optimal_coloring(G):
    # Encontrar uma coloração ótima usando a coloração gananciosa
    coloring = nx.coloring.greedy_color(G, strategy='largest_first')
    return coloring

def draw_colored_graph(G, coloring, times):
    pos = nx.spring_layout(G, seed=42)
    colors = [coloring[node] for node in G.nodes()]
    
    # Criar um dicionário de cores para os nós
    unique_colors = list(set(colors))
    color_map = plt.cm.viridis
    color_hex = {color: mcolors.to_hex(color_map(color / max(unique_colors))) for color in unique_colors}
    
    plt.figure(figsize=(12, 12))
    # Desenhar o grafo
    nx.draw(G, pos, with_labels=True, labels={node: times[node] for node in G.nodes()}, node_size=3000, node_color=colors, cmap=plt.cm.viridis, font_size=10, font_weight='bold', edge_color='gray')
    
    # Criar uma legenda personalizada com códigos hexadecimais
    legend_patches = [patches.Patch(color=color_map(color / max(unique_colors)), label=f'Cor {color}: {color_hex[color]}') for color in unique_colors]
    plt.legend(handles=legend_patches, loc='best', title='Legenda das Cores')
    
    plt.title('Visualização do Grafo com Coloração Ótima')
    plt.show()

# Encontrar a coloração ótima
coloring = find_optimal_coloring(G)

# Exibir a coloração dos vértices
print("Coloração dos vértices:")
for node, color in coloring.items():
    print(f"{times[node]}: Cor {color}")

# Desenhar o grafo colorido com legenda personalizada
draw_colored_graph(G, coloring, times)
