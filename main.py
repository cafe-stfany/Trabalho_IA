from utils import carregar_mapa, traduzir_mapa, encontrar_pontos
from busca import a_estrela
from interface import animar_agente
from batalha import batalhar, cavaleiro_vivo

# Carregamento e preparação
mapa_original = carregar_mapa("mapa.csv")
entrada, chegada = encontrar_pontos(mapa_original)
print(f"📍 Entrada: {entrada} | Chegada: {chegada}")

mapa_convertido = traduzir_mapa(mapa_original)
caminho, custo_total = a_estrela(mapa_convertido, entrada, chegada)

# Exibe o caminho percorrido
print("\n🧭 Caminho percorrido pelo agente:")
for passo in caminho:
    print(f" → {passo}", end="")
print(f"\n\n🎯 Custo total do caminho: {custo_total:.2f} minutos")

# Executar batalhas nas casas do zodíaco
cavaleiros_disponiveis = ["Seiya", "Shiryu", "Hyoga", "Shun", "Ikki"]
casas_batalhadas = set()
tempo_batalhas = 0

for passo in caminho:
    x, y = passo
    valor = mapa_original[x][y]

    if 1 <= valor <= 12 and valor not in casas_batalhadas:
        casas_batalhadas.add(valor)
        vivos = [c for c in cavaleiros_disponiveis if cavaleiro_vivo(c)]

        if vivos:
            tempo = batalhar(valor, vivos)
            tempo_batalhas += tempo if tempo else 0
        else:
            print("⚠️ Todos os cavaleiros morreram. A missão falhou.")
            break


# Animação da trajetória
animar_agente(mapa_original, caminho)


# Mostrar tempo acumulado das batalhas
print(f"\n🔥 Tempo total gasto nas batalhas: {tempo_batalhas:.2f} minutos")
print(f"🧮 Tempo total (caminho + batalhas): {custo_total + tempo_batalhas:.2f} minutos")

