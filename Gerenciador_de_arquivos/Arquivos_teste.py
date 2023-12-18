import os


def diretorio():
    print(os.getcwd())

def remover_arquivo(arquivo):
    os.remove(arquivo)

def criar_arquivo(arquivo, tipo):
    # Aqui você cria uma variavel f que cria um arquivo e armazena
    with open(f"{arquivo}.{tipo}", mode='w', encoding='utf-8') as f:
        # Aqui você digita o conteudo do arquivo
        f.write(input("Agora coloque o conteudo do arquivo: "))


def abrir_arquivo(arquivo):
    with open(arquivo, mode='r', encoding='utf-8') as f:
        print(f.read())


def main():
    print("Bem-vindo ao pequeno gerenciador de arquivos, do que você gostaria?")
    print('''
    0-Sair.
    1-criar arquivo.
    2-abrir arquivo.
    3-deletar arquivo.
    4-mostrar diretorio atual
    ''')

    while True:
        escolha = int(input("Escolha a numeração:"))
        if escolha == 1:
            # Aqui você faz a criação do arquivo
            arquivo = input("Nomeie o arquivo:")
            tipo = input("Escolha o tipo de arquivo, como txt,py,etc:")
            # Logo após os dois input, você coloca o conteudo dentro do arquivo.
            criar_arquivo(arquivo, tipo)
            print(f"Arquivo criado")


        if escolha == 2:
            print("Escolha um arquivo que você quer ler no estilo C:/Python33/README.TXT:")
            arquivo = input()
            abrir_arquivo(arquivo)


        if escolha == 3:
            print("Escolha o arquivo que você deseja deletar:")
            arquivo = input()
            remover_arquivo(arquivo)


        if escolha == 4:
            print("Este é o seu diretorio atual:")
            diretorio()

        print("Deseja continuar no gerenciador, S ou N? ")
        escolha = input()
        if escolha in ("S", "s", "Sim", "sim"):
            continue
        elif escolha in ("N", "n", "Não", "nâo"):
            break

        else:
            break



if __name__ == "__main__":
    main()
