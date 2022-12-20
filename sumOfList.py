#Write a program to find the sum of all elements of an integer list.

# Python code to demonstrate the working of
# sum()
  
numbers = [1,2,3,4,5,1,4,5]
 
# start parameter is not provided
Sum = sum(numbers)
print("Sum of numbers : ", Sum)
 
# start = 10
Sum = sum(numbers, 10)
print("Sum of numbers after adding 10 : ",Sum)