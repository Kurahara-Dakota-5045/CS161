#! /usr/bin/env python 3
"""
This is a game that counts players points.

This is a game where you click a button to "spin the wheel"
and it gives out points from 1000 to 20000. If you spin a zero
it is essentially a bankrupt so your score goes down to zero.
play this with some of your friends to see who has the best luck
after ten turns in this Wheel Game.

Dakota Kurahara
"""


import random
import sys
import time
import os
import pygame

os.getcwd()

pygame.init()


class button:
    """class for a button."""

    def __init__(self, color, x, y, width, height, text=""):
        """Create a class for my button."""
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        """Draw the button on screen."""
        if outline:
            pygame.draw.rect(
                win,
                outline,
                (self.x - 2, self.y - 2, self.width + 4, self.height + 4),
                0,
            )

        pygame.draw.rect(win, self.color,
                         (self.x, self.y, self.width, self.height), 0)

        if self.text != "":
            font = pygame.font.SysFont("comicsans", 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(
                text,
                (
                    self.x + (self.width / 2 - text.get_width() / 2),
                    self.y + (self.height / 2 - text.get_height() / 2),
                ),
            )

    def isOver(self, pos):
        """Show if the mouse is over the button."""
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


file = open("final_bgnd.png", "r")
display_width = 1280
display_height = 720
black = (0, 0, 0)
white = (255, 255, 255)
win = pygame.display.set_mode((1280, 720))
win.fill((255, 255, 255))
gameDisplay = pygame.display.set_mode((display_width, display_height))
bgndIMG = pygame.image.load(file)
gameDisplay.blit(bgndIMG, (0, 0))
pygame.display.update()
greenButton = button((0, 0, 255), 565, 450, 150, 150, "SPIN")


def points_1(text):
    """Show player 1s text on screen."""
    font = pygame.font.Font("freesansbold.ttf", 22)
    gameDisplay.fill(pygame.Color("white"), (225, 81, 85, 18))
    gameDisplay.blit(font.render(text, True, black), (225, 79))

    pygame.display.update()


def points_2(text):
    """Show player 2s text on screen."""
    font = pygame.font.Font("freesansbold.ttf", 22)
    gameDisplay.fill(pygame.Color("white"), (445, 77, 85, 18))
    gameDisplay.blit(font.render(text, True, black), (445, 77))
    pygame.display.update()


def points_3(text):
    """Show player 3s text on screen."""
    font = pygame.font.Font("freesansbold.ttf", 22)
    gameDisplay.fill(pygame.Color("white"), (735, 73, 85, 18))
    gameDisplay.blit(font.render(text, True, black), (735, 73))
    pygame.display.update()


def points_4(text):
    """Show player 4s text on screen."""
    font = pygame.font.Font("freesansbold.ttf", 22)
    gameDisplay.fill(pygame.Color("white"), (970, 77, 85, 18))
    gameDisplay.blit(font.render(text, True, black), (970, 77))
    pygame.display.update()


def wait():
    """Give the pauses between turns."""
    halt = True
    while halt:
        for e in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                halt = False

            if e.type == pygame.MOUSEMOTION:
                if greenButton.isOver(pos):
                    greenButton.color = (255, 0, 0)
                else:
                    greenButton.color = (0, 255, 0)

        pygame.display.update()


def GameOver():
    """Game Over appears on screen."""
    text = "Game Over Click Again To Restart"
    font = pygame.font.Font("freesansbold.ttf", 50)
    gameDisplay.blit(font.render(text, True, black), (250, 350))
    pygame.display.update()
    wait()


def WheelGame():
    """Run the game WheelGame."""
    gameDisplay.blit(bgndIMG, (0, 0))
    points_1("0")
    points_2("0")
    points_3("0")
    points_4("0")
    while True:
        greenButton.draw(win, (0, 0, 0))
        player_1 = 0
        player_2 = 0
        player_3 = 0
        player_4 = 0
        turn_1 = 1
        turn_2 = 1
        turn_3 = 1
        turn_4 = 1
        count = 0
        score = 0
        for e in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for count in range(0, 10):
                count += 1
                if turn_1 == count:
                    turn_1 += 1
                    if e.type == pygame.MOUSEBUTTONDOWN:

                        pygame.time.delay(100)
                        _mx_, _my_ = pygame.mouse.get_pos()
                        if 780 > _my_ > 450 and 565 < _mx_ < 715:
                            score = random.randint(0, 20)
                            if score > 0:
                                player_1 = player_1 + score * 1000
                            if score == 0:
                                player_1 = player_1 * 0
                        points_1(str(player_1))
                        wait()

                if turn_2 == count:
                    turn_2 += 1
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        pygame.time.delay(100)
                        _mx_, _my_ = pygame.mouse.get_pos()
                        if 780 > _my_ > 450 and 565 < _mx_ < 715:
                            score = random.randint(0, 20)
                            if score > 0:
                                player_2 = player_2 + score * 1000
                            if score == 0:
                                player_2 = player_2 * 0
                        points_2(str(player_2))
                        wait()
                if turn_3 == count:
                    turn_3 += 1
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        pygame.time.delay(100)
                        _mx_, _my_ = pygame.mouse.get_pos()
                        if 780 > _my_ > 450 and 565 < _mx_ < 715:
                            score = random.randint(0, 20)
                            if score > 0:
                                player_3 = player_3 + score * 1000
                            if score == 0:
                                player_3 = player_3 * 0
                        points_3(str(player_3))
                        wait()
                if turn_4 == count:
                    turn_4 += 1
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        pygame.time.delay(100)
                        _mx_, _my_ = pygame.mouse.get_pos()
                        if 780 > _my_ > 450 and 565 < _mx_ < 715:
                            score = random.randint(0, 20)
                            if score > 0:
                                player_4 = player_4 + score * 1000
                            if score == 0:
                                player_4 = player_4 * 0
                        points_4(str(player_4))
                        wait()
                        if turn_4 == 10:
                            GameOver()
                            WheelGame()


WheelGame()
