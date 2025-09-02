#CSC221
#Muhammad Hadi Naseem
#10/17/2024

#input
size = int(input("Enter the size of triangle: "))

#process + output
for i in range (size):
    for j in range(2*i+1):
        print("*",end="")
    print()
