
# Strings are ordered sequences
# So, they can be indexed
# Character : h   e   l   l   o
# Index     : 0   1   2   3   4
# Neg Index : 0  -4  -3  -2  -1

# Slicing
# [start:stop(not included):step]

str1 ="Hello"
str2 ='Hello World'  #white spaces are counted as characters
str3 = 'abcdefgh'

print(str1[2])    #l
print(str2[5])    #space
print(str1[-2])   # l
print(str2[1:7])  #ello W
print(str2[1:7:2])  #el     
print(str1[-4:-1])       #ell
print(str1[1:]) #ello  (till the end)

print(str3[3:6])  #def
print(str3[1:3])  #bc
print(str3[::2]) #aceg - beginnig to end in step of 2


##########REVERSE A STRING################
print(str3[::-1])  #hgfedcba


# Escape sequence

print("Hello \n World")

# length

print(len(str2))





