import csv
import sys

# Carrega o mapa a partir de um CSV
def carregar_mapa(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            leitor = csv.reader(arquivo, delimiter=',')
            mapa = []
            for linha in leitor:
                if linha:
                    linha_int = []
                    for celula in linha:
                        try:
                            linha_int.append(int(celula))
                        except ValueError:
                            linha_int.append(14)
                    mapa.append(linha_int)
            return mapa
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado!")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        sys.exit(1)

# Converte o mapa em pesos para o algoritmo A*
def traduzir_mapa(mapa):
    mapa_convertido = []
    for linha in mapa:
        nova_linha = []
        for valor in linha:
            if valor == 14:  # Montanhoso
                nova_linha.append(999)
            elif valor == 15:  # Plano
                nova_linha.append(1)
            elif valor == 16:  # Rochoso
                nova_linha.append(5)
            elif valor == 0 or valor == 13:  # Entrada / Chegada
                nova_linha.append(1)
            elif 1 <= valor <= 12:  # Casas do Zodíaco
                nova_linha.append(2)
            else:
                nova_linha.append(50)
        mapa_convertido.append(nova_linha)
    return mapa_convertido

# Encontra a posição de entrada e chegada
def encontrar_pontos(mapa):
    entrada = None
    chegada = None
    for i, linha in enumerate(mapa):
        for j, valor in enumerate(linha):
            if valor == 0:
                entrada = (i, j)
            elif valor == 13:
                chegada = (i, j)
    return entrada, chegada