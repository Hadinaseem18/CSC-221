#in class excercise 4
#Muhammad Hadi Naseem
#10/03/24

#input
month = int(input("Enter the month of birth: "))
day = int(input("Enter the day of birth: "))

sign = ""


#process
if (month==3 and 21<=day<=31)or(month==4 and 1<=day<=20):
          sign = "Aries!"
elif (month==4 and 21<=day<=30)or(month==5 and 1<=day<=20):
          sign = "Taurus!"
elif (month==5 and 21<=day<=31)or(month==6 and 1<=day<=20):
          sign = "Gemini!"
elif (month==6 and 21<=day<=30)or(month==7 and 1<=day<=21):
          sign = "Cancer!"
elif (month==7 and 22<=day<=31)or(month==8 and 1<=day<=21):
          sign = "Leo!"
elif (month==8 and 22<=day<=31)or(month==9 and 1<=day<=21):
          sign = "Virgo!"
elif (month==9 and 22<=day<=30)or(month==10 and 1<=day<=21):
          sign = "Libra!"
elif (month==10 and 22<=day<=31)or(month==11 and 1<=day<=21):
          sign = "Scorpio!"
elif (month==11 and 22<=day<=30)or(month==12 and 1<=day<=21):
          sign = "Sagittarius!"
elif (month==12 and 22<=day<=31)or(month==1 and 1<=day<=20):
          sign = "Capricorn!"
elif (month==1 and 21<=day<=31)or(month==2 and 1<=day<=19):
          sign = "Aquarius!"
elif (month==2 and 20<=day<=29)or(month==3 and 1<=day<=20):
          sign = "Pisces!"


#output
print("You are a",sign)
