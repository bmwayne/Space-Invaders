import pygame
import random

pygame.init()  # Initializing pygame

screen = pygame.display.set_mode((800, 600))  # Setting up game window size

# Title and Logo of the Game
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('background.png')

# Player
playerimg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 470
player_change = 0

# Enemy
enemyimg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40

# Bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 470
bulletY_change = -10
bullet_state = 'standby'


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


def bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (x + 16, y + 10))


gaming = True
while gaming:
    screen.fill((1, 1, 20))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False

        # Player Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -5
            elif event.key == pygame.K_RIGHT:
                player_change = 5

            # Bullet Firing
            elif event.key == pygame.K_SPACE:
                if bullet_state == 'standby':
                    bulletX = playerX
                    bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0

    playerX += player_change
    enemyX += enemyX_change

    # Player and Enemy boundaries
    if playerX < 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    if enemyX > 736:
        enemyX_change = -4
        enemyY += enemyY_change
    elif enemyX < 0:
        enemyX_change = 4
        enemyY += enemyY_change

    # Bullet Movement
    if bullet_state == 'fire':
        bullet(bulletX, bulletY)
        bulletY += bulletY_change

    # Bullet Reset
    if bulletY < 0:
        bulletY = 470
        bullet_state = 'standby'

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
