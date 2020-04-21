import random   

print("xxxxxxxxxx xxxxxxxxxxxxxxxxxxx xxxxxxxxxx")
print("xxxxxxxxxx JOGO ACERTAR NUMERO xxxxxxxxxx")
print("xxxxxxxxxx    VAMOS COMECAR    xxxxxxxxxx")

num_certo = random.randrange (1, 101)   
total_de_tentativas = 0
rodada  = 1
pontos = 1000

print("Qual nível de dificuldade ?")
print( " (1)-Facil  (2)-Médio  (3)-Difícil ")

nivel = int(input("Defina o nivel: "))

if (nivel==1):
    total_de_tentativas = 20
elif (nivel==2):
    total_de_tentativas = 10
else: 
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print(" Voce tem {} de {} tentativas".format(rodada,total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100: ')
            continue   

    acertou = chute == num_certo
    maior = chute > num_certo
    menor = chute < num_certo

    if (acertou):
        print('Você acertou o número secreto e fez {} pontos'.format(pontos))
        break
    else:
        if (maior):
            print('Você digitou número maior que o secreto')
        elif (menor): 
            print('Você digitou número menor que o secreto')
        pontos_perdidos = abs(num_certo -  chute) #40-20 diferença entre o numero certo e numero chutado funçao ABS faz que numero seja sempre positivo.
        pontos = pontos - pontos_perdidos

print("Fim do jogo")        