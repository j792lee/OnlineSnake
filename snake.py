import pygame
import time
import random
from HSio import insertScore, printHS

class Snake:
    direction = 'x'
    poslist = [[0,0]]
    points = 0
    bored = [[0 for i in range(40)] for i in range(20)]
    bored[poslist[0][0]][poslist[0][1]] = 1
    apple = [0,0]

    def __init__(self):
        self.newApple()
        self.poslist[0][0] = random.randint(0,19)
        self.poslist[0][1] = random.randint(0, 39)

    def draw(self, screen, font):
        if self.direction == 'Left':
            self.poslist.insert(0, [self.poslist[0][0], self.poslist[0][1]-1])
        elif self.direction == 'Right':
            self.poslist.insert(0, [self.poslist[0][0], self.poslist[0][1]+1])
        elif self.direction == 'Up':
            self.poslist.insert(0, [self.poslist[0][0]-1, self.poslist[0][1]])
        elif self.direction == 'Down':
            self.poslist.insert(0, [self.poslist[0][0]+1, self.poslist[0][1]])
        else:
            self.poslist.insert(0, [self.poslist[0][0], self.poslist[0][1]])

        if self.poslist[0][1] < 0 or self.poslist[0][0] < 0 or self.poslist[0][0]  > 19 or self.poslist[0][1] > 39:
            return self.gameEnd(screen, font)

        if self.bored[self.poslist[0][0]][self.poslist[0][1]] == 2:
            self.newApple()
            self.points += 100
        elif self.bored[self.poslist[0][0]][self.poslist[0][1]] == 1 and len(self.poslist) > 2:
            return self.gameEnd(screen, font)
        else:
            del (self.poslist[-1])

        self.bored = [[0 for i in range(40)] for i in range(20)]

        for i in self.poslist:
            self.bored[i[0]][i[1]] = 1
        self.bored[self.apple[0]][self.apple[1]] = 2
        drawbored(screen, self.bored)
        return -1

    def newApple(self):
        while True:
            self.apple[0] = random.randint(0,19)
            self.apple[1] = random.randint(0, 39)
            if self.bored[self.apple[0]][self.apple[1]] != 1:
                break

    def gameEnd(self, screen, font):
        screen.blit(font.render("Score: {0}".format(self.points), 200, (255, 255, 255)), (150, 150))
        pygame.display.update()
        return self.points


def drawbored(screen, bored):
    for i, list in enumerate(bored):
        for ii, value in enumerate(list):
            if value == 0:
                pygame.draw.rect(screen, (0,0,0), (ii*30, i*30, 30, 30))
            elif value == 1:
                pygame.draw.rect(screen, (0, 255, 0), (ii * 30, i * 30, 28, 28))
            elif value == 2:
                pygame.draw.rect(screen, (255, 0, 0), (ii * 30, i * 30, 28, 28))

def displayHS(screen, font):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                quit()
        printHS(screen, font)
        pygame.display.update()

def game(player1, screen):


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player1.direction != "Down":
                    player1.direction = "Up"
                elif event.key == pygame.K_LEFT and player1.direction != "Right":
                    player1.direction = "Left"
                elif event.key == pygame.K_DOWN and player1.direction != "Up":
                    player1.direction = "Down"
                elif event.key == pygame.K_RIGHT and player1.direction != "Left":
                    player1.direction = "Right"
        score = player1.draw(screen, font)
        screen.blit(font.render("{0}".format(player1.points), 30, (255, 255, 255)), (0, 550))
        if score != -1:
            return score
        pygame.display.update()
        time.sleep(0.05)

def nameMaker(screen, font):
    nameAsciiValue = [65,65,65]#sets defaulf ascii to 'A'
    nameAsciiIndex = 0
    #screen.blit(font.render("Name:", 200, (255, 255, 255)), (450, 0))
    while True:
        pygame.display.update()
        rectangl = (200+nameAsciiIndex*300, 150, 400, 400)
        pygame.draw.rect(screen, (0,0,0), rectangl)
        screen.blit(font.render("{0}".format(chr(nameAsciiValue[nameAsciiIndex])), 200, (255, 255, 255)), (200+nameAsciiIndex*300, 150))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    nameAsciiValue[nameAsciiIndex]+= 1
                    if nameAsciiValue[nameAsciiIndex] > 90: nameAsciiValue[nameAsciiIndex] = 65
                elif event.key == pygame.K_DOWN:
                    nameAsciiValue[nameAsciiIndex] -= 1
                    if nameAsciiValue[nameAsciiIndex] < 65: nameAsciiValue[nameAsciiIndex] = 90
                elif event.key == pygame.K_RETURN and nameAsciiIndex<2:
                    nameAsciiIndex +=1
                elif event.key == pygame.K_RETURN and nameAsciiIndex == 2:
                    playerName = ''.join(chr(x) for x in nameAsciiValue)
                    return playerName
            elif event.type == pygame.QUIT:
                quit()

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("sans",40)
player1 = Snake()
screen = pygame.display.set_mode((30 * len(player1.bored[0]), (30 * len(player1.bored))))

score = game(player1, screen)

player1.bored = [[0 for i in range(40)] for i in range(20)]
drawbored(screen, player1.bored)

name = nameMaker(screen, pygame.font.SysFont("sans",400))
insertScore(score, name)

player1.bored = [[0 for i in range(40)] for i in range(20)]
drawbored(screen, player1.bored)

displayHS(screen, font)

