import pygame

class ObjetosInterativos:
    def __init__(self, imagem, x, y,id,Ampliavel):
        self.imagem = imagem
        self.rect = self.imagem.get_rect() #posicao e tamnho da imagem
        self.rect[0] = x
        self.rect[1] = y
        self.id = id #esse id serve para as falas 
        self.ehAmpliavel = Ampliavel

    def desenhar(self, janela):
        janela.blit(self.imagem,(self.rect[0],self.rect[1]))

    def ampliar(): #implementar depois
        pass 


class Cenarios:
    def __init__(self, imagem):
        self.imagem = imagem

    def desenhar(self, janela):
        janela.blit(self.imagem(0,0))


class ItensCenario:
    def __init__(self, imagem, x, y,id):
        self.imagem = imagem
        self.rect = self.imagem.get_rect() #posicao e tamnho da imagem
        self.rect[0] = x
        self.rect[1] = y
        self.id = id
        self.ehFoiPego = False #indica se o item foi coletado pelo jogador

    def desenhar(self, janela):
        if self.ehFoiPego == False:
            janela.blit(self.imagem,(self.rect[0],self.rect[1])) #coloca o objeto na cena 
        else:
            janela.blit(self.imagem,((10*self.id), 20))  #coloca o objeto como UI

