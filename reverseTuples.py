
# Reversing a tuple using slicing technique
# New tuple is created
def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup
      
# Driver Code
tuples = ('z','a','d','f','g','e','e','k')
print(Reverse(tuples))