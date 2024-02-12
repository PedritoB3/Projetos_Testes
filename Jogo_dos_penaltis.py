import random

def defesa():
    return random.randrange(1,4)
def goleiro():
    acertos = 0
    chutes_restantes = 5

    for i in range(5):
        goleiro = defesa()

        print(f'Voce tem {chutes_restantes} restamtes')

        chute = int(input("Vai chutar em qual entrada?\n 1 2 3\n"))


        if chute == goleiro:
            print("O goleiro bloqueoou!!!")
        elif chute > 3 or chute < 1:
            print("Na trave!!!")
        else:
            print("O chute entrou!!!")
            acertos += 1

        chutes_restantes -= 1

    if acertos >= 3:
        return "\nVoce ganhou"
    else:
        return "\nVoce perdeu"


def main():
    print("Jogo dos penaltis, escolha a area do numero e chute.\n")

    print(goleiro())



if __name__ == '__main__':
            main()