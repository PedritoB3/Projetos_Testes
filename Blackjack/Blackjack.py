import random

def cartas():
    return random.randrange(1, 11)

def main():
    player1 = 0
    player2 = 0

    while True:
        escolha = input("\nPlayer 1, Gostaria de pedir ou parar?: ").lower()

        if escolha == "pedir":
            player1 += cartas()
            print(f"Player1 = {player1}")

        escolha2 = input("\nPlayer 2, Gostaria de pedir ou parar?: ").lower()

        if escolha2 == "pedir":
            player2 += cartas()
            print(f"Player2 = {player2}")

        if escolha == "parar":
            if escolha2 == "parar":
                break



    diferenca = abs(player1 - player2)

    if player1 > player2:
        print(f"A pontuação do player 1 foi equivalente a 21, com diferença de {diferenca} pontos do player 2")
    elif player2 > player1:
        print(f"A pontuação do player 2 foi equivalente a 21, com diferença de {diferenca} pontos do player 1")


if __name__ == '__main__':
    main()

