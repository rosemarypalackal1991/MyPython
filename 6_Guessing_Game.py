
import random
num_2_guess = random.randint(1,100)
#print(num_2_guess)  # Comment this at last

guess_no = 0
abs_list =[]
user_input =''

while(user_input != num_2_guess):
     user_input = input("Enter a number in the range [1,100]: ")
     print(type(user_input))
     guess_no +=1
     if guess_no ==1:
        if abs(num_2_guess - user_input)<=10:
           print("WARM!")
	else:
  	   print("COLD!")
        
     else:
        if abs(num_2_guess - user_input) < abs_list[-1]:
           print("WARMER")
        else:
           print("COLDER")
     abs_list.append(abs(num_2_guess - user_input))
     #print(abs_list)

print("Hurray!! You guessed it right in {} guesses".format(guess_no))



       



