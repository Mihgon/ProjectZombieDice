import random
from time import sleep

'''
Aluno: Michelle Gonçalves
Curso: Tecnologia em Análise e Desenvolvimento de Sistemas
Matéria: Raciocínio Computacional (11100010563_20221_01)
Projeto da Disciplina: Implementação digital do jogo de tabuleiro Zombie Dice
'''


def linhas():
    print(40 * '-')


linhas()
print(3 * ' ', 'ZUMBIE DICE (Protótipo Semana 4)')
linhas()
print(2 * ' ', 'Seja bem-vindo ao jogo Zombie Dice!')
linhas()

# Quantidade de jogadores
numJogadores = 0
while numJogadores < 2:
    print('Informe o número de jogadores para iniciar a partida! ')
    numJogadores = int(input('Número de jogadores: '))
    if numJogadores < 2:
        print('Adicione ao menos mais um jogador!')

linhas()
print(f'Agora vamos continuar, visto que temos {numJogadores} jogadores.')
linhas()

# Lista de Jogadores
listaJogadores = []
for i in range(numJogadores):
    nome = (str(input("Informe o nome do jogador " + str(i + 1) + ": "))).strip()
    listaJogadores.append(nome)
# Iniciar jogo
print(f"Os jogadores são {listaJogadores}.")
linhas()
sleep(2)
comecar = ()
print("Hora de começar esse jogo! Vamos inciar?")
while comecar != "S":
    comecar = str(input("Pressione 'S' para Sim: ")).strip().upper()
else:
    linhas()
    print(7 * ' ', "Que comecem os jogos!!!")
    linhas()

# Lista de dados
dadoVerde = "CPCTPC"
dadoAmarelo = "TPCTPC"
dadoVermelho = "TPTCPT"

listaDados = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
              dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
              dadoVermelho, dadoVermelho, dadoVermelho]

# Pontuação
dadosSorteados = []
jogadorAtual = 0
tiros = 0
cerebros = 0
passos = 0

# Sorteio de dados e jogador a iniciar partida
while True:
    dadosSorteados = []
    print("TURNO DO(A) JOGADOR(A): ", listaJogadores[jogadorAtual])
    for i in range(0, 3, 1):
        numSorteado = random.randint(0, 12)
        dadoSorteado = listaDados[numSorteado]
        dadosSorteados.append(dadoSorteado)
        if dadoSorteado == "CPCTPC":
            corDado = "VERDE"
        elif dadoSorteado == "TPCTPC":
            corDado = "AMARELO"
        else:
            corDado = "VERMELHO"
        print(f"Dado sorteado: {corDado}")
    linhas()
    sleep(2)
    for dadoSorteado in dadosSorteados:
        numFaceDado = random.randint(0, 5)
        numFaceDadoFim = numFaceDado + 1

        if dadoSorteado[numFaceDado] == "C":
            print("CEREBROOO (Você comeu um cerebro)")
            cerebros += 1
        elif dadoSorteado[numFaceDado] == "T":
            print("POW POW (Voce levou um tiro!)")
            tiros += 1
        else:
            print("PASSOS (Sua vitima fugiu...)")
            passos += 1
    linhas()
    sleep(3)
    print("SCORE ATUAL")
    print(f"CEREBROS: {cerebros}")
    print(f"TIROS: {tiros}")
    print(f"PASSOS: {passos}")
# Pergunta para continuar jogando e zerar pontuação
    continuarTurno = str(input("AVISO: Você deseja continuar jogando os dados? (s=sim / n=nao)")).lower().strip()
    if continuarTurno == "n":
        jogadorAtual += 1
        dadosSorteados = []
        tiros = 0
        cerebros = 0
        passos = 0
        if jogadorAtual == len(listaJogadores):
            print("Finalizando protótipo do jogo...")
            break

        else:
            print("Iniciando mais uma rodada, se preparem!")

            sleep(2)

            dadosSorteados = []
        continue
    pass
