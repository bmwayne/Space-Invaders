import pygame

pygame.init() #Initializing pygame

screen = pygame.display.set_mode((800,600))  #Setting up game window size

pygame.display.set_caption('Space Invaders')    #Title of the game window

icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)   #Logo of the game window

playerimg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 470
player_speed = 0

def player(x,y):
    screen.blit(playerimg, (x,y))

game = True
while game:
    screen.fill((1, 1, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        #Player Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed = -0.3
            if event.key == pygame.K_RIGHT:
                player_speed = 0.3
        if event.type == pygame.KEYUP:
            player_speed = 0
    playerX += player_speed
    player(playerX,playerY)
    pygame.display.update()