#in class exxcercise 3
#Muhammad Hadi Naseem 
#10/1/24

#input
year = int(input("Enter a year: "))

flag = True #flag true- leap year     false-common year


#process
#Solution1
'''
if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)
'''
'''
if  year%4!=0:
    flag=False
elif  year%100!=0:
    flag=True
elif  year%400!=0:
    flag=False
else:
    flag=True
'''  


#Solution2
#Leap years are those years that are divisible by four
#except that century years not divisible by 400 are not leap years

if year%4==0:
    flag=True
    if year%100==0 and year%400!=0:
        flag=False
else:
    flag=False



#output
if  flag==True:
    print(year,"is a leap year")
else:
    print(year,"is NOT a leap year")
