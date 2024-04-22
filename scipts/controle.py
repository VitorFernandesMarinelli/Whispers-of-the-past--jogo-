#Modulo de controle do jogo

#Bibliotecas
import threading
import pygame
import grafico
import time

#Variaveis globais
ehJogoExecultando = True

#Função para tratar os eventos capturados no modulo grafico
def TratamentoEventos():
    #Entradas: Nenhuma
    #Saida: Nenhuma
    global ehJogoExecultando
    time.sleep(2) #Tem que dá um tempo para a janela ser criada
    while ehJogoExecultando:
        if grafico.VerificadoNovoEvento(): #Se o modulo grafico captura um evento ele verifica qual é o tipo de evento
            evento = grafico.EntregaEventoAtual() 
            if evento.type == pygame.QUIT: #finaliza a aplicação ao apertar o botão de fechar
                grafico.ParaExeculcao()
                ehJogoExecultando = False

#Função para mandar um texto para ser escrito na tela para o modulo grafico, em um estilo de maquina de escrever (letra por letra)
def Escrever(txt): #consertar depois
    #Entradas: (String) texto a ser escrito na tela
    #Saidas: Nenhum
    mensagem = ""
    for caracter in txt:
        mensagem = mensagem + caracter
        grafico.EscreverNaTela(mensagem)
        time.sleep(0.5)

#Crias trheads:
threadGrafico = threading.Thread(target=grafico.ExecultarGrafico)
threadEventos = threading.Thread(target=TratamentoEventos)
threadEventos.start()
threadGrafico.start()
threadEventos.join()
threadGrafico.join()
