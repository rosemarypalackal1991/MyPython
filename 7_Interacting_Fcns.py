

### Create different functions which interacts with each other #########

#import random

#sample = range(1,10)

#random.shuffle(sample)

#print(sample)

### Shuffle doesnt return anything. So create a custom function which returns a shuffled list
#input_list = ['','O','']
def my_shuffled_list(input_list):
    from random import shuffle
    shuffle(input_list)
    return(input_list)
#my_shuffled_list(input_list)
    

def player_guess():
    
    #player_guess = ''
    
    player_guess = input("Enter the guess position- 0, 1 or 2: ")
    
    return int(player_guess)

#player_guess()

def guess_check (my_shuffled_list,player_guess):
    if my_shuffled_list[player_guess] == 'O':
       print("Correct")
    else:
       print("guess again")
       print(mix_list)


input_list = ['','O','']
mix_list = my_shuffled_list(input_list)
guess = player_guess()
guess_check(mix_list,guess)
   
