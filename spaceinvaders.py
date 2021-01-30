import pygame
import random
import math

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
num_of_enemy = 6
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(num_of_enemy):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 470
bulletY_change = -10
bullet_state = 'standby'

score = 0


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


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

    # Enemy Movement
    for i in range(num_of_enemy):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 470
            bullet_state = 'standby'
            score += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    playerX += player_change

    # Player and Enemy boundaries
    if playerX < 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Bullet Movement
    if bullet_state == 'fire':
        bullet(bulletX, bulletY)
        bulletY += bulletY_change

    # Bullet Reset
    if bulletY < 0:
        bulletY = 470
        bullet_state = 'standby'

    player(playerX, playerY)
    pygame.display.update()
