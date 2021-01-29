import pygame

pygame.init() #initializing pygame

pygame.display.set_mode((800,600))  #setting up game window size

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False