import random
from time import sleep

'''
Aluno: Michelle Goncalves
Curso: Tecnologia em Análise e Desenvolvimento de Sistemas
Matéria: Raciocínio Computacional (11100010563_20221_01)
Projeto da Disciplina: Implementação digital do jogo de tabuleiro Zombie Dice
Situação atual: 15% concluído
'''


def linhas():
    print(40 * '-')


linhas()
print(3 * ' ', 'ZUMBIE DICE (Prototipo Semana 4)')
linhas()
print(2 * ' ', 'Seja bem-vindo ao jogo Zombie Dice!')
linhas()

print('INTRODUCAO: Eh necessario pelo menos 2 jogadores e no maximo 8.\n'
      'Vence quem fizer 13 pontos, todos devem ter jogado, se houver empate, estes jogarao mais uma rodada!\n'
      'Na sua rodada pegue 3 dados aleatorios e jogue-os.\n'
      'Voce pode optar por continuar jogango mas se levar 3 tiros, esta fora e perde seus pontos!\n'
      'Caso continue jogando, seus tiros serao acumulados ate morrer, dados que tirar Passos serao jogados novamente.\n'
      'Ao parar, seus cerebros serao contabilizados aos seus pontos.\n'
      '')

linhas()

# Quantidade de jogadores
numJogadores = 0
while numJogadores < 2:
    print('Informe o numero de jogadores para iniciar a partida! ')
    numJogadores = int(input('Numero de jogadores: '))
    if numJogadores < 2:
        print('Adicione ao menos mais um jogador!')

linhas()
print(f'Agora vamos contunuar ja que temos {numJogadores} jogadores.')

# Lista de Jogadores
listaJogadores = []
for i in range(0, numJogadores):
    listaJogadores.append(str(input("Informe o nome do jogador " + str(i + 1) + ": ")))

print(f"Os jogadores sao {listaJogadores}")

sleep(2)

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

# verificar jogador atual - numero?
jogadorAtual = 0
dadosSorteados = []
tiros = 0
cerebros = 0
passos = 0

while True:
    print("TURNO DO JOGADOR", listaJogadores[jogadorAtual])
    for i in range(0, 3, 1):
        numSorteado = random.randint(0, 12)
        dadoSorteado = listaDados[numSorteado]

        if dadoSorteado == "CPCTPC":
            corDado = "VERDE"
        elif dadoSorteado == "TPCTPC":
            corDado = "AMARELO"
        else:
            corDado = "VERMELHO"
        print(f"Dado sorteado: {corDado}")

    for dadoSorteado in dadosSorteados:
        numFaceDado = random.choice(0, 5)

        if dadoSorteado[numFaceDado] == "C":
            print("CEREBROOO (Voce comeu um cerebro)")
            cerebros += 1
        elif dadosSorteados[numFaceDado] == "T":
            print("POW POW (Voce levou um tiro!)")
            tiros += 1
        else:
            print("PASSOS (Sua vitima fugiu...)")
            passos += 1

    score_atual = []
    score_atual += cerebros
    print(f"SCORE ATUAL: {score_atual}")
    print(f"CEREBROS: {cerebros}")
    print(f"TIROS: {tiros}")

    continuarTurno = str(input("AVISO: Voce deseja continuar jogando os dados? (s=sim / n=nao)")).lower()
    if continuarTurno == "n":
        jogadorAtual += 1
        dadoSorteado = []
        tiros = 0
        cerebros = 0
        passos = 0

        if jogadorAtual == len(listaJogadores):
            print("Finalizando prototipo do jogo...")
            break

        else:
            print("Iniciando mais uma rodada, se preparem!")

            sleep(2)

            dadosSorteados = []
        continue
    pass
