#JOGO JOKENPÔ - TDE RACIOCÍNIO ALGORÍTMICO

import random

#INTRODUÇÃO DO JOGO
print("BEM - VINDO AO JOGO JOKENPÔ")
print("Regras do jogo:\n"
"- pedra ganha da tesoura\n"
"- tesoura ganha do papel\n"
"- papel ganha da pedra\n")
print("Modalidades de jogo:")

#Escolha de modalidade de jogo
print("1 - Modo humano X humano \n"
      "2 - Modo humano X computador \n"
      "3 - Modo computador X computador \n")
modo = int(input("Entre com a modalidade de jogo (1 a 3):"))


#Modo 1 - humano X humano
contador_jogador1 = 0
contador_jogador2 = 0
while modo == 1:
    print("Escolha uma opção: \n"
          "1 - pedra \n"
          "2 - papel \n"
          "3 - tesoura \n")
    jogador1 = int(input("digite a opção do jogador 1:"))
    jogador2 = int(input("digite a opção do jogador 2:"))
    if jogador1 == jogador2:
        print("empate")
        print(contador_jogador1, "X", contador_jogador2)
    elif (jogador1 == 1 and jogador2 == 2) or (jogador1 == 2 and jogador2 == 3) or (jogador1 == 3 and jogador2 == 1):
        print("Jogador 2 venceu")
        contador_jogador2 += 1
        print(contador_jogador1, "X", contador_jogador2)
    elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 3 and jogador2 == 2):
        print("Jogador 1 venceu")
        contador_jogador1 += 1
        print(contador_jogador1, "X", contador_jogador2)
    else:
        print("Não está dentro das regras do jogo")
    print("OPÇÕES: 1 - finalizar o jogo, 2 - continuar jogando")
    final = int(input("digite a opção desejada:"))
    if final == 2:
        continue
    elif final == 1:
        print("Jogador 1:", contador_jogador1, "vitória(s)")
        print("Jogador 2:", contador_jogador2, "vitória(s)")
        if contador_jogador1 > contador_jogador2:
            print("jogador 1 venceu")
        elif contador_jogador1 < contador_jogador2:
            print("jogador 2 venceu")
        else:
            print("empate entre os jogadores")
        print("Muito obrigada por jogar - "
              "Créditos: Daniela e Letícia")
        break
    else:
        print("Insira uma opcão válida")
        final = int(input("digite a opção desejada:"))
        if final == 2:
            continue
        else:
            print("Jogador 1:", contador_jogador1, "vitória(s)")
            print("Jogador 2:", contador_jogador2, "vitória(s)")
            if contador_jogador1 > contador_jogador2:
                print("jogador 1 venceu")
            elif contador_jogador1 < contador_jogador2:
                print("jogador 2 venceu")
            else:
                print("empate entre os jogadores")
            print("Muito obrigada por jogar - "
                  "Créditos: Daniela e Letícia")
            break



#Modo 2 - humano X computador
contador_jogador = 0
contador_computador = 0
while modo == 2:
    print("Escolha uma opção: \n"
          "1 - pedra\n"
          "2 - papel\n"
          "3 - tesoura\n")
    jogador = int(input("digite a opção do jogador 1:"))
    computador = random.randint(1,3)
    print("computador:", computador)
    if jogador == computador:
        print("empate")
        print(contador_jogador, "X", contador_computador)
    elif (jogador == 1 and computador == 2) or (jogador == 2 and computador== 3) or (jogador == 3 and computador == 1):
        print("computador venceu")
        contador_computador += 1
        print(contador_jogador, "X", contador_computador)
    elif (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
        print("Jogador venceu")
        contador_jogador += 1
        print(contador_jogador, "X", contador_computador)
    else:
        print("Não está dentro das regras do jogo")
    print("OPÇÕES: 1 - finalizar o jogo, 2 - continuar jogando")
    final = int(input("digite a opção desejada:"))
    if final == 2:
        continue
    elif final == 1:
        print("Jogador :", contador_jogador, "vitória(s)")
        print("Computador:", contador_computador, "vitória(s)")
        if contador_jogador > contador_computador:
            print("jogador venceu")
        elif contador_jogador < contador_computador:
            print("computador venceu")
        else:
            print("empate")
        print("Muito obrigada por jogar - "
              "Créditos: Daniela e Letícia")
        break
    else:
        print("Insira uma opcão válida")
        final = int(input("digite a opção desejada:"))
        if final == 2:
            continue
        else:
            print("Jogador :", contador_jogador, "vitória(s)")
            print("Computador:", contador_computador, "vitória(s)")
            if contador_jogador > contador_computador:
                print("jogador venceu")
            elif contador_jogador < contador_computador:
                print("computador venceu")
            else:
                print("empate")
            print("Muito obrigada por jogar - "
                  "Créditos: Daniela Yuki")
            break

#Modo 3 - computador X computador
contador_computador1 = 0
contador_computador2 = 0
while modo == 3:
    print("Escolha uma opção:"
          "1 - pedra \n "
          "2 - papel \n "
          "3 - tesoura \n")
    computador1 = random.randint(1,3)
    computador2 = random.randint(1,3)
    print("computador 1:", computador1)
    print("computador 2:", computador2)
    if computador1 == computador2:
        print("empate")
        print(contador_computador1, "X", contador_computador2)
    elif (computador1 == 1 and computador2 == 2) or (computador1 == 2 and computador2 == 3) or (computador1 == 3 and computador2 == 1):
        print("computador 2 venceu")
        contador_computador2 += 1
        print(contador_computador1, "X", contador_computador2)
    elif (computador1 == 1 and computador2 == 3) or (computador1 == 2 and computador2 == 1) or (computador1 == 3 and computador2 == 2):
        print("computador 1 venceu")
        contador_computador1 += 1
        print(contador_computador1, "X", contador_computador2)
    else:
        print("Não está dentro das regras do jogo")
    print("OPÇÕES: 1 - finalizar o jogo, 2 - continuar jogando")
    final = int(input("digite a opção desejada:"))
    if final == 2:
        continue
    elif final == 1:
        print("Computador 1:", contador_computador1, "vitória(s)")
        print("Computador 2:", contador_computador2, "vitória(s)")
        if contador_computador1 > contador_computador2:
            print("computador 1 venceu")
        elif contador_computador1 < contador_computador2:
            print("computador 2 venceu")
        else:
            print("empate")
        print("Muito obrigada por jogar - "
              "Créditos: Daniela Yuki")
        break
    else:
        print("Insira uma opcão válida")
        final = int(input("digite a opção desejada:"))
        if final == 2:
            continue
        else:
            print("Computador 1:", contador_computador1, "vitória(s)")
            print("Computador 2:", contador_computador2, "vitória(s)")
            if contador_computador1 > contador_computador2:
                print("computador 1 venceu")
            elif contador_computador1 < contador_computador2:
                print("computador 2 venceu")
            else:
                print("empate")
            print("Muito obrigada por jogar - "
                    "Créditos: Daniela Yuki")
            break