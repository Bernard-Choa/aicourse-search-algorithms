from tkinter import *
import math

def evaluate():
    winner = check_winner()
    print(winner)

    if winner == "x":
        return 1
    elif winner == "o":
        return -1
    else:
        return 0

# Minimax function with alpha-beta pruning
def minimax(buttonValues, depth, alpha, beta, isAlphaPlayer):
    if check_winner() is not None or depth == 0:
        return evaluate()
    

    if isAlphaPlayer:
        max_eval = -math.inf
        for i in range(9):
            if buttons[i]['text'] == '':
                buttons[i]['text'] = 'x'
                eval_score = minimax(buttonValues, depth - 1, alpha, beta, False)
                buttons[i]['text'] = ''
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if buttons[i]['text'] == '':
                buttons[i]['text'] = 'o'
                eval_score = minimax(buttonValues, depth - 1, alpha, beta, True)
                buttons[i]['text'] = ''
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
        return min_eval

# Function to find the best move using minimax with alpha-beta pruning
def find_best_move(buttonValues):
    
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if buttons[i]['text'] == '':
            buttons[i]['text'] = 'x'
            move_score = minimax(buttonValues, 9, -math.inf, math.inf, False)
            buttons[i]['text'] = ''

            # print(move_score, "&", best_score)

            if move_score > best_score:
                best_score = move_score
                best_move = i

    return best_move


def next_turn(row, column):

    global player

    if buttons[row*3+column]['text'] == "" and check_winner() is None:

        buttons[row*3+column]['text'] = player

        if check_winner() is None:
            player = players[0]
            label.config(text=(players[0]+" turn"))

        elif check_winner() is True:
            label.config(text=(players[1]+" wins"))

        elif check_winner() == "Tie":
            label.config(text="Tie!")

        buttonValues = []
        for button in buttons:
            buttonValues.append(button['text'])
        # print(buttonValues)

        move = find_best_move(buttonValues)
        print(move)

        buttons[move]['text'] = player

        if check_winner() is None:
            player = players[1]
            label.config(text=(players[1]+" turn"))

        elif check_winner() is True:
            label.config(text=(players[0]+" wins"))

        elif check_winner() == "Tie":
            label.config(text="Tie!")

        # if player == players[0]:

        #     buttons[row*3+column]['text'] = player

        #     if check_winner() is False:
        #         player = players[1]
        #         label.config(text=(players[1]+" turn"))

        #     elif check_winner():
        #         label.config(text=(players[0]+" wins"))

        #     elif check_winner() == "Tie":
        #         label.config(text="Tie!")

        # else:

        #     buttons[row*3+column]['text'] = player

        #     if check_winner() is False:
        #         player = players[0]
        #         label.config(text=(players[0]+" turn"))

        #     elif check_winner():
        #         label.config(text=(players[1]+" wins"))

        #     elif check_winner() == "Tie":
        #         label.config(text="Tie!")

def check_winner():

    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    
    buttonValues = []
    for button in buttons:
        buttonValues.append(button['text'])

    for combination in winning_combinations:
        if buttonValues[combination[0]] == buttonValues[combination[1]] == buttonValues[combination[2]] != '':
            # buttons[combination[0]].config(bg="green")
            # buttons[combination[1]].config(bg="green")
            # buttons[combination[2]].config(bg="green")
            return buttonValues[combination[0]]
    
    if '' not in buttonValues:
        return 'Tie'

    return None

    # for row in range(3):
    #     if buttons[row*3+0]['text'] == buttons[row*3+1]['text'] == buttons[row*3+2]['text'] != "":
    #         buttons[row*3+0].config(bg="green")
    #         buttons[row*3+1].config(bg="green")
    #         buttons[row*3+2].config(bg="green")
    #         return True

    # for column in range(3):
    #     if buttons[0*3+column]['text'] == buttons[1*3+column]['text'] == buttons[2*3+column]['text'] != "":
    #         buttons[0*3+column].config(bg="green")
    #         buttons[1*3+column].config(bg="green")
    #         buttons[2*3+column].config(bg="green")
    #         return True

    # if buttons[0*3+0]['text'] == buttons[1*3+1]['text'] == buttons[2*3+2]['text'] != "":
    #     buttons[0*3+0].config(bg="green")
    #     buttons[1*3+1].config(bg="green")
    #     buttons[2*3+2].config(bg="green")
    #     return True

    # elif buttons[0*3+2]['text'] == buttons[1*3+1]['text'] == buttons[2*3+0]['text'] != "":
    #     buttons[0*3+2].config(bg="green")
    #     buttons[1*3+1].config(bg="green")
    #     buttons[2*3+0].config(bg="green")
    #     return True

    # elif empty_spaces() is False:

    #     for row in range(3):
    #         for column in range(3):
    #             buttons[row*3+column].config(bg="yellow")
    #     return "Tie"

    # else:
    #     return False


def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row*3+column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global player

    player = "o"

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row*3+column].config(text="",bg="#F0F0F0")


window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"]
player = "o"
buttons = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

label = Label(text=player + " turn", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row*3+column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row*3+column].grid(row=row,column=column)

window.mainloop()