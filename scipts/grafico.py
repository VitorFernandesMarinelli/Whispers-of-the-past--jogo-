#Modulo para controlar a janela grafica
#Bibliotecas
import pygame

#Variaveis globais
ehJogoExecutando = True #controle de execução da aplicação grafica

#variaveis para a comunicação de eventos entre o modulo grafico e o controle
evento = "" 
alertaEvento = False

#variaveis para escrever textos na janela
textoMensagem = ""
ehNovaMensagem = False

#Implementação das funções

#Resquisito 1:
#Função que pega a posição do mouse dentro da janela
def EntregaPosicaoMouse():
    #Entradas: Nenhuma
    #Saidas: (2 floats) possição x e y do mouse
    posicaoMouseX, posicaoMouseY = pygame.mouse.get_pos()
    return posicaoMouseX, posicaoMouseY

#Função para escrever na tela
def EscreverNaTela(txt):
    #Entradas: (String) mensagem a ser impresa na tela
    #Saidas: Nenhuma
    global textoMensagem, ehNovaMensagem
    textoMensagem = txt
    ehNovaMensagem = True
    
#Função para finalizar a janela
def ParaExecucao():
    #Entradas: Nenhuma
    #Saidas: Nenhuma
    global ehJogoExecutando
    ehJogoExecutando = False

#Função para comunicação do evento entre o modulo grafico e controle
def EntregaEventoAtual():
    #Entradas: Nenhuma
    #Saidas: Evento do pygame
    global alertaEvento
    alertaEvento = False
    return evento

#Função para comunicação entre o modulo grafico e controle para verificar se houve um evento novo
def VerificadoNovoEvento():
    #Entradas: Nenhuma
    #Saidas: (booleano) verificado se há um novo evento
    return alertaEvento

#Função para atualizar informações de eventos
def EventoAcionado(eventoCapturado):
    #Entradas: Evento do pygame
    #Saidas: Nenhuma
    global evento, alertaEvento
    evento = eventoCapturado
    alertaEvento = True

#Função para desenhar sprites (Implementar depois)
def DesnharTela():
    pass

#Função para iniciar a janela e manter ela ativa
def ExecultarGrafico():
    #Entradas: Nenhuma
    #Saidas: Nenhuma
    #Cria janela:
    pygame.init() 
    janela = pygame.display.set_mode([1472 , 704]) 
    titulo = pygame.display.set_caption("Whispers of the past") 
    #Mantem a janela aberta:
    while ehJogoExecutando:
        pygame.display.update() #atualiza a tela 
        DesnharTela()
        for eventos in  pygame.event.get():
            EventoAcionado(eventos)
            
