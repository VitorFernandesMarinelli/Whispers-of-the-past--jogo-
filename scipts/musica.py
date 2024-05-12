#modulo de musica
import pygame


pygame.mixer.init()

def TocarMusica(DiscoDaMusica):
    pygame.mixer.music.load(DiscoDaMusica)
    pygame.mixer.music.play(-1) #faz ficar em loop a musica


