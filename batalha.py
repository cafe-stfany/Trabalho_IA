# batalha.py

# Dificuldades das casas
dificuldades = {
    1: 50, 2: 55, 3: 60, 4: 70, 5: 75, 6: 80,
    7: 85, 8: 90, 9: 95, 10: 100, 11: 110, 12: 120
}

# Poder cósmico dos cavaleiros
poder_cosmico = {
    "Seiya": 1.5,
    "Shiryu": 1.4,
    "Hyoga": 1.3,
    "Shun": 1.2,
    "Ikki": 1.1
}

# Energia inicial
energia = {nome: 5 for nome in poder_cosmico}

def cavaleiro_vivo(nome):
    return energia.get(nome, 0) > 0

def escolher_vivos(nomes):
    return [n for n in nomes if cavaleiro_vivo(n)]

# Estratégia por faixa de casa
def estrategia_por_casa(numero_casa, vivos):
    if numero_casa <= 3:
        preferidos = ["Ikki", "Shun"]
    elif numero_casa <= 6:
        preferidos = ["Hyoga", "Shun"]
    elif numero_casa <= 9:
        preferidos = ["Shiryu", "Hyoga"]
    else:
        preferidos = ["Seiya", "Shiryu"]

    # Filtra cavaleiros preferidos que estão vivos
    ativos = [c for c in preferidos if c in vivos]

    # Garante pelo menos dois cavaleiros vivos
    if len(ativos) < 2:
        adicionais = [c for c in vivos if c not in ativos]
        ativos += adicionais[:2 - len(ativos)]

    return ativos if ativos else vivos[:2]  # fallback

def batalhar(numero_casa, todos_vivos):
    if numero_casa not in dificuldades:
        print(f"Casa {numero_casa} não existe.")
        return 0

    vivos = escolher_vivos(todos_vivos)
    if not vivos:
        print("Nenhum cavaleiro disponível para lutar!")
        return float("inf")

    participantes = estrategia_por_casa(numero_casa, vivos)
    dificuldade = dificuldades[numero_casa]
    soma_poder = sum(poder_cosmico[n] for n in participantes)

    tempo = dificuldade / soma_poder

    print(f"\n🏛️ Casa {numero_casa} | Dificuldade: {dificuldade}")
    print(f"🤜 Participantes: {', '.join(participantes)}")
    print(f"⏱️ Tempo estimado: {tempo:.2f} minutos")

    for nome in participantes:
        energia[nome] -= 1
        if energia[nome] == 0:
            print(f"💀 {nome} perdeu toda a energia e morreu!")

    print(f"⚡ Energia atual: {energia}")
    return tempo