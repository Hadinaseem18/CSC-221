#programming assignment 2
#Muhammad Hadi Naseem
#9/20/24

#input
male_students = int(input("Enter the number of male students:"))
female_students = int(input("Enter the number of female students:"))


#process
n = male_students/(male_students+female_students)*100
m = female_students/(male_students+female_students)*100





#output
print(f"Male percent:{n:.1f}%")
print(f"Female percent:{m:.1f}%")
