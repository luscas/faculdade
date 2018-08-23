from random import randint

nome      = input('Qual é o seu nome?\n')

print('************************************')
print('** ADS 2018.1 - IFPI Campus Picos **')
print('****** Aluno: %s ******' % nome)
print('* Bem vindo ao Jogo de Adivinhação *')
print('************************************')

numero    = randint(0,100)
chute     = int(input('Qual é o seu chute? %s \n' % numero))
tentativa = 1
continua  = True

while continua:
    if chute == numero:
        print('Parabéns %s! Você acertou!' % nome)
        continua = False
    else:
        print('%s Você errou!, Tente novamente' % nome)
        tentativa += 1
        chute      = int(input('Qual é o seu chute? %s \n' % numero))

    # Regras do jogo
    if tentativa == 5:
        print("Game Over! %s suas chances acabaram!" % nome)
        continua = False