import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
FPS = 30

# player
playerImg = pygame.image.load("player.png")
x = 20
y = 300
x_vel = 0
x_vel1 = 0

# player
enemyImg = pygame.image.load("player.png")
enemyx = 745
enemyy = 300
e_vel = 0
e_vel1 = 0

# ball
ballImg = pygame.image.load("ball.png")
ballx = 400
bally = random.randint(0, 545)
ball_vel = 6
ball_vel1 = 6

# score
score_p = 0
font =pygame.font.Font("freesansbold.ttf",16)
textx = 390
texty = 300

def show_score():
    score = font.render(":"+str(score_p),True,(255,255,255))
    screen.blit(score,(textx,texty))

def is_collision():
    distance = math.sqrt(math.pow(ballx-enemyx ,2)+math.pow(bally-enemyy,2))
    if distance <= 48:
        return True
    else:
        return False

def is_collision1():
    distance = math.sqrt(math.pow(ballx-x ,2)+math.pow(bally-y,2))
    if distance <= 48:
        return True
    else:
        return False

def player():
    screen.blit(playerImg, (x, y))


def enemy():
    screen.blit(enemyImg, (enemyx, enemyy))


def ball():
    screen.blit(ballImg, (ballx, bally))


run = True
while run:
    screen.fill((0, 0, 0))
    pygame.draw.aaline(screen, (255, 255, 255), (400, 0), (400, 600))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                x_vel = 8
            if event.key == pygame.K_s:
                x_vel1 = 8
            if event.key == pygame.K_UP:
                e_vel = 8
            if event.key == pygame.K_DOWN:
                e_vel1 = 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s :
                x_vel = 0
                x_vel1 = 0
            if event.key == pygame.K_UP or pygame.K_DOWN:
                e_vel = 0
                e_vel1 = 0
    y -= x_vel
    if y <= 5:
        y = 5
    y += x_vel1
    if y >= 530:
        y = 530

    enemyy -= e_vel
    if enemyy <= 5:
        enemyy = 5
    enemyy += e_vel1
    if enemyy >= 530:
        enemyy = 530

    ballx += ball_vel
    bally += ball_vel1
    if ballx >= 745 or ballx <= 20:
        score_p += 1
        ballx = 400
        bally = random.randint(0,565)
    if bally <= 0 or bally >= 565:
        ball_vel1 *= -1


    collision = is_collision()
    if collision:
        ball_vel *= -1

    collision1 = is_collision1()
    if collision1:
        ball_vel *= -1

    clock.tick(FPS)
    enemy()
    player()
    ball()
    is_collision()
    pygame.display.update()
