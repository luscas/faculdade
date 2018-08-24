from random import randint

class Jogo:
	# Multiplayer
	continua         = True
	players          = []          # Players
	chute            = 0           # Chute
	tentativas       = [0,0]       # Total de tentativas restantes
	nivel_tentativas = 0           # Total de tentativas por nivel
	pontuacao        = [100, 100]  # Pontuação
	posicao          = [0, 0]      # Posicao no ranking

	jogando          = 0           # Player que está jogando agora #1
	nivel            = 0           # Nivel escolhido
	numero           = 0           # Numero secreto
	opcao            = None        # Opção - Final do jogo

	# Começo
	def start(self):
		recordista = self.verifica_recordistas()

		print('***************************************')
		print('*** ADS 2018.1 - IFPI Campus Picos ****')
		print('************ Aluno: Lucas *************')

		if recordista:
			print('* Recorde de pontos atual: %s pontos *' % recordista[0][2])

		print('***************************************')

		solo = input('Digite seu nome #1: ')
		duo  = input('Digite seu nome #2: ')

		self.players.append(solo)
		self.players.append(duo)

		self.nivel = int(input('''
Qual seu nível de dificuldade?
(1) Fácil
(2) Médio
(3) Difícil
Informe o nível: '''))

		self.filtro_nivel()

		self.numero = randint(1,100)

		self.chute  = int(input('%s, qual é o seu chute? (%s): ' % (self.players[self.jogando], self.numero) ))

	# Alterna chutes
	def alterna_chutes(self):
		if self.jogando == 0: # Jogador #1
			self.jogando = 1 # Jogador #2
		else:
			self.jogando = 0

		self.chute  = int(input('%s, qual é o seu chute? (%s): ' % (self.players[self.jogando], self.numero) ))

	# Filtro Nivel
	# Define o número de tentativas de cada usuário
	def filtro_nivel(self):
		if self.nivel == 1: # Facil
			self.tentativas[0] = 10    # Cada usuário possui x tentativas
			self.tentativas[1] = 10    # Cada usuário possui x tentativas
			self.nivel_tentativas = 10 # Enquanto cada usuário perde, criamos uma variavel para guardar o total de tentativas por nivel

		elif self.nivel == 2: # Medio
			self.tentativas[0]    = 5  # Cada usuário possui x tentativas
			self.tentativas[1]    = 5  # Cada usuário possui x tentativas
			self.nivel_tentativas = 5  # Enquanto cada usuário perde, criamos uma variavel para guardar o total de tentativas por nivel

		elif self.nivel == 3: # Dificil
			self.tentativas[0]    = 4  # Cada usuário possui x tentativas
			self.tentativas[1]    = 4  # Cada usuário possui x tentativas
			self.nivel_tentativas = 4  # Enquanto cada usuário perde, criamos uma variavel para guardar o total de tentativas por nivel

	# Retira Tentativa
	# Remove tentativas de cada usuário
	def retira_tentativa(self):
		# Todos perdem 1 tentativas quando erra o número secreto
		self.tentativas[self.jogando] -= 1  # Remove tentativas do usuario[x]

		if self.nivel == 1: # Facil
			self.pontuacao[self.jogando]  -= 10 # Remove pontuação do usuario[x]
		elif self.nivel == 2: # Medio
			self.pontuacao[self.jogando]  -= 20 # Remove pontuação do usuario[x]
		elif self.nivel == 3: # Dificil
			self.pontuacao[self.jogando]  -= 25 # Remove pontuação do usuario[x]

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

	# Adiciona Ranking
	# Adiciona o usuário no ranking de recordistas
	def adiciona_ranking(self):
		arquivo = open('recordistas.txt', mode = 'w+')
		arquivo.write('%s=%s' % (self.players[self.jogando], self.pontuacao[self.jogando]))

	def end(self):
		print('***********************************************************')
		print('RANKING DE PONTOS')
		print('***********************************************************')

		for x in range(len(self.verifica_recordistas())):
			print('%sº - %s com %s pontos' % (self.verifica_recordistas()[x][0], self.verifica_recordistas()[x][1], self.verifica_recordistas()[x][2]))

		self.opcao = int(input('''************************************************
(0) - Sair
(1) - Jogar novamente
************************************************
'''))
		# Jogar novamente
		if self.opcao == 1:
			self.opcao = None
			self.start()
		else: # Sair
			self.continua = False


jogo = Jogo()

jogo.start()

opcao = None

while jogo.continua:
	# Fim do jogo
	if jogo.tentativas[0] == 0 and jogo.tentativas[1] == 0:
		jogo.end()
	else:
		# Se o chute for maior do que 0 -> Continua
		# Caso seja menor que 0 -> Considerar como numero negativo -> Nao passarao
		if jogo.chute >= 0:
			# Se eu acertei o numero secreto -> Mensagem dizendo que eu acertei ne papai
			if jogo.chute == jogo.numero:
				acerto = (jogo.tentativas[jogo.jogando] - jogo.nivel_tentativas)

				jogo.adiciona_ranking()

				print('***********************************************************')
				print('Parabéns %s! Você acertou em %s tentativas.' % (jogo.players[jogo.jogando], acerto))

				# Mostra que o usuario é um recordista
				recordistas = jogo.verifica_recordistas()
				# Existe algum recordista?
				if recordistas and recordistas[0][1] == jogo.players[jogo.jogando]:
					print('Você é o novo recordista de pontos com %s pontos.' % (recordistas[0][2]))
				else:
					for x in range(len(recordistas)):
						if recordistas[x][1] == jogo.players[jogo.jogando]:
							print('Sua pontuação foi %d ficando abaixo do recorde atual que é de %d pontos' % (recordistas[x][2], recordistas[0][2]))

				jogo.end()

			# Mostra mensagem -> chute X é maior que o numero secreto
			if jogo.chute > jogo.numero:
				print('%s seu chute foi %s' % (jogo.players[jogo.jogando], jogo.chute))
				print('** %s você errou!, seu chute foi maior que o número secreto **' % jogo.players[jogo.jogando])
				jogo.retira_tentativa()
				print('# Tentativa: %s' % jogo.tentativas[jogo.jogando])
				jogo.alterna_chutes()

			# Se o chute que eu dei for menor que o numero secreto -> mensagem
			elif jogo.chute < jogo.numero:
				print('%s seu chute foi %s' % (jogo.players[jogo.jogando], jogo.chute))
				print('%s você errou!, seu chute foi menor que o número secreto' % jogo.players[jogo.jogando])
				jogo.retira_tentativa()
				print('# Tentativa: %s' % jogo.tentativas[jogo.jogando])
				jogo.alterna_chutes()

		else: # Caso o usuario digite um numero negativo
			print('%s seu chute foi %s' % (jogo.players[jogo.jogando], jogo.chute))
			print("%s você não pode chutar números negativos." % jogo.players[jogo.jogando])
			jogo.chute = int(input('%s, qual é o seu chute? (%s): ' % (jogo.players[jogo.jogando], jogo.numero) ))