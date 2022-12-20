#Write a program to remove duplicate elements of list.

my_list = [1,2,3,1,2,2,4,4,5,4,6,2]
print("List befor : ", my_list)
temp_list = []

for i in my_list :
    if i not in temp_list:
        temp_list.append(i)
        
my_list = temp_list

print("List After removing duplicate ", my_list)