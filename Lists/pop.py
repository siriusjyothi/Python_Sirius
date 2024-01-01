# pop is used to remove one element at end of the list. 
l1 = [10,20,30]
l1.pop()
print(l1)
# l1.pop[0] # if we use [] for index to remove element it is throwing error TypeError: 'builtin_function_or_method' object is not subscriptable
l1.pop(0)
print(l1) # if we use () for index to remove element it is working correctly
l3 = [int,float,str,bool,complex,range,list,dict,tuple]
print(l3) # [<class 'int'>, <class 'float'>, <class 'str'>, <class 'bool'>, <class 'complex'>, <class 'range'>, <class 'list'>, <class 'dict'>, <class 'tuple'>]
# o/p  looks something like this it says that im taking them as classes
# l4 = [int(),float(),str(),bool(),complex(),range(),list(),dict(),tuple()]
#print(l4)
 # l4 = [int(),float(),str(),bool(),complex(),range(),list(),dict(),tuple()]

# TypeError: range expected at least 1 argument, got 0 

l4 = [int(),float(),str(),bool(),complex(),range(0),list(),dict] # we need give 0 for range default
print(l4) # [0, 0.0, '', False, 0j, range(0, 0), [], <class 'dict'>]o/p will give default values of datatypes

