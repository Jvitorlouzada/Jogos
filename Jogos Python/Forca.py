import random

def jogar():

    mensagem_abertura()
    palavra_secreta = carregando_palavra()

    letras_acertadas = ["_" for letra in palavra_secreta] # Adicionando _ para cada letra da palavra

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou): # Enquanto não enforcar e não acertar continua.

        chute_minusculo = input("Tente adivinhar uma letra: ")
        chute = chute_minusculo.upper()

        if (chute in palavra_secreta):    
            chute_correto(chute,palavra_secreta,letras_acertadas)
        else:
            erros = erros + 1
            desenha_forca(erros)

        enforcou = erros == 7 
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print ("Fim do jogo!")

def mensagem_abertura():
    print("#######################################################")
    print("         Bem-vindo ao Jogo da forca\n")
    print("  Para ganhar, você precisa acertar a palavra")
    print("#######################################################\n")
    print("            Dica: é uma fruta")

def carregando_palavra():
    frutas = [
        "Abacate", "Abacaxi", "Açaí", "Acerola", "Ameixa", "Amora", "Atemoia", "Banana",
        "Caju", "Cambuci", "Carambola", "Cereja", "Coco", "Figo", "Framboesa", "Goiaba",
        "Jabuticaba", "Jaca", "Kiwi", "Laranja", "Maça", "Mamao", "Manga", "Melancia",
        "Melao", "Mexerica", "Morango", "Pessego", "Pitaia", "Uva"
    ]

    fruta_aleatoria = random.choice(frutas) #gerando uma fruta aleatoria
    
    palavra_secreta = fruta_aleatoria.upper()
    return palavra_secreta

def chute_correto(chute,palavra_secreta,letras_acertadas):
    index = 0
    for letra in palavra_secreta:    
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra #Quando acertar, vai guardar a letra na LISTA
        index = index +1

def imprime_mensagem_vencedor():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
  

def desenha_forca(erros):
        print("  _______     ")
        print(" |/      |    ")

        if(erros == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if(erros == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if(erros == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if(erros == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if(erros == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if(erros == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (erros == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

if (__name__ == "__main__"):
    jogar()