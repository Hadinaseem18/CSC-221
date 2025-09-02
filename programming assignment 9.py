#Muhammad Hadi Naseem
#CSC221
#progrsmming assignment 9
#11/7/2024

#input
total = int(input("Enter the amount of names you want:"))      
results=[]
n=0
while n<total:
        name=input("write names:")
        n=n+1
        lower_name=name.lower()
#process+output
        g_count=name.count('g')
        e_count=name.count('e')

        if g_count>e_count:
            result="is good"
        elif g_count < e_count:
            result="is EVIL"
        else:
            result= "NEITHER"
        
        results.append(f"{name} is {result}")
print("\n".join(results))
                

    
    



