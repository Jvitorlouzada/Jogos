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

        chute = input("Tente adivinhar uma letra: ")

        index = 0

        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra #Quando acertar, vai guardar a letra na LISTA
            index = index +1
        else:
            erros = erros + 1
        
        enforcou = erros == len(palavra_secreta)   
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Parabéns você ganhou!")
    else:
        print("Você perdeu.")

    print ("Fim do jogo!")

def mensagem_abertura():
    print("#######################################################")
    print("         Bem-vindo ao Jogo da forca\n")
    print("  Para ganhar, você precisa acertar a palavra")
    print("#######################################################\n")

def carregando_palavra():
    arquivo = open("frutas.txt", "r") # Abrindo arquivo.txt onde estão as frutas
    frutas = []
    
    # Aqui verifica linha por linha do aquivo.txt, limpa os espaços e os codigos como \n e coloca essa nova linha limpa na lista FRUTAS
    for linha in arquivo:  
        linha = linha.strip()
        frutas.append(linha)
    arquivo.close()
  
    fruta_aleatoria = random.randrange(0, len(frutas)) #gerando uma fruta aleatoria
    
    palavra_secreta = frutas[fruta_aleatoria].upper()
    return palavra_secreta



if (__name__ == "__main__"):
    jogar()