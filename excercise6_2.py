#in class excercise 6 Q2
#Muhammad Hadi Naseem
#CSC221
#10/20/2024

def is_leap_year(year):
    if year%4!=0:
        flag=False
    elif year%100!=0:
        flag=True
    elif year%400!=0:
        flag=True
    else:
        flag=True
    return flag

def main():
    year=int(input("Enter a year (0 to stop):"))
    #input
    while year!=0:
    #process + output
        if is_leap_year(year):
            print(year,"is a leap year!")
        else:
            print(year,"is NOT a leap year!")

        year=int(input("Enter a year(0 to stop):"))

    print("Bye")

main()
            
           
       
            

   
