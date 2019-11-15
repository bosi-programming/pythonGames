import random


def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    # numero_secreto = round(random.random() * 100)
    #  gera um número entre 0.0 e 1.0

    numero_secreto = random.randrange(1, 101)

    # gera um número entre dois valores escolhidos e
    # pode escolher um pulo como um terceiro valor
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina um nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        # O usos de {} junto com a função format avisa para o Python que eu
        # quero substituir os {} pelos valores dentro do format()
        # Também podemos inverter a ordem de uso dos parâmetros do format ao
        # usar valores de índice dentro do {}, {1} e {0}

        chute = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute)
        numero = int(chute)

        if(numero < 1 or numero > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue  # Continua o laço, pulando para a próxima interação

        acertou = numero_secreto == numero
        maior = numero_secreto < numero
        menor = numero_secreto > numero

        if (acertou):
            print("Você acertou e fez {}!".format(pontos))
            break  # Sai de um laço antes dele terminar
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto")
                if(rodada == total_de_tentativas):
                    text_in1 = "O número secreto era {}".format(numero_secreto)
                    print(text_in1 + ". Você fez {} pontos".format(pontos))
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto")
                if(rodada == total_de_tentativas):
                    text_in1 = "O número secreto era {}".format(numero_secreto)
                    print("Você fez {} pontos".format(pontos))
            pontos_perdidos = abs(numero_secreto - numero)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()
