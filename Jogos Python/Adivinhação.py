import os
import random

def limpar_tela():
    os.system('cls')

def jogar():
    print("#######################################################")
    print("         Bem-vindo ao Jogo de adivinhação\n")
    print("  Para ganhar, você precisa acertar o número secreto")
    print("#######################################################\n")

    jogar_novamente = True  # Variável de controle para continuar jogando

    while jogar_novamente:
        print("Olá, prazer em conhecer, qual seu nome?")
        nome = input("Digite seu nome: ")

        print("Agora você precisa escolher um nível:")
        print("1 - Fácil")
        print("2 - Médio")
        print("3 - Difícil")
        nivel = int(input("Digite o número correspondente ao nível desejado: "))

        if nivel not in [1, 2, 3]:
            print("Nível inválido. Escolha um nível válido (1, 2 ou 3).")
            continue

        if nivel == 1:
            numero_secreto = random.randint(1, 10)
            Tentativas = 5
        elif nivel == 2:
            numero_secreto = random.randint(1, 50)
            Tentativas = 5
        elif nivel == 3:
            numero_secreto = random.randint(1, 100)
            Tentativas = 5

        while Tentativas > 0:
            print("Você tem", Tentativas, "tentativas")
            chute = int(input("Digite um número entre 1 e {}: ".format(10 if nivel == 1 else (50 if nivel == 2 else 100))))

            if chute < 1 or chute > (10 if nivel == 1 else (50 if nivel == 2 else 100)):
                print("\nVocê deve digitar um número entre 1 e {}.".format(10 if nivel == 1 else (50 if nivel == 2 else 100)))
                Tentativas = Tentativas - 1
                continue

            Acertou     = chute == numero_secreto
            Chute_Maior = chute >  numero_secreto
            Chute_Menor = chute <  numero_secreto

            if Acertou:
                print("Parabéns,", nome, "você acertou!")
                break
            else:
                if Chute_Maior:
                    print(nome, "o seu chute foi maior que o número secreto")
                elif Chute_Menor:
                    print(nome, "o seu chute foi menor que o número secreto")

            Tentativas = Tentativas - 1

        print("\nFim do jogo")
        print("O número correto era:", numero_secreto)
        resposta = input("Deseja jogar novamente? (S para sim, qualquer tecla para sair): ")
        if resposta == "s":
            limpar_tela()
            os.system('cls')
        elif resposta.lower() != 's':
            jogar_novamente = False

if __name__ == "__main__":
    jogar()