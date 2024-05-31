#Script que diz o que deve ser renderizado em cena e a ordem de renderização

frame_front = True #se o quadro separação está de frente ou de costas
bath_puzzel_complete = False # o estado que a banheira vai estar
number_pasword = 0


#indica que nas proximas vezes a banheira não vai estar suja
def complete_bath():
    global bath_puzzel_complete
    bath_puzzel_complete = True

#adiciona os digitos secretos da senha que foram digitados
def passaword(list_render):
    if number_pasword != 0:
        id = number_pasword + 38 # de 39 a 42
        list_render.append(id)
    return list_render

def change_passaword(number_of_passaword):
    global number_pasword
    number_pasword = number_of_passaword

#função que devolve uma lista de elementos que devem aparecer na cena dado o contexto atual
def objects_render(state,previous_scene, current_scene,Tv_On,inventory):
    global frame_front
    render = []
    if state == "jogando":
        if current_scene == "sala":
            render.append(3) #fundo
            render.append(13) #profPalito
            render.append(28) #seta para direita
            render.append(29) #seta para esquerda
            if Tv_On == True:
                render.append(11) #tv com estatica
            else:
                render.append(12) #tv desligada
        elif current_scene == "cozinha":
            render.append(7) #fundo
            render.append(28) #seta para esquerda
        elif current_scene == "porao":
            render.append(4) #fundo
            render.append(27) #seta para cima
        elif current_scene == "corredor":
            render.append(6) #fundo
            render.append(26) #seta para baixo
        elif current_scene == "quartoD":
            render.append(8) #fundo
            render.append(26) #seta para baixo
        elif current_scene == "quartoR":
            render.append(9) #fundo
            render.append(26) #seta para baixo
        elif current_scene == "banheiro":
            render.append(5) #fundo 
            render.append(26) #seta para baixo
            if bath_puzzel_complete == True:
                render.append(17) #agua da torneira
                render.append(18) #agua limpa 
            else:
                render.append(16) #agua com espuma
            if inventory[0] == False: #grampo está na pia
                render.append(19) #grampo de cabelo
    elif state == "menu":
        render.append(1) #fundo parte de baixo
        render.append(2) #fundo parte de cima
    elif state == "observavel":
        #fundo que vai ser sobreposto:
        if previous_scene == "sala":
            render.append(3)
            render.append(0) #fundo que "observavel"
            render.append(28) # seta para virar o quadro
            if frame_front == True: #quadro está de frente
                render.append(14)
            else: #quadro está de costa 
                render.append(15)
            frame_front = not frame_front
        elif previous_scene == "cozinha":
            render.append(7)
            render.append(0) #fundo que "observavel"
            render.append(34) #armario
            render.append(35) #latas
            if inventory[2] == True: #puzel completo
                render.append(36) #lata colocadas
        elif previous_scene == "quartoD":
            render.append(8) 
            render.append(0) #fundo que "observavel"
            render.append(37)
        elif previous_scene == "quartoR":
            render.append(9)
            render.append(0) #fundo que "observavel"
            render.append(33)
        elif previous_scene == "porao":
            render.append(4) #fundo
            render.append(0) #fundo que "observavel"   
            render.append(38) # caixa de senha
            render = passaword(render)         
        render.append(29)#seta para sair do observavel
    elif state == "curticneInicial":
        render.append(3) #fundo
        render.append(13) #profPalito        
        render.append(10) #Tv noticiario
    elif state == "espera" or state == "final_A":
        render.append(3) #fundo
        render.append(13) #profPalito
        if Tv_On == True:
            render.append(11) #tv com estatica
        else:
            render.append(12) #tv desligada  
    elif state == "creditos_A":
        render.append(3) #fundo
        render.append(13) #profPalito
        render.append(30) #tela creditos final A
    elif current_scene == "secreto":
        render.append(43) #fundo
    
    i = 20 # imagens do 20 ao 24
    if state != "observavel":
        for ui in inventory:
            if ui == True:
                render.append(i)
            i = i + 1
    return render

#muda o estado da Tv
def turn_Tv(tv_on):
    id = -1
    previous_id = -1
    if tv_on == True: #ligado passa para desligado:
        id = 12
        previous_id = 11
    else: #desligado passa para ligado:
        id = 11
        previous_id = 12
    return id, previous_id

#adiciona a caixa de texto na lista de objetos para renderizar
def text_render():
    id = 25 #mini fundo para textos
    return id

#remove o ultimo elemento da lista de objetos para renderizar, se espera que seja a caixa de texto
def remove_text(render_list):
    size = (len(render_list) - 1)
    render_list.remove(render_list[size])
    return render_list

#devolve o sprte da Tv
def changeTV_cutscene():
    id = 11
    previous_id = 10
    return id, previous_id


