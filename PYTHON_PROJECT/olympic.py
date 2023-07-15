# Program to draw the Olympic sign in Python Turtle
# Importing Turtle
import turtle

# creating object ttl for turtle
ttl = turtle.Turtle()
# setting the size of the pen to 6
ttl.pensize(6)

# creating the first or blue ring
ttl.color('blue')
ttl.penup()
# setting the x and y coordinates to -100 and -25
ttl.goto(-100, -25)
ttl.pendown()
# setting the radius of the circle to 51
ttl.circle(51)

# creating the second or black ring
ttl.color('black')
ttl.penup()
# setting the x and y coordinates to 10 and -25
ttl.goto(10, -25)
ttl.pendown()
# setting the radius of the circle to 51
ttl.circle(51)

# creating the third or red ring
ttl.color('red')
ttl.penup()
# setting the x and y coordinates to 120 and -25
ttl.goto(120, -25)
ttl.pendown()
# setting the radius of the circle to 51
ttl.circle(51)

# creating the fourth or yellow ring
ttl.color('yellow')
ttl.penup()
# setting the x and y coordinates to -45 and -75
ttl.goto(-45, -75)
ttl.pendown()
# setting the radius of the circle to 51
ttl.circle(51)

# creating the fifth or green ring
ttl.color('green')
ttl.penup()
# setting the x and y coordinates to 65 and -75
ttl.goto(65, -75)
ttl.pendown()
# setting the radius of the circle to 51
ttl.circle(51)
ttl.hideturtle()
ttl.done()