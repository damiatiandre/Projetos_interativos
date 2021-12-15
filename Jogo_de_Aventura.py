# Um jogo baseado em decisões tomadas por meio de respostas fornecidas ao programa
# O jogo possui finais alternativos 

# Cenário: Uma guerra de duas nações: Acre e Óleo, Somente Acre irá vencer, e o Óleo irá perder, então precisa-se chegar as decisões corretas
# vencer a guerra.

import PySimpleGUI as sg

class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Nasceste no Sul ou no Norte? '# Norte: Óleo, Sul: Acre
        self.pergunta2 = 'Qual arma deseja iniciar? (Espada ou Escudo) ' 
        self.pergunta3 = 'Qual a sua especialidade em batalha? (linha de frente ou tática)'

        self.finalHistoria1 = 'Você será um heroi na linha de frente!'
        self.finalHistoria2 = 'Você será um heroi protegendo todas as nossas tropas, porém morrerá em batalha.'
        self.finalHistoria3 = 'Você será um exímio espião, usando sua tática e manha, pegando informações preciosas e assim vencemos a guerra!'
        self.finalHistoria4 = 'Você não é capaz de lutar nessa batalha!'


        
    def Iniciar(self):
        # Layout
        layout = [
            [sg.Output(size=(77,0))],
            [sg.Input(size=(50,0),key='escolha')],
            [sg.Button('Iniciar'),sg.Button('Responder')]
        ]
        # criar a janela
        self.janela = sg.Window('Bem vindo ao jogo de escolhas, onde a errada, custará sua vida!',layout=layout)
        while True:
            # ler os dados
            self.LerValores()
            # fazer algo com os dados
            if self.evento == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()
                if self.valores['escolha'] == 'norte':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'espada':
                        print(self.finalHistoria1)
                    if self.valores['escolha'] == 'escudo':
                        print(self.finalHistoria2)
                if self.valores['escolha'] == 'sul':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'linha de frente':
                        print(self.finalHistoria4)
                    if self.valores['escolha'] == 'tatico':
                        print(self.finalHistoria3)
        
    def LerValores(self):
        self.evento, self.valores = self.janela.Read()

jogo = JogoDeAventura()
jogo.Iniciar()

