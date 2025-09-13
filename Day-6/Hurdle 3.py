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
    if wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    elif front_is_clear():
        move()
            

#for val in range(0,6):
    #run()
    

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
