import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,100,0)
b_green = (0,150,0)
b_red = (255,0,0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Car Wars')
clock = pygame.time.Clock()

crashed = False

carImg = pygame.image.load('car1.png')
road = pygame.image.load('road.png')
thingImg = pygame.image.load('car.png')
bgmenu = pygame.image.load('images.png')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("SCORE : "+str(count), True, black)
    gameDisplay.blit(text,(1,1))

def things(x, y):
    gameDisplay.blit(thingImg, (x,y))

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    gameloop()
    
def crash():
    message_display('CRASHED')

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
           action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.blit(bgmenu, (0,0))
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("CAR WARS", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        button("START",150,300,120,50,green,b_green,gameloop)
        button("QUIT",550,300,120,50,red,b_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)

def quitgame():
    pygame.quit()
    quit()

def gameloop():
    x =  (display_width * 0.45)
    y = (display_height * 0.7)
    sy = -40
    
    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 6
    dodged = 0
    
    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -8
                elif event.key == pygame.K_RIGHT:
                    x_change = 8
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                
        x += x_change
    
        if sy < 20:
            sy += 1
        else:
            while sy > -30:
                sy -= 1
                
        gameDisplay.blit(road,(0,sy))
        
        things(thing_startx, thing_starty)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
        
        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - 149
            thing_startx = random.randrange(0,display_width)
            thing_speed += 0.6
            dodged += 1

        if y < thing_starty+144:
            if x > thing_startx-4 and x+4 < thing_startx + 85 or x+car_width+4 > thing_startx and x + 4 + car_width < thing_startx+85:
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_intro()  
gameloop()
pygame.quit()
quit()
