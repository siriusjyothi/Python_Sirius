# extend() is a methos where you can add multiple   elements at end of a list.
l1 = [10,20,30]
# l1.extend(90,70,80) # TypeError: list.extend() takes exactly one argument (3 given) if w epass elements with paranthasis it wil throw an exception.
l1.extend([90,80,70]) # we need to use squarebrackets instead of () to add multiple elements at a time
print(l1)
l2 = ["nameone"]
l2.extend("nametwo")
print(l2) # ['nameone', 'n', 'a', 'm', 'e', 't', 'w', 'o'] this is the o/p if dont use []
l2.extend(["namethree"])
print(l2) # ['nameone', 'n', 'a', 'm', 'e', 't', 'w', 'o', 'namethree']

