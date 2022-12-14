import random
import time
from time import sleep
import pygame
import sys
from pygame import *

pygame.init()
display_weight = 1080
display_height = 720
kW = 0.7
kH = 0.40
KATE_WEIGHT = display_weight * kW
KATE_HEIGHT = display_height * kH

KATE_X = (display_weight - KATE_WEIGHT) / 2
KATE_Y = 75

BALL_DIAMETR = 30
BALL_X_START = (display_weight - 30) / 2
BALL_Y_START = display_height / 1.15
BALL_CENTER_X_START = BALL_X_START + (BALL_DIAMETR / 2)
BALL_CENTER_Y_START = BALL_Y_START + (BALL_DIAMETR / 2)

kMiniKate = 4.2
xDisplay0 = 0
yDisplay0 = 0

xKate0 = KATE_X
yKate0 = KATE_Y + KATE_HEIGHT

xMiniKate0 = (display_weight - (KATE_WEIGHT / kMiniKate)) / 2

a1 = xMiniKate0 - xKate0  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
a2 = BALL_X_START - xMiniKate0
b1 = BALL_Y_START - yKate0

b2 = (a2 * b1) / a1

yMiniKate0 = BALL_CENTER_Y_START - b2

display = pygame.display.set_mode([display_weight, display_height])

background = pygame.image.load("vorota.jpg")
person = pygame.image.load("person.png")


class Player:

    def __init__(self, start_x, statr_y, speed, image, weight=77, height=245):
        self.image = image
        self.height = height
        self.weight = weight
        self.speed = speed
        self.x = start_x
        self.y = statr_y

    def go(self, vector):

        if vector == "UP" and (self.y - self.speed > 0):
            self.y -= self.speed

        if vector == "LEFT" and self.x > 0:
            self.x -= self.speed

        if vector == "RIGHT" and self.x + self.weight < display_weight:
            self.x += self.speed

        if vector == "DOWN":
            self.y += self.speed


ball = Surface((BALL_DIAMETR, BALL_DIAMETR))
ball.fill(Color("black"))

blue_kords = Surface((5, 5))
blue_kords.fill(Color("blue"))

bg = Surface((display_weight, display_height))
bg.fill((0, 100, 0))

kate = Surface((KATE_WEIGHT, KATE_HEIGHT))
kate.fill((0, 0, 0))


def predictor(X_start, Y_start):
    XtoMini = X_start - xMiniKate0
    YtoMini = yMiniKate0 - Y_start

    XtoKate = XtoMini * kMiniKate
    YtoKate = YtoMini * kMiniKate

    X_finite = XtoKate + xKate0
    Y_finite = yKate0 - YtoKate
    return X_finite, Y_finite


def run_game():
    game = True

    while game:

        # display.blit(background, (0, 0))
        display.blit(leha.image, (leha.x, leha.y))

        # _________________________________________
        key = pygame.key.get_pressed()
        # if key[pygame.K_w]:
        #     leha.go("UP")
        if key[pygame.K_a] and leha.x >= 260:
            leha.go("LEFT")

        if key[pygame.K_d] and leha.x <= 760:
            leha.go("RIGHT")

        # if key[pygame.K_s]:
        #     leha.go("DOWN")

        display.blit(bg, (0, 0))
        display.blit(kate, (KATE_X, KATE_Y))
        display.blit(ball, ((display_weight - 30) / 2, display_height / 1.15))

        test_ball_x_1 = random.randint(int(xMiniKate0), int(xMiniKate0 + (KATE_WEIGHT / kMiniKate)))
        test_ball_y_1 = random.randint(int(yMiniKate0 - (KATE_HEIGHT / kMiniKate)), int(yMiniKate0))
        ball.fill((255, 255, 255))

        display.blit(ball, (test_ball_x_1, test_ball_y_1))

        ball.fill((255, 0, 0))

        display.blit(ball, predictor(test_ball_x_1, test_ball_y_1))

        sleep(2)

        display.blit(blue_kords, (xMiniKate0, yMiniKate0))

        # -------------------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        pygame.time.Clock().tick(60)


leha = Player(300, 240, 10, person)
run_game()
