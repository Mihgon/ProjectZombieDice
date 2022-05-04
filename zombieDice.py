'''
Aluno: Michelle Gonçalves
Curso: Tecnologia em Análise e Desenvolvimento de Sistemas
Matéria: Raciocínio Computacional (11100010563_20221_01)
Projeto da Disciplina: Implementação digital do jogo de tabuleiro Zombie Dice
'''

import random
from random import shuffle


def linhas():
    """Função que retorna uma linha pré definida."""

    print(40 * '-')


linhas()
print(13 * ' ', 'ZUMBIE DICE')
linhas()
print(2 * ' ', 'Seja bem-vindo ao jogo Zombie Dice!')
linhas()


class criarDados():

    def __init__(self, cor, lados):
        self.cor = cor
        self.lados = lados

    def rolarDados(self):
        """Função que retorna um lado aleatório do dado."""
        return self.lados[random.randint(0, 5)]


class Jogador():

    def __init__(self, nome, pontos):
        self.nome = nome
        self.pontos = pontos

    def rodada(self):
        """Função que informa o jogador a iniciar a partida, retorna seus pontos da rodada e finaliza a rodada em caso de ter tomado 3 tiros."""
        print()
        print(f'A partida começa com: {self.nome} ')
        self.pontosTemporarios = {'Cérebros': 0, 'Tiros': 0}
        self.dadoJogador = copoDados()
        self.dadoRolado = []
        escolha = 'S'
        while self.pontosTemporarios['Tiros'] < 3 and escolha == 'S' and len(self.dadoJogador) > 0:
            self.dadoRolado = self.sortearDado(self.dadoRolado)
            resultado = self.jogarDado(self.dadoRolado)
            resultado, self.dadoRolado = self.separarDados(resultado, self.dadoRolado)
            if self.pontosTemporarios['Tiros'] >= 3:
                print()
                print("Você tomou vários tiros e perdeu a rodada!")
                self.pontosTemporarios['Cérebros'] = 0
                break
            escolha = self.continuarRodada()
        self.pontos += self.pontosTemporarios['Cérebros']

    def sortearDado(self, dadoNaMao):
        """Função que sorteia os dodos a serem retirados na partida."""
        while len(dadoNaMao) < 3:
            dadoNaMao.append(self.dadoJogador.pop())
        return dadoNaMao

    def jogarDado(self, dadoNaMao):
        """Função que joga os dados sorteados na função anterior."""
        resultadoRodada = []
        resultadoDado = []
        for corDado in dadoNaMao:
            resultadoDado.append(corDado.rolarDados())
            resultadoRodada.append(corDado.cor + ' - ' + resultadoDado[-1])
        print(resultadoRodada)
        return resultadoDado

    def separarDados(self, dadoNaMao, dadoNaMesa):
        """Função que separa os dados que ficarão na mesa e que voltarão para o copo."""
        for i in range(2, -1, -1):
            if dadoNaMao[i] != "Passos":
                self.pontosTemporarios[dadoNaMao[i]] += 1
                dadoNaMao.pop(i)
                dadoNaMesa.pop(i)
        return dadoNaMao, dadoNaMesa

    def continuarRodada(self):
        """Função que pergunta ao jogador se deseja continuar jogando a partida em caso de não ter tomado 3 tiros."""
        continuarJogada = ''
        print()
        print(f"Você fez até o momento:\n {self.pontosTemporarios}")
        while continuarJogada != 'S' and continuarJogada != 'N':
            print()
            continuarJogada = input('Continuar a rodada (S/N)? ').upper()
        return continuarJogada


def copoDados():
    """Função onde foram criados os dados e onde embaralham os dados no copo."""
    tuboDeDados = []
    dadoVerde = criarDados('Dado Verde', ["Cérebros", "Passos", "Cérebros", "Tiros", "Passos", "Cérebros"])
    dadoAmarelo = criarDados('Dado Amarelo', ["Tiros", "Passos", "Cérebros", "Tiros", "Passos", "Cérebros"])
    dadoVermelho = criarDados('Dado Vermelho', ["Tiros", "Passos", "Tiros", "Cérebros", "Passos", "Tiros"])

    for i in range(1, 6):
        tuboDeDados.append(dadoVerde)
    for i in range(1, 4):
        tuboDeDados.append(dadoAmarelo)
    for i in range(1, 3):
        tuboDeDados.append(dadoVermelho)

    shuffle(tuboDeDados)
    return tuboDeDados


def rodadaJogo(naRodada):
    """Função que informa quando uma rodada chegou ao fim."""
    for cadaJogador in naRodada:
        cadaJogador.rodada()
        print()
        print("Fim da rodada: ")
        mostrarPontos(naRodada)
    return naRodada


def criarJogadores():
    """Função que cria o jogador, solicita a quantidade de jogadores para a rodada e embaralha os jogadores."""
    totalDeJogadores = int(input("Digite o número de jogadores para esta partida:  "))
    jogadores = []
    for i in range(1, totalDeJogadores + 1):
        jogadorNome = input(f"Nome do Jogador {i}: ").upper()
        esseJogador = Jogador(jogadorNome, 0)
        jogadores.append(esseJogador)
    print()
    shuffle(jogadores)
    print("A ordem de jogada será:\n ")
    for i in range(len(jogadores)):
        print(i + 1, ':', jogadores[i].nome)

    return jogadores


def mostrarPontos(pontos):
    """Função que informa a quantidade de cérebros que o jogador comeu e quantidade de tiros que levou a cada jogada."""
    print("Os cérebros devorados por jogador nesta rodada são:")
    for i in range(len(pontos)):
        print(pontos[i].nome, '-' , pontos[i].pontos)


def main():
    """Função que executa o jogo e apresenta o vencedor."""
    jogadores = criarJogadores()
    fimDeJogo = False
    vencedor = []
    while fimDeJogo == False:
        rodadaJogo(jogadores)
        for cadaJogador in jogadores:
            if cadaJogador.pontos >= 13:
                fimDeJogo = True
                print('Fim de Jogo!!! Temos um vencedor!')
                vencedor.append(cadaJogador.nome)
                print(f'O vencedor é: {vencedor}')


if __name__ == '__main__':
    main()
