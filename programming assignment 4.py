#programming assignment 4
#Muhammad Hadi Naseem
#10/5/2024

#input
packages = int(input("Enter the number of packages: "))


#process
discount=0

if  0<=packages<=9:
    discount=0
elif 10<=packages<=19:
    discount=10
elif 20<=packages<=49:
    discount=20
elif 50<=packages<=99:
    discount=30
elif packages>=100:
    discount=40
    
n = (99-(99/100*discount))*packages
m = (99/100*discount)*packages
    
    
    

    


#output
print(f"Amount of discount:{m:.1f}")
print(f"Total amount after discount:{n:.1f}")
