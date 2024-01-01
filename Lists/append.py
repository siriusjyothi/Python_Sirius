l1 = [10,20,30]
l2 = [40,60,70]
print(l1 , l2)
l2[2] = 20
print(l2)
l1.append(60) # append is used to add one element at a time at the end of the list it will not take mulitple elements
l2.append(90)
print(l1 )
print(l2)
l3 = ["nameone", "nametwo", "namethree"]
print(l3)
l4 = ["namefour", ["namefive", "namesix"]] # this is nested list of names we cannot append nested list and it is counted as one number
l3.append("nameeight")
l4.append("nameeight")
print(l3)
print(l4)
print(l3[0]) # using indexes to get particular element
print(l4[1])
# l4.append("namenine", "nametwo") # TypeError: list.append() takes exactly one argument (2 given) since we cannot add muliple elements in one shot
print(l4[1])
l4[1]  = ["nameone", "nametwo", "namethree"]
print(l4)
l4[1][0] = "nameten" # we can insert particular element with index even in nested lists too
print(l4)
print(len(l4)) # prints length of list