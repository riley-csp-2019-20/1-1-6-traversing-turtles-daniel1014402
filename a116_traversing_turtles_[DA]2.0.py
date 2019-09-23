#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  my_turtles.append(t)

#  
start_x = 0
start_y = 0

#
for t in my_turtles:
	t.goto(start_x, start_y)
	t.pendown()
	t.right(45)    
	t.forward(50)
	start_x=t.xcor()
	start_y=t.ycor()
	turtle_shapes=turtle_colors.pop()


#	
	start_x = start_x + 50
	start_y = start_y + 50

wn = trtl.Screen()
wn.mainloop()