def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def run():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while(at_goal() == False):
      run()

#for val in range(0,6):
    #run()
    

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
