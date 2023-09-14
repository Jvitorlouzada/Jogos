import Forca
import Adivinhação

def escolha_jogo():
    print("#######################################################")
    print("         Qual jogo você quer jogar?\n")
    print("#######################################################\n")

    print("1- Adivinhação\n")
    print("2- Forca\n")

    jogo = int(input("Qual jogo?"))

    if 1==jogo:
        print("Bem vindo ao jogo da Adivinhação")
        Adivinhação.jogar()
    elif 2==jogo:
        print("Bem vindo ao jogo da Forca")    
        Forca.jogar()

if __name__ == "__main__":
    escolha_jogo()
