


################################
mylist = list(range(0,11,2))
print(mylist)



###################################

out = [num for num in range(1,51) if (num % 3==0) ]
print(out)

##################################


mylistt = []
for numb in range(1,101):
    if (numb%3==0 and numb%5!=0):
       mylistt.append('Fizz')
       #print ('Fizz')
    elif numb%5 == 0 and numb%3 !=0:
       #print ('Buzz')
       mylistt.append('Buzz')
    elif (numb%3 == 0 and numb%5 == 0):
       #print('FizzBuzz')
       mylistt.append('FizzBuzz')
    else:
       #print(numb)
       mylistt.append(numb)

print(mylistt)



######################################



st = 'Sprint only the words that start with s in this sentence'

bb = st.split()
print(bb)

for word in bb:
    if(word[0] =='s' or word[0] =='S'):
       print(word)


#####################################

st1 = 'Print every word in this sentence that has an even number of letters'

cc = st1.split()
print(cc)

for word in cc:
    if len(word) %2 == 0:
       print(word)



#############################################



sentence = 'Create a list of the first letters of every word in this string'

Mlist = sentence.split()

#Mlist = ['Create','a','list','of'...]

#Letter_list = []

#for word in Mlist:
        #Letter_list.append(word[0])
#print(Letter_list)

New_list = [word[0] for word in Mlist]
print(New_list)


################################################



