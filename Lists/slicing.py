l1 = [10,20,30,40,50,10,30,50]
l2 = [10,20,30,40,50]
print(l1+l2)# [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
l3 = ['h','e','l','l','o']
l4 = ['w','o','r','l','d']
print(l3+l4) #['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

# slicing start:end(-1),jump or default
# l1 = [10,20,30,40,50]
# print(l1.index[2]+l2.index[2])

print(l3)
print(l3[3])
print(l3[1:4]) # ['e', 'l', 'l']
print(l3[1:4:2]) # ['e', 'l']
print(l3[::]) # ['h', 'e', 'l', 'l', 'o']
# inorder to delete duplicates we can convert list into set..set will not take default values
print(l1)
l5 = set(l1)
print(l5)


