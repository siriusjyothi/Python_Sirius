l1 = [10,20,30,40]
print(l1.index(30))
l2 = [30,10,20,50,10,20]
print(l2.index(10)) # 1 i.e first indexspot , what if we have duplicate values which index value will it fetch, first index of that element
# note index(element,start,end) from where to where you want to find the index of partcular element
print(l2.index(10,4)) # after 4 th index in which spot we have 10 i.e 4th indexspot
print(l2.index(10,0,5))