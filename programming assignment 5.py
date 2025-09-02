#programming assignment 5
#Muhammad Hadi naseem
#10/10/24

#input + process
r=0
b=0
y=0

while True:
    color=input("Enter a color: ")
    if color=='q':
        break
    elif color=='r':
        r=r+1
    elif color=='y':
        y=y+1
    elif color=='b':
        b=b+1
    else:
        print("Invalid input!")
    


T= r+y+b


#output
print(f"{r} red\n{y} yellow\n{b} blue")
print(f"{T} total")

#Extra Credit   
max=0
if(max<r):
    max=r
if(max<b):
    max=b
if(max<y):
    max=y

if(max==r):
    print("The winning color is red!")
elif(max==b):
    print("The winning color is blue!")
elif(max==y):
    print("The winning color is yellow!")

    
         
    




