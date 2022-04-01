
#Q1
out = (9**2)+((15/2)*3)-1.75
print(out)

print(type( 3 + 1.5 + 4))

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

list4 = [5,3,4,6,1]
list4.sort()
print(list4)

l1 = [0,0,0]
print(l1)

l2 = [0] * 3
print(l2)


d = {'simple_key':'hello'}
print(d['simple_key'])


d1 = {'k1':{'k2':'hello'}}
print(d1['k1']['k2'])

d2 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d2['k1'][0]['nest_key'][1][0])


d3 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d3['k1'][2]['k2'][1]['tough'][2][0])


list5 = [1,2,2,33,4,4,11,22,3,3,2]

print(set(list5))


print(4**0.5 != 2)
print(3.0 == 3)

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
print(l_one[2][0] >= l_two[2]['k1'])


