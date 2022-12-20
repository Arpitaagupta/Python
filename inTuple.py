tup = [23, (11,8), 45, (5,5,33), 12, 56, 78, 0]

print("The tuple is : ")
print(tup)
N = int(input("Enter the value to check whether tuple contains it or not : "))

result = False
for elem in tup :
   if N == elem :
      my_result = True
      break
print("Does the tuple contain the value mentioned ?")
print(result)