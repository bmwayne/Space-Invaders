import pygame

pygame.init() #Initializing pygame

screen = pygame.display.set_mode((800,600))  #Setting up game window size
pygame.display.set_caption('Space Invaders')    #Title of the game window
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)   #Logo of the game window

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    screen.fill((0, 58, 108))
    pygame.display.update()