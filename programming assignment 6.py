#progrsmming assignment 6
#Muhammad Hadi Naseem
#10/22/2024

#input
number=int(input("Enter a stopping number: "))

#process + output
for i in range(1,number+1):
    for j in range(i, number+1):
        if i==j and i != 1:
            print()

        print(f"{i} * {j} = {i*j}")
    
