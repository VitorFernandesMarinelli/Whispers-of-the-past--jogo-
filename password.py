#cuida da senha do porão

correct_password = [3,9,5,3]
current_password = [0,0,0,0]
point = 0

#verifica se a senha está correta
def check_password():
    correct = True
    for i in range(len(correct_password)):
        if current_password[i] != correct_password[i]:
            correct = False
    return correct

#verifica um digito
def try_password(number):
    global point, current_password
    password_correct = -1 #-1 indica que a senha ainda não está completa
    current_password[point] = number #adiciona o digito na senha
    point = point + 1
    if point == 4: #senha completa
        password_correct = check_password()
        point = 0 #reinicia a senha
    return password_correct

def how_digits_password():
    return point    