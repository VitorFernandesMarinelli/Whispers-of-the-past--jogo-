import pygame

images_to_Drwan = []
position_images = []

font = ""

new_event = False
event_to_treat = ""

isRuning = True
isChanging_grphics = False
render_now = False

#permite o controle pega informações do evento
def see_event():
    event = ""
    if new_event == True:
        event= event_to_treat
    return event


#idica que o evento já foi precebido
def event_handled():
    global new_event, event_to_treat
    new_event = False
    event_to_treat = ""

#troca as imagens a ser renderizadas
def change_images(new_images, new_possitions):
    global images_to_Drwan, position_images, isChanging_grphics
    while render_now == True: #só troca o contexto se não estiver no processo de atualização
        pass
    isChanging_grphics = True
    images_to_Drwan = new_images
    position_images = new_possitions
    isChanging_grphics = False

#finaliza a parte grafica
def shut_down():
    global isRuning
    isRuning = False

#pega a possição do mouse:
def get_mouse_possition():
    return pygame.mouse.get_pos() 


#captura eventos
def events(event):
    global new_event, event_to_treat
    new_event = True
    if event.type == pygame.QUIT: #botão de fechar
        event_to_treat = "OFF"
    elif event.type == pygame.MOUSEBUTTONDOWN: #o mouse interagiu com algo 
        event_to_treat = "click"
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_z:
            event_to_treat = "jump"
        else:
            event_to_treat = "key"

#desenha na tela todas a imagens
def draw_imagens(screen):
    global render_now
    i = 0
    if isChanging_grphics == False:
        render_now = True
        for image in images_to_Drwan:
            screen.blit(image,position_images[i])
            i = i + 1
        render_now = False
        

#mostra um texto na tela
def display_mensagens(text, possition): 
    global images_to_Drwan, position_images
    mensage = font.render(text, True, (255, 255, 255))    
    images_to_Drwan.append(mensage)
    position_images.append(possition)

#remove o texto
def clear_text():
    global images_to_Drwan, position_images, isChanging_grphics
    index = (len(images_to_Drwan)-1)
    while render_now == True: #só troca o contexto se não estiver no processo de atualização
        pass
    isChanging_grphics = True
    images_to_Drwan.remove(images_to_Drwan[index])
    position_images.remove(position_images[index])
    isChanging_grphics = False

        

#inicia o script de graphics
def start_graphics():
    global font
    # Inicializacao
    pygame.init()
    font = pygame.font.Font(None, 36)

    # Definindo as dimensoes da tela
    SCREEN_WIDTH = 1472
    SCREEN_HEIGHT = 704
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Whispers Of The Past")

    while isRuning:
        draw_imagens(screen)
        for event in pygame.event.get():
            events(event)
        pygame.display.flip()


