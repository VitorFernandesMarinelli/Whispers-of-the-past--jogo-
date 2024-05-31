#script que carrega as imagem, musica, falas e efeitos sonoros 
import os
import pygame
import pygame.locals

#pega o caminho absoluto do código python
def get_python_location():
    return os.path.dirname(os.path.abspath(__file__))

#Carrega todas as imagens do jogo
def load_imagens():
    images = []
    local = get_python_location()
    local = local+"\\imagens\\"
    names = os.listdir(local)
    for arqurive in names:
        absolute = local+arqurive
        absolute = absolute.replace('\\', '/')
        load = pygame.image.load(absolute)
        images.append(load)
    return images


#Carrega o local de todas as musicas do jogo
def load_musics():
    musics = []
    local = get_python_location()
    local = local+"\\musicas\\"
    names = os.listdir(local)
    for arqurive in names:
        absolute = local+arqurive
        absolute = absolute.replace('\\', '/')
        musics.append(absolute)
    return musics


#carrega todos os efeitos sonoros do jogo
def load_sound_effects():
    sounds = []
    local = get_python_location()
    local = local+"\\sons\\"
    names = os.listdir(local)
    for arqurive in names:
        absolute = local+arqurive
        absolute = absolute.replace('\\', '/')
        sounds.append(absolute)
    return sounds

#carrega as descrições e falas
def load_text(idLanguange):
    texts = []
    local = get_python_location()
    if idLanguange == 0:  #id = 0 Portugues
        local = local + "\\PT-BR.txt"
    else:  
        local = local + "\\EN-EUA.txt"
    # <dá para escalonar os idiomas> 
    with open(local, 'r',encoding='utf-8') as arquivo_entrada:
        for linha in arquivo_entrada:
            texts.append(linha.strip()) 
    return texts    
    


