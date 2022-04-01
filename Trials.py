
import random
input_list = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']


def player_input():  # asks the first player to choose the marker of his choice. returns a tuple of marker order
    user_in = ''
    while (user_in != 'X' and user_in != 'O'):
         user_in = raw_input("Player1: Please enter your marker: ").upper()
         if user_in == 'X':
            return ('X','O')
         else:
            return('O','X')
#(inp1,inp2) = player_input()


def who_plays_first(): #randomly chooses which player to start first
    player = random.randint(1,2)
    if player==1:
       print("First chance goes to player 1")
       return 1
    else:
       print("First chance goes to player 2")
       return 0

#play = (who_plays_first())


def choose_pos(): # asks the current player to enter his position
    pos = raw_input("Enter the value from 1 to 9: ")
    int_pos = int(pos)
    return(int_pos)

def board(position,marker): # list with marker and position
    input_list[position] = marker
    return(input_list)

def display_board(my_board):
    print("     |     |     ")
    print('  '+my_board[1]+'  |  '+ my_board[2]+'  |  '+ my_board[3])
    print("     |     |     ")
    print("=================")
    print("     |     |     ")
    print('  '+my_board[4]+'  |  '+ my_board[5]+'  |  '+ my_board[6])
    print("     |     |     ")
    print("=================")
    print("     |     |     ")
    print('  '+my_board[7]+'  |  '+ my_board[8]+'  |  '+ my_board[9])
    print("     |     |     ")

def iswin(my_board,marker):
    if ((my_board[1] == marker and my_board[2] == marker and my_board[3] == marker) or (my_board[4] == marker and my_board[5] == marker and my_board[6] == marker) or (my_board[7] == marker and my_board[8] == marker and my_board[9] == marker) or (my_board[1] == marker and my_board[4] == marker and my_board[7] == marker) or (my_board[2] == marker and my_board[5] == marker and my_board[8] == marker) or (my_board[3] == marker and my_board[6] == marker and my_board[9] == marker) or (my_board[1] == marker and my_board[5] == marker and my_board[9] == marker) or (my_board[3] == marker and my_board[5] == marker and my_board[7] == marker)):
        return 1

########################################## GAME ON #############################################################

(inp1,inp2) = player_input()  # gets marker suggestion from player 1 . obviously, player 2 takes the opp marker
if inp1 == 'X':
   marker1 = 'X'
   marker2 = 'O'
else:
   marker1 = 'O'
   marker2 = 'X'

play = who_plays_first()

while ((input_list[1] == ' ' or input_list[2] == ' ' or input_list[3] == ' ' or input_list[4] == ' ' or input_list[5] == ' ' or input_list[6] == ' ' or input_list[7] == ' ' or input_list[8] == ' ' or input_list[9] == ' ')):

    if play ==1: # player 1 plays first
       pos = choose_pos() # player 1 can choose his position
       myboard1 = board(pos,marker1) # list with marker and position of player1
       display_board(myboard1)
       if iswin(myboard1,marker1)==1:
          print("Player 1 wins")
          break  # breaks out of the while loop
       play = 0


    else:  #player 2 plays first
       pos = choose_pos()
       myboard2 = board(pos,marker2)
       display_board(myboard2)
       if iswin(myboard2,marker2)==1:
          print("Player 2 wins")
          break  # breaks out of the while loop
       play = 1



