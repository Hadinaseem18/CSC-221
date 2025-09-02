#in class excercise 10
#Muhammad Hadi Naseem
#CSC221
#11/14/2024


#input
numbers=[]
numberstring=input()
numbers=numberstring.split()
numbers=[int(n) for n in numbers]



#process
s1=numbers[0] #first smallest number
s2=2**100 #second smallest number

for n in numbers:
    if n<s1: #finding new smallest number
        s2=s1#orginal smallest number become the second smallest
        s1=n#new smallest number
    if s1<n<s2:#finding second smallest number
        s2=n#new second smallest number

#output
print(s1,"and",s2)

        

