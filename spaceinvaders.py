import pygame

pygame.init() #Initializing pygame

screen = pygame.display.set_mode((800,600))  #Setting up game window size

pygame.display.set_caption('Space Invaders')    #Title of the game window

icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)   #Logo of the game window

playerimg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 470

def player():
    screen.blit(playerimg, (playerX,playerY))

game = True
while game:
    screen.fill((1, 1, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player()
    pygame.display.update()