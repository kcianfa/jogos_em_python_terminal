import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    # numero_secreto = 42
    # numero_secreto = random.random() * 100 #random gera um numero entre 0.0 e 1.0
    numero_secreto = random.randrange(1,101)  # Opção para trazer numeros entre 1 e 100 
    #Gerar um número aleatório entre 1 e 100.
    numero_secreto = round(numero_secreto)
    total_de_tentativas = 0
    pontos = 1000
    rodada = 1
    print(numero_secreto)
    print("Qual o nível de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil ")

    nivel = int(input("Defina o nivel: ")) # o input vai retornar um valor para a variável e já estamos convertendo para inteiro

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5        

    if(nivel == 1):
        total_de_tentativas = 20


    # Usando sistema de loop com while
    # while (rodada <= total_de_tentativas ):
    #     print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    #     chute_str = input("Digite um número entre 1 e 100: ")
    #     print("Você digitou " , chute_str)
    #     chute = int(chute_str)

    #     if(chute < 1 or chute > 100):
    #         print("Você deve digitar um número entre 1 e 100!")
    #         continue

    #     acertou = chute == numero_secreto
    #     maior   = chute > numero_secreto
    #     menor   = chute < numero_secreto

    #     if(acertou):
    #         print("Você acertou!")
    #         break
    #     else:
    #         if(maior):
    #             print("Você errou! O seu chute foi maior do que o número secreto.")
    #         elif(menor):
    #             print("Você errou! O seu chute foi menor do que o número secreto.")

    #     rodada = rodada + 1       
    # print("Fim do jogo")


    # Usando sistema de loop com for
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute) #40-20 = 20 pts perdidos
                #para fazer um valor absoluto ignorando o sinal caso a conta seja 40-60
                pontos = pontos - pontos_perdidos
    print(f"O numero secreto era o {numero_secreto}")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()