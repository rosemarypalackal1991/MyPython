

# Has 33

'''def has_33(my_list):
    for idx in range(len(my_list)):
        if idx ==0:
           continue
        else:
           if my_list[idx]==3 and my_list[idx-1]==3:
              return True
           else:
              pass
        return False


x = has_33([1, 1, 3])
print(x)


list = ['H']
y = 3* list
print(y)'''



# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

'''def paper_doll(input_str):
    mylist = list(input_str)
    str1 = ''
    new_list = []
    for letter in mylist:
       new_list.append(letter*3)
    for word in new_list:
       str1 = str1+word
    return str1

z = paper_doll('Mississippi')
print(z)'''



# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an #eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

#blackjack(5,6,7) --> 18
#blackjack(9,9,9) --> 'BUST'
#blackjack(9,9,11) --> 19


'''def blackjack(num1,num2,num3):
    sum1 = num1+num2+num3
    if sum1 <= 21:
       return sum1
    elif sum1 >21 and (num1 == 11 or num2 ==11 or num3 ==11):
       if (sum1-10)<=21:
          return sum1 - 10
       else:
          return 'BUST'
    else:
       return 'BUST'

b = blackjack(6,5,7)
print(b)'''



#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 #will be followed by at least one 9). Return 0 for no numbers.

#summer_69([1, 3, 5]) --> 9
#summer_69([4, 5, 6, 7, 8, 9]) --> 9
#summer_69([2, 1, 6, 9, 11]) --> 14


'''def summer_69 (input_list):
#input_list = [4,5,6,7,5,4,6,8,9,3,5,9,10]
    if 6 in input_list:
      sixes = [i for i, e in enumerate(input_list) if e == 6] 
      nines = [i for i,e in enumerate(input_list) if e == 9]
      del input_list[min(sixes):max(nines)+1]
      print(input_list)
      return sum(input_list)
    elif input_list == []:
      return 0
    else:
      return sum(input_list)


s69 = summer_69([4, 5, 6, 7, 8, 9])
print(s69)'''
        


input_list = [10,10,10,6,10,6,9,6,10,10,9,10,9,10]
'''summation = 0
add = True
for num in input_list: 
    if add == True:     
         if num !=6:
            summation = summation +num
         else:
            add = False                
    else:
         if num ==9:
            add = True           
print(summation)'''


total = 0
add = True

for num in input_list:
    while add:
          if num!=6:
             total +=num
             break
          else:
             add = False
    while not add:
          if num!=9:
             break
          else:
             add = True
             break
print(total)













          



       




        
    


        


