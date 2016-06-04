#import

import pygame
import sys
import time
import math
import random
import shelve
from random import randrange


#Constants
white = (255,255,255)
lightgreen = (168,192,50)
green = (97,178,56)
darkgreen = (52,151,78)
blue= (70,126,145)
lblue = (153,217,234)
yellow = (242,250,87)

score_=0
distance = 0
lef_angle=0
right_angle=0
a=0
b=0
dir_cat =0
dir_gaz =0
dir_c = 0
dir_g = 0
dir_g0 = 0
start = True
pressed_up = False
pressed_left = False
pressed_right = False
intro = True

pos_cat = [0,0]
pos_gaz= [101,92]

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Hunt-Me")
icon = pygame.image.load("icon.gif")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
myFont = pygame.font.SysFont("Agency FB", 48)
hereFont = pygame.font.SysFont("Agency FB", 40)
scoreFont = pygame.font.SysFont("Agency FB",48)
menuFont = pygame.font.SysFont("Agency FB",62)
winFont = pygame.font.SysFont("Agency FB",100)
where = hereFont.render("here !",1,lightgreen)
N = myFont.render("North ",1,white)
NE = myFont.render("NorthEast ",1,white)
NW = myFont.render("NorthWest ",1,white)
S = myFont.render("South ",1,white)
SE = myFont.render("SouthEast",1,white)
SW = myFont.render("SouthWest",1,white)
E = myFont.render("East",1,white)
W = myFont.render("West",1,white)
play = menuFont.render("HunT",4,lightgreen)
more = menuFont.render("? help",4,blue)
sound = pygame.mixer.Sound("cricket.ogg")
run_sound = pygame.mixer.Sound("run.ogg")
back = pygame.image.load("back.png")
game_logo = pygame.image.load("deer.png")
logo = pygame.image.load("logo.png")





    



    

        

################ methods ###############


### Main Menu
def game_intro():
    global intro, score_
    
   
    
    score = scoreFont.render(str(score_),1,white)
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            screen.fill(white)
            screen.blit(play,(720,650))
            screen.blit(more,(410,650))
            screen.blit(game_logo,(400,0))
            pygame.draw.rect(screen, lblue, (560,510,80,80), 0)
            screen.blit(score,(590,520))
            screen.blit(logo,(10,730))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            ### Donate button
            if 710 + 85 > mouse[0] > 710 and 645 + 70  > mouse[1] > 645 :
                if click[0] == 1:
                    intro = False
                    random_dist()
            if 400+85 > mouse[0] > 400 and 645 + 70 > mouse[1] > 645 :
                if click[0] == 1:
                    helper()
             
            pygame.display.update()
            



#Compass
def compass():
    if dir_c == 0 or dir_c == 360:
        screen.blit(N,(560,10))
    elif dir_c == 45 :
        screen.blit(NE,(560,10))
    elif dir_c == 90 :
        screen.blit(E,(560,10))
    elif dir_c == 135 :
        screen.blit(SE,(560,10))
    elif dir_c == 180 :
        screen.blit(S,(560,10))

    elif dir_c == 225 :
        screen.blit(SW,(560,10))
    elif dir_c == 270 :
        screen.blit(W,(560,10))
    elif dir_c == 315 :
        screen.blit(NW,(560,10))

#random distance
def random_dist():
    global pos_gaz
    pos_gaz[0] = random.randint(120,200)
    pos_gaz[1] = random.randint(120,200)
#distance
def dist():
    global distance
    global dir_cat
    global dir_gaz
    dir_cat = math.ceil(math.cos(pos_cat[1]))
    dir_gaz = math.ceil(math.cos(pos_gaz[1]))
   
    distance = math.ceil(math.sqrt((pow((pos_gaz[0]-pos_cat[0]),2)) + (pow((pos_gaz[1] - pos_cat[1]),2))))


#update position_cat
def run_cat():
    global dir_c , pressed_up

    if pressed_up:
        pos_cat[0] += 3 * math.cos(dir_c)
        pos_cat[1] += 3 * math.sin(dir_c)
        
        
    if pressed_left:
        if dir_c > 44:
            dir_c -= 45
        else:
            dir_c = 360    

    if pressed_right:
        if dir_c < 316:
            dir_c += 45
        else:
            dir_c = 0
        

   
#HELP
def help_me():
    global dir_g0,dir_g
    dir_g = pos_gaz[1]
    while dir_g > 360:
        dir_g = dir_g - 360
    if dir_c < dir_g:
        screen.blit(where,(980,250))
    else:
        screen.blit(where,(220,250))



#Key Events
def update_pos_cat():
    
    global pressed_up
    global pressed_left
    global pressed_right
    global pressed_down
    keys=pygame.key.get_pressed()
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:    
            pressed_up = True
        if event.key == pygame.K_LEFT:
            pressed_left = True
        if event.key == pygame.K_RIGHT:
            pressed_right = True
        if event.key == pygame.K_DOWN:
            pressed_down = True

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:    
            pressed_up = False
        if event.key == pygame.K_LEFT:
            pressed_left = False
        if event.key == pygame.K_RIGHT:
            pressed_right = False
        if event.key == pygame.K_DOWN:
            pressed_down = False 
 

 
#update position_gaz first time
def update_pos_gaz_r1():
    global left_angle
    global right_angle
    if pos_cat[0] < pos_gaz[0] and pos_cat[1] < pos_gaz[1]:
        left_angle = 0
        right_angle = 90
    if pos_cat[0] < pos_gaz[0] and pos_cat[1] > pos_gaz[1]:
        left_angle = 90
        right_angle = 180
    if pos_cat[0] > pos_gaz[0] and pos_cat[1] < pos_gaz[1]:
        left_angle = 270
        right_angle = 360
    if pos_cat[0] > pos_gaz[0] and pos_cat[1] > pos_gaz[1]:
        left_angle = 180
        right_angle = 270
    

#update positoin of gaz second time
def update_pos_gaz_r2():
    global left_angle
    global right_angle
    
    if pos_cat[0] < pos_gaz[0] and pos_cat[1] < pos_gaz[1]:
        left_angle = -90
        right_angle = 180
    if pos_cat[0] < pos_gaz[0] and pos_cat[1] > pos_gaz[1]:
        left_angle = -180
        right_angle = 90
    if pos_cat[0] > pos_gaz[0] and pos_cat[1] < pos_gaz[1]:
        left_angle = 0
        right_angle = 270
    if pos_cat[0] > pos_gaz[0] and pos_cat[1] > pos_gaz[1]:
        left_angle = -270
        right_angle = 0
       
#set random angle        
def random_angle():
    global a
    global b
    
    angle = random.randint(left_angle,right_angle)
    print(angle)
    a = math.sin(angle)
    b = math.cos(angle)


#gaz run
def run_gaz():
    
    pos_gaz[0] += 2*a
    pos_gaz[1] += 2*b
    time.sleep(0.100)




   
    
    ####### Game Loop #########
    

while True :
    game_intro()                
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
    
    screen.blit(back,(0,0))
    dist()
    update_pos_cat()
    run_cat()
    if distance <10:
        win1 = winFont.render("Great !! ",1,yellow)
        win2 = winFont.render("You won't sleep hungry tonight",1,yellow)
        screen.blit(win1,(380,180))
        score_ += 1
        intro = True
             
    if distance < 101 and distance >98:
        update_pos_gaz_r1()
        random_angle()
        distance += 3
    if distance < 101:
        if distance < 43 and distance > 40:
            update_pos_gaz_r2()
            random_angle()
            distance +=2
            
        elif distance < 40:
            run_gaz()
            white = lightgreen
        else:
            white =(255,255,255)
            if pressed_up :
                 run_gaz()
                    
                
    mts = scoreFont.render("mts",1,white)
    distDisplay = scoreFont.render(str(distance), 1, white)
    compassDisplay = myFont.render(str(dir_c), 1, white)
    compass()   
    screen.blit(distDisplay,(580,730))
    screen.blit(mts,(655,730))
    help_me()
    if pressed_up:
        run_sound.play()            

            
    pygame.key.get_repeat()   

    pygame.display.flip()







    


        

