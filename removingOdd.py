#Write a program to print a list after removing all the odd elements.
# list with EVEN and ODD number
list = [11, 22, 33, 44, 55]

# print original list
print ("Original list:", list)

# loop to traverse each element in the list
# and, remove elements
# which are ODD (not divisible by 2)
for i  in list:
	if(i%2 != 0):
	    list.remove(i)

# print list after removing ODD elements
print ("list after removing ODD numbers:", list)