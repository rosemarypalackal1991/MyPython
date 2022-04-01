


#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

 #spy_game([1,2,4,0,0,7,5]) --> True
 #spy_game([1,0,2,4,0,5,7]) --> True
 #spy_game([1,7,2,0,4,5,0]) --> False




'''mylist = [1,0,2,4,0,5,7]
if 0 in mylist:
   ind1 = mylist.index(0)
   if mylist[ind1+1]==0:
      if mylist[ind1+2]==7:
         print('True')
      else:
         print('False')
   else:
      print('False') 
else:
   print ('False')

zeroes = [i for i,e in enumerate(mylist) if e==0]
sevens = [i for i,e in enumerate(mylist) if e==7]

print(zeroes)
print(sevens)

if zeroes[1]<sevens[0]:
   print('true')

else:
   print('false')'''



# Get prime numbers:

# Method 1


def primes (num):
  p = 0
  #for x in range (2, num+1):
  for x in range (num):
    #for y in range (2,(num//2)+1): 
     for y in range (2,x): 
          if (x % y) ==0:
             break
     else:
         p+=1
  return p
print(primes(10))

# Method 2

def is_prime(num):
   if num==0 or num ==1:
      return 0
   elif num == 2:
      return 1
   else:
        for y in range (2,(num//2)+1): 
           if num % y == 0:
              return 0
           else:
              pass
           return 1

def total_prime(max_num):
    u = 0
    for i in range (0,max_num+1):
        if is_prime(i):
           u = u+1
    return u



print(total_prime(12))
#print(is_prime(5))





'''PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter

print_big('a')

out:   *  
      * *
     *****
     *   *
     *   *

HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
For purposes of this exercise, it's ok if your dictionary stops at "E".'''


def print_big(letter):
    patterns = {1:'     *      ', 2:'   *    *   ' ,3:'*         *',4:'  *   *   *   ',5:' *         * '}

    alphabet = {'A':[1,2,4,5], 'B':[3,4,5,1]}

    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
print_big('A')












