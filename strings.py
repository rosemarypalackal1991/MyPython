
# Strings are ordered sequences
# So, they can be indexed
# Character : h   e   l   l   o
# Index     : 0   1   2   3   4
# Neg Index : 0  -4  -3  -2  -1

# Slicing
# [start:stop(not included):step]

str1 ="Hello"
str2 ='Hello World'  #white spaces are counted as characters

print(str1[2])    #l
print(str2[5])    #space
print(str1[-2])   # l
print(str2[1:7])  #ello W
print(str2[1:7:2])  #el     
print(str1[-4:-1])       #ell

# Escape sequence

print("Hello \n World")

# length

print(len(str2))





