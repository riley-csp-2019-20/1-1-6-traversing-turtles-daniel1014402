#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic","triangle","turtle"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","purple","pink"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color=turtle_colors.pop()
  t.fillcolor(new_color)
  my_turtles.append(t)


  
  
#  
start_x = 0
start_y = 0


#

move = 1
for t in my_turtles:
	t.up()
	t.goto(start_x, start_y)
	t.down()
	t.right(45*move)
	t.forward(50)
	move = move + 1 





#	
	start_x = t.xcor()
	start_y = t.ycor()

wn = trtl.Screen()
wn.mainloop()