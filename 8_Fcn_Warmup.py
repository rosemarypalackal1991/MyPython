


######### To display alternate lower and upper casing for string#########

def myfunc(my_string):
 stringg = ''
 for idx in range(len(my_string)):
      if idx % 2 == 0:
         stringg = stringg + my_string[idx].lower()
      else:
         stringg = stringg + my_string[idx].upper()
 return(stringg)


h = myfunc('Execute')


############LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd




def myfunc(num1,num2):
    if num1%2==0 and num2%2==0:
       return min(num1,num2)
    else:
       return max(num1,num2)

num = myfunc(1,3)

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(input_string):  
    myString = input_string.split()
    if myString[0][0] == myString[1][0]:
       return True
    else:
       return False


t = animal_crackers('Levelheaded Llama')


#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty (int1, int2):
    if int1+int2==20 or int1==20 or int2==20:
       return(True)
    else:
       return(False)

x = makes_twenty(10,10)
print(x)




    

        
           
           
