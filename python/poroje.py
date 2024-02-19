# import ha
import pgzrun
import os
from pgzhelper import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 1400
HEIGHT = 870
TITLE = 'Game'


# actor ha
button = Actor('sound_off' , (1300,100))

Background = Actor('background' , (500,350))

idle = Actor('idle' , (600,700))

jump = Actor('jump1' , (600,685))
jump.images = ['jump2' , 'jump3' , 'jump4' , 'jump5' , 'jump6']
jump.fps = 3

down = Actor('down1' , (600,685))
down.images = ['down2' , 'down3' , 'down4' , 'down5' , 'down6']
down.fps = 10

walk = Actor('walk1', (600,685))
walk.images = ['walk2' , 'walk3' , 'walk4' , 'walk5' , 'walk6' , 'walk7' , 'walk8' , 'walk9' , 'walk10' , 'walk11' , 'walk12' , 'walk13' , 'walk14' , 'walk16']
walk.fps = 15

dying = Actor('dying15' , (600,685))

gosht = Actor('gosht' , (-90,700))

gosht2 = Actor('gosht' , (-90,3000))

shamshir = Actor('shamshir' , (2000,700))

tabar = Actor('tabar' , (2000,700))

 
# bol ha
harkat = False
jump1 = False
music = False
dying1 = False

button_pos = (0,0)

# update
def update() :

    #global ha 
    global dying1
    global jump1
    global music
    global harkat

# object
    if harkat == True :
        shamshir.x -= 13
    tabar.x -= 10

    if tabar.x == -100 :
        harkat = True

    if tabar.colliderect(gosht) :
        tabar.x =2000

    elif tabar.colliderect(gosht2) :
        tabar.x =2000
# mordan 
    if tabar.colliderect(idle) :
        dying1 = True

        if dying1 == True :
            idle.image = dying.image
            tabar.x = 2000
            idle.y = 700
            tabar.y = 3000

        if idle.flip_x == True:         
            idle.flip_x = True
# music
    if music :
        sounds.dying_light.play()
    else:
        sounds.dying_light.stop()
# harkat
    if keyboard.d and idle.x <= 1350 and dying1 == False:
        idle.x += 8 
        walk.animate()
        idle.flip_x = False
        idle.image = walk.image


    elif  keyboard.a and idle.x >= 80 and dying1 == False:
        idle.flip_x = True
        idle.x -= 8 
        walk.animate()
        idle.image = walk.image
# jump
    elif keyboard.w and idle.y == 700 and dying1 == False :
        jump1 = True

    if jump1 and idle.y >= 300 and dying1 == False :
        if idle.flip_x == True:         
            idle.flip_x = True

        else : 
            idle.flip_x = False
        idle.y -= 8
        jump.animate()
        idle.image = jump.image

        if idle.y == 300 :
            jump1 = False

    elif jump1 == False and idle.y != 700 :

        if idle.flip_x == True:
            idle.flip_x = True

        else:
            idle.flip_x = False
        idle.y += 5    
        down.animate()
        idle.image = down.image

        if idle.y <= 300 :
            idle.y += 5        
         
        
# draw 
def draw() : 
    Background.draw()

    idle.draw()

    button.draw()

    shamshir.draw()

    tabar.draw() 

# on mouse down
def on_mouse_down(pos) :

    global  button_pos, music

    button_pos = pos

    if  button.collidepoint(pos) and music == False :
        music = True
        button.image = 'sound_on'

    elif button.collidepoint(pos) and music == True:
         music = False
         button.image = 'sound_off'


pgzrun.go()