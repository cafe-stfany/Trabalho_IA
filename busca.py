import heapq

def heuristica(a, b):
    # Distância de Manhattan
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_estrela(mapa, inicio, fim):
    fila = []
    heapq.heappush(fila, (0, inicio))
    veio_de = {}
    custo_total = {inicio: 0}
    visitados = set()

    while fila:
        _, atual = heapq.heappop(fila)

        if atual == fim:
            break

        if atual in visitados:
            continue
        visitados.add(atual)

        x, y = atual
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(mapa) and 0 <= ny < len(mapa[0]):
                vizinho = (nx, ny)
                novo_custo = custo_total[atual] + mapa[nx][ny]

                if vizinho not in custo_total or novo_custo < custo_total[vizinho]:
                    custo_total[vizinho] = novo_custo
                    prioridade = novo_custo + heuristica(vizinho, fim)
                    heapq.heappush(fila, (prioridade, vizinho))
                    veio_de[vizinho] = atual

    # Reconstruir caminho
    caminho = []
    atual = fim
    while atual != inicio:
        caminho.append(atual)
        atual = veio_de.get(atual)
        if atual is None:
            print("❌ Caminho não encontrado!")
            return [], float('inf')
    caminho.append(inicio)
    caminho.reverse()
    return caminho, custo_total[fim]