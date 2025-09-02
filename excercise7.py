#in class excercise 7
#Muhammad Hadi Naseem
#10/24/2024


def isprime(n):
    if n==0 or n==1:
        return False
    if n==2:
        return True
    #general case
    for m in range(2,n//2+1):
        if n%m==0:
            return False
    return True

    
def main():

     #input
     n = int(input("How many prime numbers do you want:"))

     #process + output
     print("The first",n,"prime numbers are: ")
     i=2
     num=0
     while num<n:
         if isprime(i):
             print(i)
             num=num+1
         i=i+1

main()

