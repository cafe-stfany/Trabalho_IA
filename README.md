# 💫 Projeto de Inteligência Artificial — Cavaleiros do Zodíaco

Este projeto simula a jornada dos Cavaleiros de Bronze através das 12 Casas do Zodíaco, com foco em Inteligência Artificial, algoritmos de busca e tomada de decisão em ambiente hostil. Inspirado no anime *Os Cavaleiros do Zodíaco*.

## 🔧 Tecnologias Utilizadas
- Python 3.13
- Pygame (para visualização gráfica)
- Algoritmo A* (A Star)
- Lógica de batalhas com sistema de energia e dificuldade por templo

## 🧠 Funcionalidades
- Caminho calculado automaticamente usando o algoritmo A*
- Batalhas entre cavaleiros com base em energia e dificuldade do templo
- Interface visual das casas, cavaleiros, terrenos e resultado das batalhas
- Cavaleiros mortos ficam no templo em que morreram
- Apenas cavaleiros vivos continuam avançando

## 📁 Estrutura de Arquivos

Trabalho_IA/
├── main.py # Execução principal
├── busca.py # Algoritmo A*
├── batalha.py # Lógica de batalha
├── interface.py # Interface gráfica com Pygame
├── utils.py # Funções auxiliares
├── mapa.csv # Mapa com as 12 casas
├── imagens/ # Imagens dos terrenos e cavaleiros
└── pycache/ # Arquivos compilados


## 🧪 Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/cafe-stfany/Trabalho_IA.git
## Instale as dependências:
pip install pygame
## Execute
python main.py

✨ Créditos
Desenvolvido por Palloma Stfany Silva Café e Luiz Gabriel como projeto acadêmico de Inteligência Artificial (UFMT).
