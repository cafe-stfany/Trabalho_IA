import pygame
import csv
import sys

# Cores
COR_GRADE = (0, 0, 0)
AZUL = (50, 150, 255)            # caminho
VERDE = (0, 255, 0)              # chegada (13)
VERMELHO = (255, 0, 0)           # entrada (0)
PRETO = (0, 0, 0)                # fundo
AMARELO = (255, 255, 0)          # casas 1 a 12

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

def animar_agente(mapa_original, caminho):
    pygame.init()
    tamanho_celula = 18
    largura = len(mapa_original[0]) * tamanho_celula
    altura = len(mapa_original) * tamanho_celula
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Saga do Santuário")

    # Carregar imagens
    try:
        plano_img = pygame.image.load("imagens/plano.jpg").convert()
        plano_img = pygame.transform.scale(plano_img, (tamanho_celula, tamanho_celula))
    except:
        plano_img = None

    try:
        rochoso_img = pygame.image.load("imagens/rochoso.jpg").convert()
        rochoso_img = pygame.transform.scale(rochoso_img, (tamanho_celula, tamanho_celula))
    except:
        rochoso_img = None

    try:
        montanhoso_img = pygame.image.load("imagens/montanhoso.jpg").convert()
        montanhoso_img = pygame.transform.scale(montanhoso_img, (tamanho_celula, tamanho_celula))
    except:
        montanhoso_img = None

    try:
        templo_img = pygame.image.load("imagens/Templo.jpg").convert_alpha()
        templo_img = pygame.transform.scale(templo_img, (tamanho_celula, tamanho_celula + 8))
    except Exception as e:
        print(f"⚠️ Erro ao carregar imagem do templo: {e}")
        templo_img = None
    try:
        agente_img = pygame.image.load("imagens/seiya.png").convert_alpha()
        agente_img = pygame.transform.scale(agente_img, (tamanho_celula, tamanho_celula))
    except Exception as e:
        print(f"⚠️ Erro ao carregar imagem do agente: {e}")
        agente_img = None


    for passo in caminho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

        tela.fill(PRETO)

        for i, linha in enumerate(mapa_original):
            for j, valor in enumerate(linha):
                x = j * tamanho_celula
                y = i * tamanho_celula

                if valor == 0:
                    pygame.draw.rect(tela, VERMELHO, (x, y, tamanho_celula, tamanho_celula))
                elif valor == 13:
                    pygame.draw.rect(tela, VERDE, (x, y, tamanho_celula, tamanho_celula))
                elif valor == 15:
                    if plano_img:
                        tela.blit(plano_img, (x, y))
                    else:
                        pygame.draw.rect(tela, (200, 200, 200), (x, y, tamanho_celula, tamanho_celula))
                elif valor == 16:
                    if rochoso_img:
                        tela.blit(rochoso_img, (x, y))
                    else:
                        pygame.draw.rect(tela, (150, 150, 150), (x, y, tamanho_celula, tamanho_celula))
                elif valor == 14:
                    if montanhoso_img:
                        tela.blit(montanhoso_img, (x, y))
                    else:
                        pygame.draw.rect(tela, (100, 100, 100), (x, y, tamanho_celula, tamanho_celula))
                elif 1 <= valor <= 12:
                    pygame.draw.rect(tela, AMARELO, (x, y, tamanho_celula, tamanho_celula))
                    if templo_img:
                        tela.blit(templo_img, (x, y - 6))
                else:
                    pygame.draw.rect(tela, PRETO, (x, y, tamanho_celula, tamanho_celula))

        # Desenha o agente
        ax, ay = passo
        px = ay * tamanho_celula
        py = ax * tamanho_celula
        if agente_img:
            tela.blit(agente_img, (px, py))
        else:
            pygame.draw.circle(tela, AZUL, (px + tamanho_celula // 2, py + tamanho_celula // 2), 8)


        # Grade sobreposta
        for y in range(0, altura, tamanho_celula):
            pygame.draw.line(tela, COR_GRADE, (0, y), (largura, y), 1)
        for x in range(0, largura, tamanho_celula):
            pygame.draw.line(tela, COR_GRADE, (x, 0), (x, altura), 1)

        pygame.display.flip()
        pygame.time.delay(150)

    pygame.time.delay(500)
    pygame.quit()