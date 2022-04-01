


# Write a function that computes the volume of a sphere given its radius.

def volume (radius):
    return ((4.0/3.0)* (22.0/7.0) *(radius)**3)

print(volume (2))



# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    return num>=low and num<=high

print ran_check(0,1,3)




'''Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33

HINT: Two string methods that might prove useful: .isupper() and .islower()

If you feel ambitious, explore the Collections module to solve this problem!'''
def add_letters (mystr):
    upper = 0
    lower = 0
    for letter in mystr:
        if letter.isupper():
           upper+=1
        elif letter.islower():
           lower+=1
        else:
           continue
    print('No.of Upper case characters = {}'.format(upper))
    print('No.of Lower case characters = {}'.format(lower))
    return(upper,lower)

add_letters('Hello Mr. Rogers, how are you this fine Tuesday?')

(upper,lower) = add_letters('Hello Mr. Rogers, how are you this fine Tuesday?')
print(upper)



# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


def unique_list (mylist):
    return list(set(mylist))

a = unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
print (a)



'''Write a Python function to multiply all the numbers in a list.
Sample List : [1, 2, 3, -4]
Expected Output : -24'''


def multiply (mylist):
    num = 1
    for i in range(0, len(mylist)):
        num = num* mylist[i]
    return num

print(multiply([1, 2, 3, -4]))



'''
Write a Python function that checks whether a word or phrase is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.'''


def palindrome(mystr):
    x = mystr.replace(' ','').lower()
    y = x[::-1]
    return x == y

t = (palindrome('nurses run'))
print(t)



'''
Hard:

Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

'''

import string
x = list(string.ascii_lowercase)
print(x)

mystr = "The quick brown fox jumps over the lazy dog"
y = list(set(mystr.replace(' ','').lower()))
print(y)

if sorted(x) == sorted(y):
   print(True)
else:
   print (False)

