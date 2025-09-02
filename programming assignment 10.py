#programming assignment 10
#Muhammad Hadi Naseem
#CSC221
#11/17/20

#input
scores=[]
score = int(input("How many scores?"))
n=0
while n<score:
    score_input = float(input("Enter a score:"))
    n=n+1
    scores.append(score_input)


    

#process

#average score
average_sum = sum(scores)
average_score = average_sum/score
print("The average score is",average_score)

#Highest score
h1=scores[0] #highest score
for n in scores:
    if n>h1:
        h1=n
print(f"The highest score is {h1:.0f}")  

#below average + above average
for n in scores:
    if n < average_score:
        cal_below_average = average_score - n
        print(f"{n} is below average by {cal_below_average:.2f}")
    elif n>average_score:
        cal_above_average = n - average_score
        print(f"{n} is above average by {cal_above_average:.2f}")
    else:
        print(n,"is a average score")
    
        

        





