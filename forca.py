import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    # palavra.capitalize() nada mais é que do que um formatador da string, deixa a visualização da nossa palavra banana em Banana
    # palavra.endswith("na") retorna True, afinal banana termina com na. 

    # palavra_secreta = "banana".upper()  #para deixar todas as letras maiúsculas
    # letras_acertadas = ["_","_","_","_","_","_"]

    #tornando a palavra secreta dinamica
    palavra_secreta = "maça".upper()
    letras_acertadas = ["_" for letra in palavra_secreta] #nome da funcionalidade para adicionar "_" a palavra secreta: "List Comprehensions"

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    # not é usado como forma de negação 
    # enquanto TRUE and TRUE - não falso e não falso 
    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper() #stript é responsável por fazer uma limpeza, por exemplo, removendo os espaços

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    # print("Encontrei a letra {} na posicao {}".format(letra,index))
                    # se acertar a letra, vou sobreescrever, guardar a letra dentro de letra acertada
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6 #verificando se o usuário já errou 6 vezes. Se já, para o jogo
        acertou = "_" not in letras_acertadas # tratamento para validar apenas que acertou quando não houver mais "_" em letras_acertadas
        print(letras_acertadas)

        # find = palavra_secreta.find("b"); nesse caso vai retornar 0 que é a posição em que a letra b se encontra
        # lower = palavra_secreta.lower() pega todas as palavras da string e as transforma em letra minuscula.
        # upper = palavra_secreta.upper() pega todas as palavras da string e as transforma em letra maiúcula.
        # strip = palavra_secreta.strip() retorna a palavra sem os espaços.

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")


    print("Fim do jogo")
    # Tudo que está identado significa que pertence a função.

# se houver a necessidade de jogar esse jogo sem antes passar pelo arquivo jogos de escolha, essa função autoriza que o jogo da forca seja jogado mesmo assim
if(__name__ == "__main__"):
    jogar()