#in class excercise 8
#Muhammad Hadi Naseem
#11/1/2024


def main():
    instructions()
    choice = menu()
    while choice!="3":
        draw_shape(choice)
        choice=menu()
    print("Bye!")
    



#function 1 : This function describe the program and how it works
def instructions():
    print("This program will draw a diamond or a triangle")
  
#function 2 : this function will return a choice to the main
def menu():
      print("1)Draw Traingle")
      print("2)Draw Diamond")
      print("3)Quit")
      choice = input("Enter a choice:")
      while not(choice=="1" or choice=="2" or choice=="3"):
          print("Invalid input")
          choice = input("Enter a choice:")
      return choice
#function 3 : This function calls on appropriate function depending on the choice to draw a shape\
def draw_shape(choice):
    #get size of shape
    size=get_size()
    #get char of shape
    char=get_char()
    #based upon the choice, invoke either draw triangle or diamond
    if choice == "1":
        print("draw a triangle")
        draw_triangle(size,char)
    if choice == "2":
        print("draw a diamond")
        draw_diamond(size,char)
#function 4 : This function will return the size of the shape, same function for either of the shape
def get_size():
    size = int(input("Enter the size of the shape:"))
    return size

#function 5: This function will ask users to select a character that will be used to draw the shape
def get_char():
    char = input("Enter a character to be used:")
    return char

#function 6: This function draws a triangle of size size using character c
def draw_triangle(size,char):
    for i in range(size):
        for k in range(size-i-1):
            print(" ", end="")
        for j in range(2*i+1):
             print(char, end="")
        print()
    


#function 7:  This function first calls draw_triangle, then add_bottom to draw the diamond
def draw_diamond(size,char):
    draw_triangle(size,char)
    draw_bottom(size,char)


#function 8: This function draws an upside down triangle of size size-1 as the bottom of the diamond
def draw_bottom(size,char):
    for i in range(size-1):
        for j in range(i+1):
            print(" ",end="")

        for k in range(2*(size-1-i)-1):
             print(char, end="")
        print()
    
    


main()
