import turtle
#Insert variable here
turtle.penup () #Pick up the pen so it doesn't draw
turtle.goto (0,0) #move the turtle to the
#position, -200, -100,on
#the screen
turtle.pendown() #put the pen down to start
#Drawing
#Draw the square:
turtle.goto(0,100)
turtle.goto (100,100)
turtle.goto (100,0)
turtle.goto (0,0)
#...and end it before the next line.
side_length=100
turtle.goto(0,side_length)
tutle.goto (100,side_length)
turtle.goto (100,side_length)
turtle.goto (0,side_length)
turtle.mainloop()
