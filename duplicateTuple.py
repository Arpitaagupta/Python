# Python3 code to demonstrate working of
# Removing duplicates from tuple
# using tuple() + set()
 
# initialize tuple
tup = [1, 3, 5, (5,6), (8,9,3), 2, 3, 5, 1, 1, 3, (5,6)]
 
# printing original tuple
print("The original tuple is : " + str(tup))
 
# Removing duplicates from tuple
# using tuple() + set()
res = tuple(set(tup))
 
# printing result
print("The tuple after removing duplicates : " + str(res))