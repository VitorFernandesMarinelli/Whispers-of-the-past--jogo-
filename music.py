#Cuida das musicas
import pygame

#incializa o modulo de musica do pygame
def start():
    pygame.mixer.init()

#troca a musica que está sendo tocada
def change_music(disco):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(disco)
    pygame.mixer.music.play(-1)

#para a musica
def stop_music():
    pygame.mixer.music.stop()

#"despausa" a musica
def retorn_music():
    pygame.mixer.music.unpause()

#toca um efeito sonoro
def play_sound_efect(soud_path):
    song_to_play = pygame.mixer.Sound(soud_path)
    song_to_play.play()