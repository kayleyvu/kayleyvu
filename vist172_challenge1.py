############################# 
# Challenge 1  
# VIST 172
# Kayley Vu, September 8 2023
#############################

#libraries
from turtle import * 
import random 

#create screen 
s = Screen() #get screen 
setup(600,600) #window dimensions 
title('Challenge 1: Kayley Vu') #screen title 
s.bgcolor('black') #screen background color 

#turtle settings
t = Turtle()
t.shape('turtle')
speed(speed='fastest')

#world coordinates 
setworldcoordinates(-10,-10,10,10) 

#random colored spiraling squares
def createspiral(): 
    for i in range(num_sq): 
        colormode(255) 

        #choose rand int betw 0 and 255 to gen rand rgb values 
        a=random.randint(0,255)
        b=random.randint(0,255)
        c=random.randint(0,255)

        #set outline and fill color 
        pencolor('white')
        fillcolor(a,b,c)
        d=random.randint(0,6) #random line thickness
        width(d)


        #begin filling squares
        begin_fill()

        #loop to draw each square 
        for j in range(4): 
            #each side of square with length 5
            fd(5)

            #turn 90 deg right
            rt(90)

        #end color fill
        end_fill()
    
        #turn deg for next square 
        rt(12)
 
while True:
    #user chooses number of squares 
    num_sq = numinput('Spiraling Squares','How many squares (10-50):',30,minval=10,maxval=50)
    num_sq = int(num_sq)

    #call spiral function
    createspiral()

    #try again
    tryagain=textinput('again?','Try again? yes/no:')
    if tryagain=='yes':
        #clear screen
        clear()
    
    else:
        ht() #hide turtle 
        penup()
        setposition(0,8)
        write('Bye!',move=False,align='center',font=('Arial',15,'normal'))
        done()


