"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Wesley Derflinger.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.

import rosegraphics as rg

window = rg.TurtleWindow()

green_turtle = rg.SimpleTurtle('turtle')
green_turtle.pen = rg.Pen('green', 3)
green_turtle.speed = 1

wes_turtle = rg.SimpleTurtle('turtle')
wes_turtle.pen = rg.Pen('orange', 5)
wes_turtle.speed = 5

size_1 = 300
size_2 = 150

for k in range(5):

    green_turtle.draw_square(size_1)
    wes_turtle.draw_square(size_2)
    green_turtle.pen_up()
    wes_turtle.pen_up()
    green_turtle.backward(45)
    wes_turtle.forward(45)
    green_turtle.forward(10)
    wes_turtle.backward(10)
    green_turtle.left(45)
    wes_turtle.right(45)
    green_turtle.pen_down()
    wes_turtle.pen_down()
    size_1 = size_1 - 12
    size_2 = size_2 - 5


window.close_on_mouse_click()
########################################################################
