

mystr = 'oldmacdonanld'
x = list(mystr.capitalize())
x[3] = x[3].upper()
print(x)

str1 = ''
for letter in x:
    str1 = str1 + letter
print (str1)




#MASTER YODA: Given a sentence, return a sentence with the words reversed

# Here we have addressed 2 methods to convert a list back into string/ sentence

def sent_rev(sent):
#sent = ' I am Rose'
    reversed_sent = ''
    sent_list = sent.split()
    #print(sent_list)
    sent_list.reverse()
    #for idx in range(len(sent_list)):
        #reversed_sent = reversed_sent + sent_list[idx]+' '
    #return reversed_sent

    reversed_sent = " ".join(sent_list)
    return(reversed_sent)

reversed_sentence = sent_rev('I am Rose')
print(reversed_sentence)



# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def within_ten(num):
    
    if abs( 100-num) <=10 or abs(200-num) <=10:
       return True
    else:
       return False

ans = within_ten(90)
print(ans)
       





