#Write a program to develop a movie recommendation system based on reviews. Take 10 reviews from
#user as input using keywords good, excellent, worst, poor, bad, outstanding, time waste etc. Based
#on reviews categorize number of positive and negative reviews.
  # For equal number of  positive and negative reviews --> 1 time watch movie
  #Positive --> Display  "Must Watch"
  #Negative --> Display "Don't Watch"

movie_name = input("Enter name of movie : ")
good=bad=fair=average=0
n=int(input("Enter the number of reviews you want : "))
for i in range(0,n):
    a=input("Enter your review : ")

if(a.title()=='Good' or a.title()=='Outstanding' or a.title()=='Excellent' or a.title()=='Awesome' or a.title()=='Nice'):
    good=good+1
elif(a.title()=='Ok' or a.title()=='Average' or a.title()=='Fair'):
    average=average+1
elif(a.title()=='Boring' or a.title()=='Bad' or a.title()=='Worst' or a.title()=='Poor'):
    bad=bad+1
if(good>bad and good>average):
    print("Nice Movie must watch")
elif((average>bad and average>good) or (good==average and bad<good)):
    print("Average movie")
elif((bad>good and bad>average) or (bad==average and bad>good)):
    print("Waste of time..Don't Wacth")