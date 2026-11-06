import pygame
pygame.init()

HIGHT=600
WIDTH=800
WIDTH_PADDEL=15
HIGHT_PADDEL=120

X_PADDEL_1=80
Y_PADDEL_1=240

X_PADDEL_2=720
Y_PADDEL_2=240

CENTER_PALL_X=400
CENTER_PALL_Y=300


PALL=15

MOVE=10


screen=pygame.display.set_mode((WIDTH,HIGHT))
clock=pygame.time.Clock()
BLACK=(0,0,0)
white=(255,255,255)


running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys=pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            Y_PADDEL_1 -= MOVE
        elif keys[pygame.K_DOWN]:
            Y_PADDEL_1 += MOVE
        elif keys[pygame.K_KP8]:
            Y_PADDEL_2 -= MOVE
        elif keys[pygame.K_KP2]:
            Y_PADDEL_2 += MOVE


    Y_PADDEL_1= max(0, min(Y_PADDEL_1, HIGHT - HIGHT_PADDEL))
    Y_PADDEL_2=max(0, min(Y_PADDEL_2, HIGHT - HIGHT_PADDEL))

    screen.fill(BLACK)
    #Rander game here 
    pygame.draw.rect(screen,white,(X_PADDEL_1,Y_PADDEL_1,WIDTH_PADDEL,HIGHT_PADDEL))
    pygame.draw.rect(screen,white,(X_PADDEL_2,Y_PADDEL_2,WIDTH_PADDEL,HIGHT_PADDEL))
    pygame.draw.circle(screen,white,(CENTER_PALL_X,CENTER_PALL_Y),PALL)

    # here clear a SCREN
    pygame.display.flip()
    # Here a Clear a screen 60 times in 1sec
    clock.tick(60)

pygame.quit()

