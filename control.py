#controla a aplicação
import threading
import time
import random
import graphics
import load
import position
import music
import render
import password

Tv_ON = True
previous_scene = ""
current_scene = ""
state = ""

door_final_open = False
inventory = [False,False,False,False,False] # grampo | cabide | lata | chave A | chave B
current_id_text = -1

current_position = []
current_images = []

isRunning = True
protect_miss_click = False

images = []
songs = []
musics = []
texts = []

skip_text = False
writing_text = False
iten_description = False


#função que pega os eventos e trata os 
def take_events():
    global isRunning, skip_text, protect_miss_click, iten_description, current_id_text
    event = graphics.see_event()
    if event == "OFF": #Botão de fechar a janela
        graphics.shut_down()
        isRunning = False
        music.stop_music()
    elif protect_miss_click == True: #proteje contra apertar mutiplas vezes 
        protect_miss_click = False
        event = ""
    elif event == "key": #Evento de apertar uma tecla
        protect_miss_click = True
        if state == "menu":
            change_scene("sala","curticneInicial")
            music.change_music(musics[1])
            initiation_cutscene()
        elif writing_text == True:
            skip_text = True
        elif state == "curticneInicial":
            continue_initiation_cutscene()
        elif state == "final_A":
            final_A_cotinue()
        elif state == "cutsene_porao":
            continus_cutscene_porao()
        elif state == "cutscene_c":
            continus_cutscene_C()
        elif iten_description == True:
            graphics.clear_text()
            disable_text_box()
            iten_description = False
        time.sleep(0.4)
    elif event == "click": #Evento de clicar com o mouse
        protect_miss_click = True
        check_collision()
    elif event == "jump": #pula curticnes
        skip_text = True
        current_id_text = -2
        time.sleep(0.2)
        if state == "curticneInicial": 
            continue_initiation_cutscene()
        elif state == "cutsene_porao":
            continus_cutscene_porao()
        elif state == "cutscene_c":
            continus_cutscene_C()
    event = ""
    graphics.event_handled()
    time.sleep(0.2)

#função que continua a cutscene do final A 
def final_A_cotinue():
    global current_id_text,current_images
    graphics.clear_text()
    id = (current_id_text + 1)
    text = texts[id]
    if text == "eof":
        current_id_text = -1
        change_scene("sala","creditos_A")
    else:
        perpare_to_write(id)
        current_id_text = id

#função que inicia a cutscene do final A 
def final_A_cutscene_start():
    global current_id_text
    current_id_text = 22  
    music.play_sound_efect(songs[3])
    time.sleep(0.1)
    perpare_to_write(current_id_text)

#função que verifica se o final secreto foi acionado ou não
def verify_codicional_to_final_A():
    global current_id_text, current_images,current_position
    i = 0
    while i != 300:  #5 minutos
        time.sleep(1)
        i = i + 1
        print(i,"\n")
        if isRunning == False or state == "jogando":
            i = 300
    #se a condição foi concluida
    if state == "espera" and isRunning == True:
        current_id_text = 21
        change_scene("sala","final_A")
        activate_text_box()
        final_A_cutscene_start()

#interação com a tv na sala
def change_tv_states():
    global Tv_ON
    Tv_ON = not Tv_ON
    new_id, old_id = render.turn_Tv(Tv_ON)
    change_especific_imagem(new_id,old_id)

#segue o roteiro da cutscene do porão
def continus_cutscene_porao(): 
    global current_id_text,current_images
    graphics.clear_text()
    id = (current_id_text + 1)
    text = texts[id]
    if text == "eof" or current_id_text == -2:
        current_id_text = -1
        change_scene("secreto","escolha")
    else:
        if id == 50: # abriu a porta
            change_scene("secreto","cutsene_porao")
            activate_text_box()

        perpare_to_write(id)
        current_id_text = id

#inicia a cutscene do porão
def cutscene_porao_start():
    global current_id_text
    current_id_text = 49
    change_scene("porao","cutsene_porao")
    activate_text_box()
    perpare_to_write(current_id_text)

def continus_cutscene_C(): 
    global current_id_text,current_images
    graphics.clear_text()
    id = (current_id_text + 1)
    text = texts[id]
    if text == "eof" or current_id_text == -2:
        current_id_text = -1
        change_scene("secreto","Final_C")
    else:
        perpare_to_write(id)
        current_id_text = id

def start_cutscene_C():
    global current_images, current_position
    id_start_dialogue = 87
    change_scene("secreto","cutscene_c")
    time.sleep(0.5)
    activate_text_box()
    perpare_to_write(id_start_dialogue)

#verifica se o mouse clicou em algo valido
def check_collision():
    global iten_description, inventory, door_final_open
    pos = graphics.get_mouse_possition()
    idColide = position.colid_object(pos)
    if idColide != -1: #precionou um objeto existente no contexto atual do jogo
        if state != "observavel" and state != "escolha":
            if current_scene == "sala": #SALA-------------------------------
                if idColide == 0: #TV
                    change_tv_states()
                elif idColide == 1: #porta (sala para porão)
                    music.play_sound_efect(songs[3])
                    time.sleep(0.5)
                    change_scene("porao","jogando")
                elif idColide == 2: #seta Esquerda (sala para cozinha)
                    music.play_sound_efect(songs[3])
                    time.sleep(0.5)
                    change_scene("cozinha","jogando")
                elif idColide == 3: #seta Direita (sala para corredor)
                    music.play_sound_efect(songs[3])
                    time.sleep(0.5)
                    change_scene("corredor","jogando")                
                elif idColide == 4: #quadro da Fazenda
                    activate_text_box()
                    perpare_to_write(33)
                    iten_description = True
                elif idColide == 5: #quadro separação
                    change_scene(current_scene,"observavel")                  
            elif current_scene == "porao": # PORÃO--------------------------
                if idColide == 0: #seta porão para sala
                    music.play_sound_efect(songs[3])
                    time.sleep(0.5)
                    change_scene("sala","jogando")
                elif idColide == 1: #leitor senha
                    change_scene(current_scene,"observavel")
                elif idColide == 2: #porta porão
                    if door_final_open == True: #a senha está certa
                        cutscene_porao_start()
                    else: #a senha não está correta
                        activate_text_box() 
                        perpare_to_write(44)
                        iten_description = True                         
            elif current_scene == "cozinha": # COZINHA-----------------------
                if idColide == 0: #seta cozinha para sala
                    music.play_sound_efect(songs[3])
                    time.sleep(0.5)
                    change_scene("sala","jogando")       
                elif idColide == 1: #armario esquerda
                    change_scene(current_scene,"observavel")                      
                elif idColide == 2: #armario centro
                    activate_text_box() 
                    perpare_to_write(40)
                    iten_description = True 
                    inventory[2] = True #jogador pegou as latas
                elif idColide == 3: #armario da direita
                    if inventory[0] == True: # armario só abre com o grampo
                        inventory[4] = True # dentro do armario há a chave
                        activate_text_box() 
                        perpare_to_write(37)
                        iten_description = True
                    else: # amario trancado
                        activate_text_box() 
                        perpare_to_write(41)
                        iten_description = True                         
            elif current_scene == "corredor": # CORREDOR---------------------
                if idColide == 0: #seta corredor para sala
                    music.play_sound_efect(songs[3])
                    time.sleep(0.5)
                    change_scene("sala","jogando")
                elif idColide == 1: #porta quarto Renato
                    music.play_sound_efect(songs[3])
                    time.sleep(0.5)
                    change_scene("quartoR","jogando") 
                if idColide == 2: #porta quarto Dalila
                    if inventory[3] == True and inventory[4] == True: #jogador está em posse das duas partes da chave
                        music.play_sound_efect(songs[3]) 
                        time.sleep(0.5)
                        change_scene("quartoD","jogando")
                    else:
                        activate_text_box()
                        perpare_to_write(47)
                        iten_description = True
                elif idColide == 3: #porta banheiro
                    music.play_sound_efect(songs[3])
                    time.sleep(0.5)
                    change_scene("banheiro","jogando")                               
            elif current_scene == "quartoD": # QUARTO DALILA-----------------
                if idColide == 0: #seta quarto Dalila para corredor
                    music.play_sound_efect(songs[3])
                    time.sleep(0.5)
                    change_scene("corredor","jogando") 
                elif idColide == 1: #gaveta quarto Dalila
                    change_scene(current_scene,"observavel")
                elif idColide == 2: #quadro inacabado
                        activate_text_box() 
                        perpare_to_write(46)
                        iten_description = True  
            elif current_scene == "quartoR": # QUARTO RENATO-----------------
                if idColide == 0: #seta quarto Renato para corredor
                    music.play_sound_efect(songs[3])
                    time.sleep(0.5)
                    change_scene("corredor","jogando")   
                elif idColide == 1: # estante de livros
                    change_scene(current_scene,"observavel")  
                elif idColide == 2: #guardaRoupa
                    inventory[1] = True 
                    activate_text_box()
                    perpare_to_write(39)
                    iten_description = True                  
            elif current_scene == "banheiro": # BANHEIRO---------------------
                if idColide == 0: #seta banheiro para corredor
                    music.play_sound_efect(songs[3])
                    time.sleep(0.5)
                    change_scene("corredor","jogando") 
                elif idColide == 1: #banheira
                    render.complete_bath()
                    refsh_scene()
                    activate_text_box()
                    perpare_to_write(36)
                    iten_description = True
                elif idColide == 2: #grampo pego
                    inventory[0] = True
                    activate_text_box()
                    perpare_to_write(35)
                    iten_description = True
                elif idColide == 3: #pegar chave da privada
                    if inventory[1] == True: #jogador estar com o cabide
                        activate_text_box()
                        perpare_to_write(37)
                        iten_description = True
                        inventory[3] = True    
                    else: #jogador está sem o cabide
                        activate_text_box()
                        perpare_to_write(38)
                        iten_description = True                                           
        elif state == "escolha":
            if idColide == 0: #aceitou
                change_scene("secreto","secreto")
                activate_text_box()
                perpare_to_write(86)
                time.sleep(10)
                change_scene(current_scene,"Final_B")
            else:
                start_cutscene_C()
        else: # OBSERVAVEL--------------------------
            if idColide == 0: #seta para sair
                change_scene(current_scene,"jogando")
            elif idColide == 1 and current_scene != "porao":
                if current_scene == "sala": # quadro separação
                    refsh_scene()
                elif current_scene == "quartoR": # estante de livros
                    activate_text_box()
                    perpare_to_write(34)
                    iten_description = True
                elif current_scene == "cozinha": # armario da direita
                    if inventory[2] == False: #ainda não está com as latas
                        activate_text_box()
                        perpare_to_write(42)
                        iten_description = True                        
                    else: #já tem as latas, puzzel completo
                        activate_text_box()
                        perpare_to_write(43)
                        iten_description = True   
                elif current_scene == "quartoD": # gaveta                    
                    activate_text_box()
                    perpare_to_write(45)
                    iten_description = True                    
            elif door_final_open == False: #senha
                correct_password = password.try_password(idColide) #aplica o digito
                if correct_password == True: #senha correta
                    door_final_open = True
                    render.change_passaword(4)
                    refsh_scene()
                    time.sleep(0.6)
                    change_scene("porao","jogando")
                elif correct_password == False: #senha digitada incorreta
                    render.change_passaword(4)
                    refsh_scene()
                    time.sleep(0.8)
                    render.change_passaword(0)
                    refsh_scene()
                    time.sleep(0.2)
                    activate_text_box()
                    perpare_to_write(48)
                    iten_description = True
                else: #inseriu um digito
                    number_of_digits = password.how_digits_password()
                    render.change_passaword(number_of_digits)
                    refsh_scene()

#pede para renderizar a mesma cena, usado para atualizções de objetos na cena
def refsh_scene():
    change_scene(current_scene,state)

#funcao que realiza a troca de cena
def change_scene(new_scene,new_state):
    global current_scene, previous_scene, state, current_position, current_images, Tv_ON
    position_to_send = []
    images_to_send = []
    #atuliza o contexto:
    previous_scene = current_scene 
    current_scene = new_scene
    state = new_state
    #pega o indice dos objetos da lista a serem renderezados
    index_images_render = render.objects_render(state,previous_scene,current_scene,Tv_ON,inventory)
    #carrega as possições e imagens
    for id in index_images_render:
        images_to_send.append(images[id])
        position_idividual = position.get_object_possition(id,current_scene,state)
        position_to_send.append(position_idividual)
    graphics.change_images(images_to_send,position_to_send)
    position.load_possicion_objects_interactvs(current_scene,state)
    current_images = images_to_send
    current_position = position_to_send


#funcao que altera a possicao de um objeto já renderizado, usado para fazer animacoes
def chagen_possition(id, new_possition):
    global current_position
    current_position[id] = new_possition
    graphics.change_images(current_images,current_position) 

#implementa uma pequena animacao no menu
def animation_menu():
    pos = current_position[1]
    pos_text = position.get_text_possitio(0)
    apear_text = True
    while current_scene == "menu" and isRunning == True:
        p = random.randint(-1, 1)
        if apear_text == True:
            graphics.display_mensagens(texts[0],pos_text)
        else:
            graphics.clear_text()
        apear_text = not apear_text
        new_pos = (pos[0]+p,pos[1])
        chagen_possition(1,new_pos)
        time.sleep(2)

#atualiza um sprite (quando não precisa mudar o current_position)
def change_especific_imagem(new_id, previous_id):
    global current_images
    previous_image = images[previous_id]
    for i in range(len(current_images)):
        if current_images[i] == previous_image:
            current_images[i] = images[new_id]
    graphics.change_images(current_images,current_position)

#faz a animação da cutscene inicial continuar
def continue_initiation_cutscene():
    global current_id_text,current_images
    graphics.clear_text()
    id = (current_id_text + 1)
    text = texts[id]
    if text == "eof" or current_id_text == -2:
        current_id_text = -1
        verify_A = threading.Thread(target=verify_codicional_to_final_A) #uma nova trhead fica rodando para verificar se as condições do final A foram atendidos
        verify_A.start()
        change_scene("sala","espera")
        music.change_music(musics[1]) #a musica de gameplay volta a tocar
    else:
        if id == 7: #Tv dá problema
           music.play_sound_efect(songs[0]) #som interferencia da TV
           current_id_Tv, previous_id_Tv = render.changeTV_cutscene()
           change_especific_imagem(current_id_Tv,previous_id_Tv)
        elif id == 8:
            music.play_sound_efect(songs[1]) #som do telefone
            time.sleep(6)
        elif id == 16:
            music.play_sound_efect(songs[3])#porta abrindo
        elif id == 18:
            music.stop_music()
            music.play_sound_efect(songs[2]) #som das batidas no porão
            time.sleep(15)
        perpare_to_write(id)
        current_id_text = id

#execulta a cutscene inicial
def initiation_cutscene():
    global current_images, current_position
    id_start_dialogue = 1
    time.sleep(0.5)
    activate_text_box()
    perpare_to_write(id_start_dialogue)

#desativa a caixa de texto
def disable_text_box():
    global current_images, current_position
    id = render.text_render()
    pos = position.get_object_possition(id,"sala",state)
    current_images.remove(images[id])
    current_position.remove(pos)
    graphics.change_images(current_images,current_position)
    change_scene(current_scene,state)

#ativa a caixa de texto
def activate_text_box():
    global current_images, current_position
    id = render.text_render()
    pos = position.get_object_possition(id,"sala",state)
    current_images.append(images[id])
    current_position.append(pos)
    graphics.change_images(current_images,current_position)

#prepara a uma thread para escrever os textos
def perpare_to_write(id):
    global current_id_text
    current_id_text = id
    write_thread = threading.Thread(target=write_machine,args=(id,))
    time.sleep(1)
    write_thread.start()
    # a thread secundaria volta para tratar eventos

#manda escrever na tela letra por letra de um texto
def write_machine(id):
    global writing_text,skip_text
    mensage = ""
    text = texts[id]
    pos = position.get_text_possitio(1)
    writing_text = True
    for letter in text:
        mensage = mensage+letter
        graphics.display_mensagens(mensage,pos)
        time.sleep(0.05)
        graphics.clear_text()
        if skip_text == True: #para impacientes, ele pula o texto para o final
            break
    skip_text = False
    writing_text = False
    graphics.display_mensagens(text,pos)
    
#função que inicia a parte do backend da aplicação
def start():
    global images,songs,musics,texts
    #carrga os arquivos para a aplicacao:
    images = load.load_imagens()
    songs = load.load_sound_effects()
    musics = load.load_musics()
    texts = load.load_text(0) #no momento só tem a versão em portugues
    #incia a musica:
    music.start()
    music.change_music(musics[0])
    #define o contexto inicial:
    change_scene("menu","menu")
    animation_menu_thread = threading.Thread(target=animation_menu)
    animation_menu_thread.start()
    while isRunning == True:
        take_events()


secundarie_thread = threading.Thread(target=start)
secundarie_thread.start()
graphics.start_graphics()