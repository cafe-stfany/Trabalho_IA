import pygame
import time
import sys

TAM_CELULA = 20
cavaleiros = ["Seiya", "Shiryu", "Hyoga", "Shun", "Ikki"]

def carregar_imagens():
    imagens = {}
    for cav in cavaleiros:
        try:
            img_vivo = pygame.image.load(f"imagens/{cav.lower()}.png")
            img_morto = pygame.image.load(f"imagens/{cav.lower()}_morto.png")
            imagens[cav] = pygame.transform.scale(img_vivo, (TAM_CELULA, TAM_CELULA))
            imagens[f"{cav}_morto"] = pygame.transform.scale(img_morto, (TAM_CELULA, TAM_CELULA))
        except:
            print(f"⚠️ Erro ao carregar imagem de {cav}")
    print("Imagens carregadas:", list(imagens.keys()))

    return imagens

def animar_agente(mapa, caminhos, mortos, entrada, chegada, caminho_total):

    rastro_ativo = set()

    rastros = {c: set() for c in cavaleiros}

    pygame.init()
    largura = len(mapa[0]) * TAM_CELULA
    altura = len(mapa) * TAM_CELULA
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Cavaleiros do Zodíaco – Caminho dos Vivos")
    clock = pygame.time.Clock()

    imagens = carregar_imagens()

    # Carrega terrenos
    img_plano = pygame.transform.scale(pygame.image.load("imagens/montanhoso.jpg"), (TAM_CELULA, TAM_CELULA))
    img_rochoso = pygame.transform.scale(pygame.image.load("imagens/plano.jpg"), (TAM_CELULA, TAM_CELULA))
    img_montanhoso = pygame.transform.scale(pygame.image.load("imagens/rochoso.jpg"), (TAM_CELULA, TAM_CELULA))
    img_casa = pygame.transform.scale(pygame.image.load("imagens/Templo.jpg"), (TAM_CELULA, TAM_CELULA))

    max_passos = max(len(caminhos[c]) for c in cavaleiros if c in caminhos)

    for passo in range(max_passos + 1):
        for cav in cavaleiros:
            if cav in caminhos and passo < len(caminhos[cav]):
                pos = caminhos[cav][passo]
                rastros[cav].add(pos)  # adiciona posição visitada

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Desenha o mapa com imagens
        for i in range(len(mapa)):
            for j in range(len(mapa[0])):
                valor = mapa[i][j]
                x, y = j * TAM_CELULA, i * TAM_CELULA

                if valor == 14:
                    tela.blit(img_plano, (x, y))
                elif valor == 15:
                    tela.blit(img_rochoso, (x, y))
                elif valor == 16:
                    tela.blit(img_montanhoso, (x, y))
                elif 1 <= valor <= 12:
                    tela.blit(img_casa, (x, y))
                else:
                    pygame.draw.rect(tela, (0, 0, 0), (x, y, TAM_CELULA, TAM_CELULA))
        # Destaca entrada (vermelho) e chegada (verde)
        pygame.draw.rect(tela, (255, 0, 0), (entrada[1]*TAM_CELULA, entrada[0]*TAM_CELULA, TAM_CELULA, TAM_CELULA))  # vermelho
        pygame.draw.rect(tela, (0, 255, 0), (chegada[1]*TAM_CELULA, chegada[0]*TAM_CELULA, TAM_CELULA, TAM_CELULA))  # verde
        # Desenha o rastro que já foi percorrido
        for pos in rastro_ativo:
            pygame.draw.rect(tela, (0, 0, 255), (pos[1]*TAM_CELULA + 6, pos[0]*TAM_CELULA + 6, 8, 8))



       
        # Atualiza o rastro com a posição dos cavaleiros vivos neste passo
        for cav in cavaleiros:
            if cav in caminhos and passo < len(caminhos[cav]):
                delay = 2  # quantos passos atrás o rastro deve aparecer
                passo_rastro = passo - delay

                if cav in caminhos and passo_rastro >= 0:
                    pos_rastro = caminhos[cav][passo_rastro]
                    rastro_ativo.add(pos_rastro)


        # Desenha cavaleiros vivos
        for idx, cav in enumerate(cavaleiros):
            if cav in caminhos and passo < len(caminhos[cav]):
                pos = caminhos[cav][passo]
                img = imagens.get(cav)
                if img:
                    offset_x = idx * 12 # deslocamento horizontal (entre cavaleiros)
                    tela.blit(img, (pos[1]*TAM_CELULA + offset_x, pos[0]*TAM_CELULA))



        # Desenha cavaleiros mortos
        for cav, pos_morte in mortos.items():
            if pos_morte and cav in caminhos:
                try:
                    idx_morte = caminhos[cav].index(pos_morte)
                except ValueError:
                    continue  # posição não encontrada no caminho

                if passo >= idx_morte:
                    img = imagens.get(f"{cav}_morto", imagens.get(cav, None))
                    if img:
                        tela.blit(img, (pos_morte[1]*TAM_CELULA, pos_morte[0]*TAM_CELULA))


        pygame.display.flip()
        clock.tick(4)

    time.sleep(3)
    pygame.quit()
