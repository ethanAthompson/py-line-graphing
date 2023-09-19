#here I import all of my modules that I need 
#and shorten all of the long modules

from os import system, name
import time
from random import randint
import random
from datetime import date
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#BBS ID

today = date.today()#this date module returns a date and it is
#being contained by the today value.

CurrentDate = today.strftime("%B %d, %Y ") #I am formatting the currentn date
#using the strftime method I can format the date in python because strftime converts the date object to a string date.
print("Today is {}".format(CurrentDate)) # her I format my date using the format method into the sentence

def MainPage():#my MainPage function
    
    def Title(Title = "APP:"): #I am defining a function and putting in a parameter which I then call by putting in GraphMaker because it is my title
        #I put Title = "APP" as a place holder for my actual title
        print("Your" + Title)#I am putting my Title variable here so then I can replace it with the graphmaker which is the title  I want
    Title("GraphMaker:")#I call my function with the parameter in it
    

    def GraphingNow():#I am defining the function responsible for my graphing
        print("")#an empty space
        print("Graph Customization")#This is the title of my graph
        Option_1 = input("do you want to customize your graph? Y/N: ") #My option choice deciding if you want to
            #proceed in creating your graph or no
            
            #if you input  from the following y,Y, yes, Yes then it will try the following code
        if Option_1 == 'y' or Option_1 == 'Y':  # you answer in Y,y then it will do the following
            try:#I am using try and except for this part because I want to locate the errors you make and restart 
                print("")#empty space
                print("|Customizable Graph|")#this is so you know which graph your making
                print("")#empty space
                print("Enter your X coords follow by a space EX: 1 5 6 8 etc") #tells you the instructions to the program
               
                X_Coords = [int(X_Coords) for X_Coords in input("Enter X Coordinates: ").split(" ")] #this here is where my program can allow you to enter in your numbers followed by the space
                    #I use .split so all of your inputs stay on a single line
                    #I used type casting to convert your number that starts out a string into a integer. and for how many numbers you input
                    #it will continue forever unless you mess up, Also it will be printed out into a list
                    #this would allow python to have you accept the N amount of numbers you input
                    
                print(X_Coords)#right here I print out X_Coords or your numbers, printed into a list so matplotib can take that input
                print("")#empty space
                
                print("Enter your Y Coords follow by a space EX: 2 10 30 etc") #tells you instruction to the program
                Y_Coords = [int(Y_Coords) for Y_Coords in input("Enter Y Coordinates: ").split(" ")]
                #I use .split so all of your inputs stay on a single line
                #right here I print out Y_Coords or your numbers, printed into a list so matplotib can take that input
                    #A variable is containing information about the coordinates you input, I use type casting for Y_Coords so
                    #python can convert your number into a integer because your input would normally be a string. And for the loop
                    #in input("Enter Y Coordinates: "), it will convert all of your numbers to a int and into a list
                    
                print(Y_Coords)#prints out the list 
                print("Your Coordinates Above ^")#I used a print statement to display your coordinates above sign
                if len(X_Coords) != len(Y_Coords): #If the length of your X_Coordinates is not the same as the length of your Y_Coordinates 
                        #then it will Restart the graphing process
                        print("Coordinate is Not similar length")#tells you that the coordinates are not of same length
                        GraphingNow()#I am calling my graphing function so I can restart when lengths of both coordinates are not equal
                        
                        
                #Graphing Name(C1)
                    #I use 3 user inputs that will be converted into a string because these are your titles/labels for
                    #your graph
                Title_Choice = str(input("Your Graph Title is: ")) 
                X_Label_Choice = str(input("Label your X Values as: "))
                Y_Label_Choice = str(input("Label your Y Values as: "))
                    
                #Color Choices(C2)
                    #below are your Color choices that are a list of information which you can take and the graph will make
                    #the line of your graph the color you choose
                Colors = ['blue','green','red','cyan','magenta','black','yellow']
                print(Colors)#I print out my list
                Color_Choice = str(input("Choose a Color: "))#this user input will convert your answer into a string
                    #for example if you put blue then it will make the line that color
                     
                #LineStyle Choices(C3)
                Line_Styles = [None,'dashed','solid']#Linestyles variable is responsible for holding 3  options you can have to style your line graph
                print(Line_Styles)#I print my list for user to see
                Line_Choice = input("Choose a linestyle for your graph: ") #I was thinking of putting str() type casting but I need the person to type in None which is a boolean.
                    #this will allow you to input from what you see in the list above
                    
                #MarkerC Choices(C4)
                
                Marker_Choice = ['o',None,'X','+','*','_','|']#MarkerChoice containing my list of markers
                print(Marker_Choice)#I am displaying the list that is the MarkerChocie variable
                Choose_Marker = input("Enter a Marker for your graph: ")
                
            except ValueError:#I put this except because it is needed after a try statement become I am testing for errors
                    #the biggest error is the Value error because C1,C2,C3,C4 have no numbers and to locate others
                print("Try Again:") #Prints try again
                GraphingNow()#then it restarts to the top of the function
                    
                    
                #plt is short for matplotlib.pyplot and I am plotting 
                #the letters you input into your graph
            plt.title(Title_Choice)#your title name
            plt.xlabel(X_Label_Choice)#Your X Label name
            plt.ylabel(Y_Label_Choice)#your Y label name
                #this here is the plotting for the graph your making
            plt.plot(X_Coords,Y_Coords, marker = Choose_Marker, color = Color_Choice, linestyle = Line_Choice)
                #in matplotlib they said they will fix the Capitalization of the first letters of (m)arker,(c)olor, etc in their next update
            plt.grid()#this is the default grid it will display under your graph
            plt.show() #this basically shows your graph/displays it
            GraphingNow()

        elif Option_1 == 'n' or Option_1 == 'N' or Option_1 == '': 
            try:
                print("")#empty space
                print("|Default Graph|")#tells you your default graph
                print("")#empty space
                print("Enter your X coords follow by a space EX: 1 5 6 8 etc") #tells you the instructions to the program
                X_Coords = [int(X_Coords) for X_Coords in input("Enter X Coordinates: ").split(" ")] 
                #I use .split so all of your inputs stay on a single line
                #this here is where my program can allow you to enter in your numbers followed by the space
                    #I used type casting to convert your number that starts out a string into a integer. and for how many numbers you input
                    #it will continue forever unless you mess up, Also it will be printed out into a list
                    #normally the for loop would be like
                    
                    #[for x_Coords in input("Enter X Coordinates: ")
                    #print(X_Coords)]
                
                    #this would allow python to have you accept the N amount of numbers you input
                    
                print(X_Coords)#right here I print out X_Coords or your numbers, printed into a list so matplotib can take that input
                print("")#empty space
                print("Enter your Y Coords follow by a space EX: 2 10 30 etc") #tells you instruction to the program
                Y_Coords = [int(Y_Coords) for Y_Coords in input("Enter Y Coordinates: ").split()]
                #I use .split so all of your inputs stay on a single line
                #right here I print out Y_Coords or your numbers, printed into a list so matplotib can take that input
                    #A variable is containing information about the coordinates you input, I use type casting for Y_Coords so
                    #python can convert your number into a integer because your input would normally be a string. And for the loop
                    #in input("Enter Y Coordinates: "), it will convert all of your numbers to a int and into a list
                    
                print(Y_Coords)#prints out the list 
                print("Your Coordinates Above ^")#I used a print statement to display your coordinates above sign
                if len(X_Coords) != len(Y_Coords): #If the length of your X_Coordinates is not the same as the length of your Y_Coordinates 
                        #then it will Restart the graphing process
                    GraphingNow()#I am calling my graphing function so I can restart when lengths of both coordinates are not equal
                    
                print("Creating Default Graph Display..")#tells you that python is creating your default graph since you didnt want to customize one
                time.sleep(1)#allows python to wait for a second
                print("Your Graph is Made")#Tells you your graph is made
                    
                    #the default graph settings
                plt.title("Default Graph")#your title name
                plt.xlabel("X-Axis")#Your X Label name
                plt.ylabel("Y-Axis")#your Y label name
                plt.plot(X_Coords,Y_Coords, marker = 'o', color = 'black', linestyle = 'solid')
                plt.grid()#this is the default grid it will display under your graph
                plt.show() #this basically shows your graph/displays it
                GraphingNow()
            except ValueError:
                GraphingNow()#I am calling my function
        
        else:
            GraphingNow()
            
            
    GraphingNow()
  

MainPage()
