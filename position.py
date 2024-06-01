import pygame
#script que guarda a possição de todos os objtos 

List_of_interactives = []


def load_possicion_objects_interactvs(scene,state):
    global List_of_interactives
    print(state)
    list_temporary = []
    if state == "espera":
        list_temporary.append(pygame.Rect(452,142,486,254)) # id = 0 → Tv 
        list_temporary.append(pygame.Rect(1286,70,143,311)) # id = 1 → porta (sala para porão)
    elif state == "jogando":
        if scene == "sala":
            list_temporary.append(pygame.Rect(452,142,486,254)) # id = 0 → Tv 
            list_temporary.append(pygame.Rect(1286,70,143,311)) # id = 1 → porta (sala para porão)         
            list_temporary.append(pygame.Rect(1,500,119,69)) # id = 2 → setaEsquerda (sala para cozinha)
            list_temporary.append(pygame.Rect(1350,500,119,69)) # id = 3 → setaDireita (sala para corredor)
            list_temporary.append(pygame.Rect(990,62,195,97)) # id = 4 → quadroFazenda
            list_temporary.append(pygame.Rect(1086,190,99,97)) # id = 5 → quadroSala (separação)
        elif scene == "porao":
            list_temporary.append(pygame.Rect(561,0,69,119)) #id = 0 → setaCima (porão sala)
            list_temporary.append(pygame.Rect(547,195,61,91)) # id = 1 → leitorSenha (porão)
            list_temporary.append(pygame.Rect(288,96,257,387)) # id = 2 → porta (porão para fim)
        elif scene == "cozinha":
            list_temporary.append(pygame.Rect(1352,429,119,69)) # id = 0 → setaDireita (cozinha sala)
            list_temporary.append(pygame.Rect(350,248,210,128)) # id = 1 → armarioCozinha (esquerda)
            list_temporary.append(pygame.Rect(663,249,209,127)) # id = 2 → armarioCozinha (centro)
            list_temporary.append(pygame.Rect(1063,249,209,127)) # id = 3 → armarioCozinha (direita)
        elif scene == "corredor":
            list_temporary.append(pygame.Rect(1128,498,119,205)) # id = 0 → setaBaixo (corredor sala)
            list_temporary.append(pygame.Rect(122,148,125,509)) # id = 1 → porta (corredor para quarto R)
            list_temporary.append(pygame.Rect(425,68,143,439)) # id = 2 → porta (corredor para quarto D)
            list_temporary.append(pygame.Rect(1017,29,222,326)) # id = 3 → porta (corredor para banheiro)
        elif scene == "quartoR":
            list_temporary.append(pygame.Rect(1006,498,119,205)) # id = 0 → setaBaixo (quarto R para corredor)
            list_temporary.append(pygame.Rect(832,2,225,125)) # id = 1 → estante de livros
            list_temporary.append(pygame.Rect(30,0,318,672)) # id = 2 → QuartoR (guardaRoupa)
        elif scene == "quartoD":
            list_temporary.append(pygame.Rect(1006,498,119,205)) # id = 0 → setaBaixo (quarto D para corredor)
            list_temporary.append(pygame.Rect(232,364,233,101)) # id = 1 → QuartoD (gaveta)
            list_temporary.append(pygame.Rect(780,112,73,80)) # id = 2 → quadroQuartoD (inacabado)
        elif scene == "banheiro":
            list_temporary.append(pygame.Rect(693,492,119,205)) # id = 0 → setaBaixo (banheiro para corredor)
            list_temporary.append(pygame.Rect(1036,284,76,63)) # id = 1 → torneira (banheira)
            list_temporary.append(pygame.Rect(1276,366,43,15)) # id = 2 → banheiro (grampo)
            list_temporary.append(pygame.Rect(186,326,203,230)) # id = 3 → banheiro (privada)           
    elif state == "observavel":
        list_temporary.append(pygame.Rect(0,0,119,69)) # id = 0 → setaEsquerda (sair observavel)
        if scene == "sala":
            list_temporary.append(pygame.Rect(656,624,119,69)) # id = 1 → setaDireita (virar quadro)
        elif scene == "quartoR":
            list_temporary.append(pygame.Rect(128,0,1151,703)) # id = 1 → estante livros ampliada (fala)
        elif scene == "cozinha":
            list_temporary.append(pygame.Rect(234,60,933,603)) # id = 1 → armario ampliado (fala)
        elif scene == "quartoD":
            list_temporary.append(pygame.Rect(386,0,711,703)) # id = 1 → gaveta ampliado (fala)    
        elif scene == "porao":
            list_temporary.append(pygame.Rect(528,246,103,105)) # id = 1 → digito (1)        
            list_temporary.append(pygame.Rect(648,246,105,105)) # id = 2 → digito (2) 
            list_temporary.append(pygame.Rect(772,246,105,105)) # id = 3 → digito (3)   
            list_temporary.append(pygame.Rect(528,368,103,105)) # id = 4 → digito (4)        
            list_temporary.append(pygame.Rect(648,368,105,105)) # id = 5 → digito (5) 
            list_temporary.append(pygame.Rect(772,368,105,105)) # id = 6 → digito (6)
            list_temporary.append(pygame.Rect(528,488,103,105)) # id = 7 → digito (7)        
            list_temporary.append(pygame.Rect(648,488,105,105)) # id = 8 → digito (8) 
            list_temporary.append(pygame.Rect(772,488,105,105)) # id = 9 → digito (9)     
    elif state == "escolha":
        list_temporary.append(pygame.Rect(0,0,721,703)) # id = 0 → esolha aceitar
        list_temporary.append(pygame.Rect(722,0,1471,703)) #id = 1 → escolha recusar         
    List_of_interactives = list_temporary

#fornece a possção dos elementos pelo ID
def get_object_possition(object_id,scene,state):
    posX = 0
    posY = 0
    if object_id == 13: #prof palito
        posX = 1007 
        posY = 196
    #objetos que precisam de um contexto para pegar a possição:
    elif object_id == 26: #seta para baixo
        if scene == "banheiro":
            posX = 693
            posY = 492
        elif scene == "corredor":
            posX = 1128
            posY = 498
        elif scene == "quartoD":
            posX = 1006
            posY = 498
        elif scene == "quartoR":
            posX = 1006
            posY = 498
    elif object_id == 27: #seta para cima
        posX = 561
        posY = 0
    elif object_id == 28: #seta para a direita
        if scene == "sala" and state != "observavel":
            posX = 1350
            posY = 500
        elif scene == "cozinha": #cozinha
            posX = 1352
            posY = 429
        else: #virar quadro observavel
            posX = 656 
            posY = 624
    elif object_id == 29: #seta para a esquerda 
        if scene == "sala" and state != "observavel":
            posX = 1
            posY = 500
        else: #observaveis 
            posX = 0
            posY = 0
    possition_to_send = (posX,posY)
    return possition_to_send

#fornce a possição dos textos
def get_text_possitio(text_id):
    posX = 100
    posY = 550
    if text_id == 0:
        posX = 160
        posY = 550
    #<escalonavel>
    possition_to_send = (posX,posY)
    return(possition_to_send)






#verifica se clicou em um objeto
def colid_object(mousePos): 
    for id in range(len(List_of_interactives)):
        if List_of_interactives[id].collidepoint(mousePos):
            return id
    # se não colidiu com nada, ele devolve -1
    return -1
    