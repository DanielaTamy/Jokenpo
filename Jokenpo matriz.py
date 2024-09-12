#JOGO JOKENPÔ - TDE RACIOCÍNIO ALGORÍTMICO

# 0 --> empate 1 --> vitória do jogador1 2 --> vitória jogador2
# 0 = pedra 1 = papel 2 = tesoura
#jogador 1 = linhas    jogador2 = colunas
import random

contador1 = 0
contador2 = 0
def jogadorxjogador(jogador1, jogador2):
    matrizVencedor = [[0, 2, 1],
                      [1, 0, 2],
                      [2, 1, 0]]
    vencedor = matrizVencedor[jogador1][jogador2]
    global contador1 #global para indicar que pode ser modificavel
    global contador2
    if vencedor == 0:
        print("Empate")
    elif vencedor == 1:
        print("Jogador 1 ganhou")
        contador1 += 1
    else:
        print("Jogador 2 ganhou")
        contador2 += 1
    print("Placar:", contador1, "x", contador2)
    return vencedor

contador_jogador = 0
contador_computador = 0
def jogadorxcomputador(jogador, computador):
    matrizVencedor = [[0, 2, 1],
                      [1, 0, 2],
                      [2, 1, 0]]
    vencedor = matrizVencedor[jogador][computador]
    global contador_jogador
    global contador_computador
    if vencedor == 0:
        print("Empate")
    elif vencedor == 1:
        print("Jogador ganhou")
        contador_jogador += 1
    else:
        print("computador ganhou")
        contador_computador += 1
    print("Placar:", contador_jogador, "x", contador_computador)
    return vencedor

contador_computador1 = 0
contador_computador2 = 0
def computadorxcomputador(computador1, computador2):
    matrizVencedor = [[0, 2, 1],
                      [1, 0, 2],
                      [2, 1, 0]]
    vencedor = matrizVencedor[computador1][computador2]
    global contador_computador1
    global contador_computador2
    if vencedor == 0:
        print("Empate")
    elif vencedor == 1:
        print("computador 1 ganhou")
        contador_computador1 += 1
    else:
        print("computador 2 ganhou")
        contador_computador2 += 1
    print("Placar:", contador_computador1, "x", contador_computador2)
    return vencedor

# INTRODUÇÃO DO JOGO
print("BEM-VINDO AO JOGO JOKENPÔ")
print("Regras do jogo:\n"
      "- pedra ganha da tesoura\n"
      "- tesoura ganha do papel\n"
      "- papel ganha da pedra\n")

print("Modalidades de jogo:")
# Escolha de modalidade de jogo
print("1 - Modo humano X humano \n"
      "2 - Modo humano X computador \n"
      "3 - Modo computador X computador \n")

modo = int(input("Entre com a modalidade de jogo (1 a 3):"))

# Modo 1 - humano X humano
while modo == 1:
    print("Escolha uma opção: \n"
          "0 - pedra \n"
          "1 - papel \n"
          "2 - tesoura \n")
    jogador1 = int(input("Digite a opção do jogador 1:"))
    jogador2 = int(input("Digite a opção do jogador 2:"))
    resultado = jogadorxjogador(jogador1, jogador2)
    print("OPÇÕES: 1 - finalizar o jogo, 2 - continuar jogando")
    final = int(input("digite a opção desejada:"))
    if final == 2:
        continue
    else:
        print("Jogador 1: ", contador1, "vitória(s)")
        print("Jogador 2: ", contador2, "vitória(s)")
        if contador1 > contador2:
            print("jogador 1 venceu")
        elif contador1 < contador2:
            print("jogador 2 venceu")
        else:
            print("empate")
        print("Muito obrigada por jogar - Créditos: Daniela Yuki")
        break

#Modo 2 - humano X computador
while modo == 2:
    print("Escolha uma opção: \n"
          "0 - pedra \n"
          "1 - papel \n"
          "2 - tesoura \n")
    jogador = int(input("Digite a opção do jogador 1:"))
    computador = random.randint(0, 2)
    print("opção computador:", computador)
    resultado = jogadorxcomputador(jogador, computador)
    print("OPÇÕES: 1 - finalizar o jogo, 2 - continuar jogando")
    final = int(input("digite a opção desejada:"))
    if final == 2:
        continue
    else:
        print("Jogador 1: ", contador_jogador, "vitória(s)")
        print("Jogador 2: ", contador_computador, "vitória(s)")
        if contador_jogador > contador_computador:
            print("jogador venceu")
        elif contador_jogador < contador_computador:
            print("computador venceu")
        else:
            print("empate")
        print("Muito obrigada por jogar - Créditos: Daniela Yuki")
        break

#Modo 3 - computador X computador
while modo == 3:
    print("Escolha uma opção:"
          "1 - pedra \n "
          "2 - papel \n "
          "3 - tesoura \n")
    computador1 = random.randint(0,2)
    computador2 = random.randint(0,2)
    print("computador 1:", computador1)
    print("computador 2:", computador2)
    resultado = computadorxcomputador(computador1, computador2)
    print("OPÇÕES: 1 - finalizar o jogo, 2 - continuar jogando")
    final = int(input("digite a opção desejada:"))
    if final == 2:
        continue
    else:
        print("Jogador 1: ", contador_computador1, "vitória(s)")
        print("Jogador 2: ", contador_computador2, "vitória(s)")
        if contador_computador1 > contador_computador2:
            print("computador 1 venceu")
        elif contador_computador1 < contador_computador2:
            print("computador 2 venceu")
        else:
            print("empate")
        print("Muito obrigada por jogar - Créditos: Daniela Yuki")
        break