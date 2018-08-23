from random import randint

# Marciely e Lucas

class Jogo:
    nome      = None # Nome da pessoa
    chute     = 0    # Chute
    nivel     = 0    # Nivel escolhido
    tentativa = 0    # Total de tentativas restantes
    numero    = 0    # Numero secreto
    pontuacao = 100  # Pontuação
    tentivas  = 0    # Total de tentativas por nivel

    # Começo
    def init(self):
        self.nome = input('Qual é o seu nome?\n')

        print('************************************')
        print('** ADS 2018.1 - IFPI Campus Picos **')
        print('****** Aluno: %s ******' % self.nome)
        print('* Bem vindo ao Jogo de Adivinhação *')
        print('************************************')

        self.nivel = int(input("Qual seu nível de dificuldade? \n(1) Fácil (2) Médio (3) Difícil \nInforme o nîvel\n"))

        self.filtro_nivel()

        self.numero = randint(0,100)
        self.chute  = int(input('Qual é o seu chute? %s \n' % self.numero))

    def filtro_nivel(self):
        if self.nivel == 1: # Facil
            self.tentativa  = 10
            self.tentativas = 10
        elif self.nivel == 2: # Medio
            self.tentativa  = 5
            self.tentativas = 5
        elif self.nivel == 3: # Dificil
            self.tentativa  = 4
            self.tentativas = 4

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

jogo = Jogo()

jogo.init()

opcao = None

while True:
    # Se o usuario tiver ainda tentativas -> Continua
    # Caso nao tenha mais nenhuma tentativa -> Mensagem com opcao de Sair ou Recomeçar o jogo
    if jogo.tentativa > 0:
        # Se o chute for maior do que 0 -> Continua
        # Caso seja menor que 0 -> Considerar como numero negativo -> Nao passarao
        if jogo.chute >= 0:
            # Se eu acertei o numero secreto -> Mensagem dizendo que eu acertei ne papai
            if jogo.chute == jogo.numero:
                print('%s seu chute foi %s' % (jogo.nome, jogo.chute)) # Mensagem

                acerto = (jogo.tentativas - jogo.tentativa)

                print('Parabéns %s! Você acertou em %s tentativas' % (jogo.nome, acerto))

                # Mensagem final do jogo -> Sair ou Jogar novamente
                print("***********************************************************")
                opcao = int(input("0 - Sair \n1 - Jogar novamente\n"))
                print("***********************************************************")

                # Jogar novamente
                if opcao == 1:
                    opcao = None
                    jogo.init()
                else: # Sair
                    break

            # Mostra mensagem -> chute X é maior que o numero secreto
            elif jogo.chute > jogo.numero:
                print('%s seu chute foi %s' % (jogo.nome, jogo.chute))

                jogo.retira_tentativa()

                print('%s você errou!, seu chute foi maior que o número secreto' % jogo.nome)

                print('Tentativa %s' % jogo.tentativa)
                jogo.chute = int(input('Qual é o seu chute? %s \n' % jogo.numero))

            # Se o chute que eu dei for menor que o numero secreto -> mensagem
            elif jogo.chute < jogo.numero:
                print('%s seu chute foi %s' % (jogo.nome, jogo.chute))

                print('%s você errou!, seu chute foi menor que o número secreto' % jogo.nome)

                jogo.retira_tentativa()

                print('Tentativa %s' % jogo.tentativa)
                jogo.chute = int(input('Qual é o seu chute? %s \n' % jogo.numero))

        else: # Caso o usuario digite um numero negativo
            print('%s seu chute foi %s' % (jogo.nome, jogo.chute))
            print("%s você não pode chutar números negativos." % jogo.nome)
            jogo.chute = int(input('Qual é o seu chute? %s \n' % jogo.numero))

    else: # Caso o usuario nao tenha mais tentativas
        print("***********************************************************")
        opcao = int(input("0 - Sair \n1 - Jogar novamente\n"))
        print("***********************************************************")

        # Jogar novamente
        if opcao == 1:
            opcao = None
            jogo.init()
        else: # Sair
            break