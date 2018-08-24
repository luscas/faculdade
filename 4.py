from random import randint

class Jogo:
    # Multiplayer
    players   = []   # Players
    modo      = 1    # Solo ou Multiplayer
    nome      = None # Nome da pessoa
    chute     = 0    # Chute
    nivel     = 0    # Nivel escolhido
    tentativa = 0    # Total de tentativas restantes
    numero    = 0    # Numero secreto
    pontuacao = 100  # Pontuação
    posicao   = 0    # Posicao no ranking
    tentivas  = 0    # Total de tentativas por nivel

    def __init__(self):
        pass
        '''# Suporta -> Multiplayer
        self.modo = int(input('(1) Solo\n(2) Multiplayer\n'))

        if self.modo == 1:
            solo = input('Digite seu nome: ')

            self.players.append(solo)
        else:
            solo = input('Digite seu nome #1: ')
            duo  = input('Digite seu nome #2: ')

            self.players.append([solo, duo])

        print(self.players)'''

    # Começo
    def init(self):
        recordista = self.verifica_recordistas()

        print('***************************************')
        print('*** ADS 2018.1 - IFPI Campus Picos ****')
        print('************ Aluno: Lucas *************')

        if recordista:
            print('* Recorde de pontos atual: %s pontos *' % recordista[0][2])

        print('***************************************')
        self.nome = input('Qual é o seu nome?\n')
        self.nivel = int(input('''
Qual seu nível de dificuldade?
(1) Fácil
(2) Médio
(3) Difícil
Informe o nîvel: '''))

        self.filtro_nivel()

        self.numero = randint(1,100)
        self.chute  = int(input('Qual é o seu chute? (%s): ' % self.numero))

    # Recordistas
    # @return 0 -> posicao
    # @return 1 -> nome
    # @return 2 -> pontuacao
    def verifica_recordistas(self):
        # Comeca com a pontuacao anterior
        with open('recordistas.txt', 'r') as recordistas:
            recordistas = recordistas.read()
            recordistas = recordistas.splitlines()

        # Existe algum recordista?
        if recordistas:
            lista = []
            for i in range(len(recordistas)):
                lista.append(recordistas[i].split('='))

            posicao = 0
            retorno = []
            for x in range(len(lista)):
                posicao  += 1
                retorno.append([posicao, str(lista[x][0]), int(lista[x][1])])
            return retorno

    # Filtrar nivel
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

    # Adiciona no ranking
    def adiciona_ranking(self):
        arquivo = open('recordistas.txt', mode = 'w+')
        arquivo.write('%s=%s' % (self.nome, self.pontuacao))

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
                #print('%s seu chute foi %s' % (jogo.nome, jogo.chute)) # Mensagem

                acerto = (jogo.tentativas - jogo.tentativa)

                jogo.adiciona_ranking()

                print('Parabéns %s! Você acertou em %s tentativas' % (jogo.nome, acerto))

                # Mostra que o usuario é um recordista
                recordistas = jogo.verifica_recordistas()
                # Existe algum recordista?
                if recordistas and recordistas[0][1] == jogo.nome:
                    print('Você é o novo recordista de pontos com %s pontos.' % (recordistas[0][2]))
                else:
                    for x in range(len(recordistas)):
                        if recordistas[x][1] == jogo.nome:
                            print('Sua pontuação foi %d ficando abaixo do recorde atual que é de %d pontos' % (recordistas[x][2], recordistas[0][2]))

                # Mensagem final do jogo -> Sair ou Jogar novamente
                opcao = int(input('''************************************************
(0) - Sair
(1) - Jogar novamente
************************************************
'''))

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

                print('** %s você errou!, seu chute foi maior que o número secreto **' % jogo.nome)

                print('# Tentativa: %s' % jogo.tentativa)
                jogo.chute = int(input('Qual é o seu chute? (%s): ' % jogo.numero))

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