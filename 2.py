from random import randint

class Jogo:
    nome      = None
    chute     = None
    nivel     = 0
    tentativa = 1
    numero    = 0
    pontuacao = 100
    total_ten = 0

    def bem_vindo(self):
        print('************************************')
        print('** ADS 2018.1 - IFPI Campus Picos **')
        print('****** Aluno: %s ******' % self.nome)
        print('* Bem vindo ao Jogo de Adivinhação *')
        print('************************************')

    def filtro_nivel(self):
        if self.nivel == 1:
            self.tentativa = 10
            self.total_ten = 10
        elif self.nivel == 2:
            self.tentativa = 5
            self.total_ten = 5
        elif self.nivel == 3:
            self.tentativa = 4
            self.total_ten = 4

    def retira_tentativa(self):
        if self.nivel == 1: # Facil
            self.tentativa -= 1
            self.pontuacao -= 10
        elif self.nivel == 2: # Medio
            self.tentativa -= 1
            self.pontuacao -= 20
        elif self.nivel == 3: # Dificil
            self.tentativa -= 1
            self.pontuacao -= 25

    def final_jogo(self):
        self.nome = input('Qual é o seu nome?\n')
        self.bem_vindo()
        self.nivel = int(input("Qual seu nível de dificuldade? \n(1) Fácil (2) Médio (3) Difícil \nInforme o nîvel\n"))
        self.filtro_nivel()
        self.numero = randint(0,100)
        self.chute  = int(input('Qual é o seu chute? %s \n' % self.numero))

jogo = Jogo()

jogo.final_jogo()

continua  = True

opcao = None

recordistas = open('recordistas.txt', 'r')
recordistas = recordistas.read()

while continua:
    if jogo.tentativa > 0:
        if jogo.chute >= 0:
            if jogo.chute == jogo.numero:
                print('%s seu chute foi %s' % (jogo.nome, jogo.chute))

                acerto = (jogo.total_ten - jogo.tentativa)

                print('Parabéns %s! Você acertou em %s tentativas' % (jogo.nome, acerto))

                print("***********************************************************")
                opcao = int(input("0 - Sair \n1 - Jogar novamente\n"))
                print("***********************************************************")

                if opcao == 1:
                    opcao = None
                    jogo.final_jogo()
                else:
                    continua = False

            elif jogo.chute > jogo.numero:
                print('%s seu chute foi %s' % (jogo.nome, jogo.chute))

                jogo.retira_tentativa()

                print('%s você errou!, seu chute foi maior que o número secreto' % jogo.nome)

                print('Tentativa %s' % jogo.tentativa)
                jogo.chute = int(input('Qual é o seu chute? %s \n' % jogo.numero))
            elif jogo.numero > jogo.chute:
                print('%s seu chute foi %s' % (jogo.nome, jogo.chute))

                print('%s você errou!, seu chute foi menor que o número secreto' % jogo.nome)

                jogo.retira_tentativa()

                print('Tentativa %s' % jogo.tentativa)
                jogo.chute = int(input('Qual é o seu chute? %s \n' % jogo.numero))
        else:
            print('%s seu chute foi %s' % (jogo.nome, jogo.chute))
            print("%s você não pode chutar números negativos." % jogo.nome)
            jogo.chute = int(input('Qual é o seu chute? %s \n' % jogo.numero))
    else:
        print("***********************************************************")
        opcao = int(input("0 - Sair \n1 - Jogar novamente\n"))
        print("***********************************************************")

        if opcao == 1:
            opcao = None
            jogo.final_jogo()
        else:
            continua = False