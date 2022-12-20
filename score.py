score = input("Enter Score in between 0.0 to 1.0 : ")
s=float(score)
if(s>=0.9 and s<=1.0):
    print("Grade is A")
elif(s>=0.8 and s<0.9):
    print("Grade is B")
elif(s>=0.7 and s<0.8):
    print("Grade is C")
elif(s>=0.6 and s<0.7):
    print("Grade is D")
elif(s>=0.0 and s<0.6):
    print("Grade is F")
else:
    print("Error")

