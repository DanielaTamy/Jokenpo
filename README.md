# ✋📝 Jogo Jokenpô e Uso de Matrizes
Março/2023
Raciocínio Algorítmico - 1° período Ciência da Computação PUCPR

Este repositório contém dois programas em Python que implementam o clássico jogo Jokenpô (Pedra, Papel, Tesoura). Um dos programas usa estruturas tradicionais de controle e o outro utiliza uma matriz para determinar o vencedor de cada rodada de forma eficiente.

## 📂 Arquivos

1. **jokenpo_simples.py**:
   - Este arquivo implementa o jogo Jokenpô com três modalidades diferentes:
     - **👤 vs 👤 Modo humano x humano**: Dois jogadores humanos jogam entre si.
     - **👤 vs 🤖 Modo humano x computador**: Um jogador humano enfrenta o computador.
     - **🤖 vs 🤖 Modo computador x computador**: Dois computadores jogam entre si.
   - O código utiliza estruturas básicas como loops `while`, declarações condicionais `if` e funções para verificar os vencedores de cada rodada.
  
2. **jokenpo_com_matriz.py**:
   - Este arquivo usa uma matriz 3x3 para determinar o vencedor do Jokenpô de forma mais eficiente.
   - A matriz predefine os resultados para cada combinação de jogadas, simplificando a lógica de verificação do vencedor.
   - Assim como no arquivo anterior, são oferecidos os três modos de jogo (humano x humano, humano x computador e computador x computador).

## 📜 Regras do Jogo

As regras do Jokenpô são as seguintes:
- **🪨 Pedra (0)** ganha da **✂️ Tesoura (2)**.
- **✂️ Tesoura (2)** ganha do **📄 Papel (1)**.
- **📄 Papel (1)** ganha da **🪨 Pedra (0)**.

## ▶️ Como Executar

1. **Pré-requisitos**:
   - Certifique-se de ter o **Python 3** instalado em seu sistema.
   - Baixe ou clone este repositório.

2. **Execução**:
   - Para executar o jogo em modo simples, use o comando:
     ```bash
     python jokenpo_simples.py
     ```
   - Para executar o jogo que utiliza matrizes para verificar o vencedor, use o comando:
     ```bash
     python jokenpo_com_matriz.py
     ```

3. **🎮 Interações no Jogo**:
   - O programa solicitará que você escolha uma das modalidades de jogo (humano x humano, humano x computador ou computador x computador).
   - Dependendo da modalidade, o jogador será solicitado a inserir sua jogada ou visualizar as jogadas do computador.
   - A cada rodada, o 🏆 placar será exibido.
   - O jogo pode continuar por várias rodadas até que você decida encerrar.

