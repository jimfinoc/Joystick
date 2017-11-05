import pygame
pygame.init()
pygame.joystick.init()

### Tells the number of joysticks/error detection
joystick_count = pygame.joystick.get_count()
print "Number of joysticks detected: ", joystick_count
if joystick_count == 0:
    print "Error, I did not find any joysticks"
else:
    my_joystick=pygame.joystick.Joystick(0)
    my_joystick.init()
    axis_count = my_joystick.get_numaxes()
    print "Number of axes:", axis_count
    buttons_count = my_joystick.get_numbuttons()
    print "Number of buttons:", buttons_count
