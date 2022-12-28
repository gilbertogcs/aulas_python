#importando as libs necessarias
import random
import os

move_list = ["papel", "pedra", "tesoura"]
player_count = 0
computer_count = 0

print(50 * '=')
print('Seja bem vindo ao Jogo Pedra Papel Tesoura')
print(50 * '=')

#função somente para fazer o print dos valores
def main_print():
    print(50 * '=')
    print("\nPLACAR:")
    print('Você: {}'.format(player_count))
    print('Compurador: {}'.format(computer_count))
    print('\n')
    print('Escolha seu lance: ')
    print('0 - Papel | 1 - Pedra | 2 - Tesoura')

def select_move():
    return random.choice(move_list)#retorna elemento da lista de forma aleatoria

def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1, 2]:
                raise #crash no programa
            return move_list[player_move]
        except Exception as e:
            print(e)

def select_winner(p_move, c_move):
    global player_count, computer_count
    if p_move == "papel":
        if c_move == "pedra":
            player_count +=1
            return"p"
    elif c_move == "tesoura":
        computer_count +=1
        return "c"
    else:
        return "d"

    if p_move =="pedra":
        if c_move =="tesoura":
            player_count +=1
            return "p"
        elif c_move =="papel":
            computer_count +=1
            return "c"
        else:
            return "d"

    if p_move == "tesoura":
        if c_move == "papel":
            player_count +=1
            return "p"
        elif c_move == "pedra":
            computer_count +=1
            return "c"
        else:
            return "d"

again =1
while again ==1:
    main_print()
    player_move = get_player_move()
    computer_move = select_move()
    winner = select_winner(player_move, computer_move)
    print('')
    print(50*'=')
    print('Sua jogada: {}'.format(computer_move.upper()))

    if winner == "p":
        print('Você Venceu!')
    elif winner == "c":
        print('Você Perdeu!')
    else:
        print('Empate')
    print(50 *'=')

    while True:
        print("Para Jogar Novamente? 0 - Sim | 1 - Não")
        next = int(input())
        if next ==0:
            break
        elif next == 1:
            again = 0
            break
    os.system("cls")








