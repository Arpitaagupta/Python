# Python3 code to demonstrate working of
# K Multiple Elements Tuples
# Using list comprehension + all()
  
# initializing list
test_list = [(6, 24, 12), (7, 9, 6), (12, 18, 21)]
  
# printing original list
print("The original list is : " + str(test_list))
  
# initializing K
K = 6
  
# all() used to filter elements
res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]
  
# printing result
print("K Multiple elements tuples : " + str(res))