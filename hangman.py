import random
from re import U

def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    #variaveis
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    #laço com condiçao de parada ou continuidade
    while(not enforcou and not acertou):
           chute = pede_chute()

           if (chute in palavra_secreta):
                marca_chute_correto(chute, letras_acertadas, palavra_secreta)
           else:
               erros = erros + 1 
               desenha_forca(erros)
                
        

           acertou = "_" not in letras_acertadas
           enforcou = erros == 6
    if(acertou):
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)    

    print("fim de jogo")  


def imprime_mensagem_abertura():
    print("##################################")
    print("Bem Vindo ao jogo  de advinhação!")
    print("##################################")
#slseciona a palavra secreta do arquivo txt
def carrega_palavra_secreta():
    arquivo = open("palavras.txt")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()        
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta
#retorna um caracter secreto para cada letra da palavra
def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]
#pedir o chute do usuario
def pede_chute():
    chute = input("qual letra?")
    chute = chute.strip().upper()    
    return chute
#verificar se o chute esta correto
def marca_chute_correto(chute, letras_acertadas, palavra_secreta ):
    index = 0
    for letra in palavra_secreta:
            if (chute == letra):
                 letras_acertadas[index] = letra
            index = index + 1
    print(letras_acertadas)

def mensagem_perdedor(palavra_secreta):
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

def mensagem_vencedor():
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

