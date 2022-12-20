my_tuple_1 = (23, 45, 12, 56, 78, 0)

print("The first tuple is : ")
print(my_tuple_1)
N = 12
print("The value of 'N' has been initialized")

my_result = False
for elem in my_tuple_1 :
   if N == elem :
      my_result = True
      break
print("Does the tuple contain the value mentioned ?")
print(my_result)