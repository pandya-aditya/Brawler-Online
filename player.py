from typing import List, Union
import os
import pygame

pygame.init()

class Player():

    def __init__(self, characterX, characterY, player):

        self.characterRun = ["pictures/ninja/Run__000.png",
                             "pictures/ninja/Run__001.png",
                             "pictures/ninja/Run__002.png",
                             "pictures/ninja/Run__003.png",
                             "pictures/ninja/Run__004.png",
                             "pictures/ninja/Run__005.png",
                             "pictures/ninja/Run__006.png",
                             "pictures/ninja/Run__007.png",
                             "pictures/ninja/Run__008.png",
                             "pictures/ninja/Run__009.png"]

        self.characterIdle = ["pictures/ninja/Idle__000.png",
                              "pictures/ninja/Idle__001.png",
                              "pictures/ninja/Idle__002.png",
                              "pictures/ninja/Idle__003.png",
                              "pictures/ninja/Idle__004.png",
                              "pictures/ninja/Idle__005.png",
                              "pictures/ninja/Idle__006.png",
                              "pictures/ninja/Idle__007.png",
                              "pictures/ninja/Idle__008.png",
                              "pictures/ninja/Idle__009.png"]

        self.slide = ["pictures/ninja/Slide__000.png",
                      "pictures/ninja/Slide__001.png",
                      "pictures/ninja/Slide__002.png",
                      "pictures/ninja/Slide__003.png",
                      "pictures/ninja/Slide__004.png",
                      "pictures/ninja/Slide__005.png",
                      "pictures/ninja/Slide__006.png",
                      "pictures/ninja/Slide__007.png",
                      "pictures/ninja/Slide__008.png",
                      "pictures/ninja/Slide__009.png"]

        self.characterJump = ["pictures/ninja/Jump__000.png",
                              "pictures/ninja/Jump__001.png",
                              "pictures/ninja/Jump__002.png",
                              "pictures/ninja/Jump__003.png",
                              "pictures/ninja/Jump__004.png",
                              "pictures/ninja/Jump__005.png",
                              "pictures/ninja/Jump__006.png",
                              "pictures/ninja/Jump__007.png",
                              "pictures/ninja/Jump__008.png",
                              "pictures/ninja/Jump__009.png"]

        self.characterThrow = ["pictures/ninja/Throw__000.png",
                               "pictures/ninja/Throw__001.png",
                               "pictures/ninja/Throw__002.png",
                               "pictures/ninja/Throw__003.png",
                               "pictures/ninja/Throw__004.png",
                               "pictures/ninja/Throw__005.png",
                               "pictures/ninja/Throw__006.png",
                               "pictures/ninja/Throw__007.png",
                               "pictures/ninja/Throw__008.png",
                               "pictures/ninja/Throw__009.png"]

        self.crouchAttack = "pictures/crouch attack.png"
        self.characterImage = "pictures/ninja/Idle__000.png"
        self.attackImage = "pictures/transparent.png"
        self.star = "pictures/ninja star.png"
        self.transparentImage = "pictures/transparent.png"
        self.characterCrouch = "pictures/green crouch.png"
        self.battleground = "pictures/battleground.png"

        self.characterX = characterX
        self.characterY = characterY
        self.characterYValue = characterY
        self.attackX = 0
        self.attackY = 0
        self.attackSpeed = 0

        self.jumpCount = 10
        self.jumpImageCount = len(self.characterThrow) - 1
        self.attackCount = 0
        self.runCount = 0
        self.idleCount = len(self.characterIdle) - 1
        self.slideCount = len(self.slide) - 1

        self.directionDecided = False
        self.isJump = False

        self.isAttack = False

        if player == 0:
            self.facing = "left"
        if player == 1:
            self.facing = "right"
        self.frameRate = 0
        self.elapsed = 0
        self.attackElapse = 0

    def draw(self, WIN):
        if self.facing == "right":
            WIN.blit(pygame.image.load(os.path.join(self.characterImage)), (self.characterX, self.characterY))
        if self.facing == "left":
            WIN.blit(pygame.transform.flip(pygame.image.load(os.path.join(self.characterImage)), True, False),
                     (self.characterX, self.characterY))
        WIN.blit(pygame.image.load(os.path.join(self.attackImage)), (self.attackX, self.attackY))
        return self.characterX, self.characterY, self.attackX, self.attackY

    def move(self):
        keys = pygame.key.get_pressed()
        now = pygame.time.get_ticks()

        # WASD movement pattern
        if keys[pygame.K_a]:
            if keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
                self.characterX -= 40
            elif keys[pygame.K_s] and not self.isJump:
                self.characterX -= 15
                self.characterY = self.characterYValue + 50
                if now - self.elapsed >= 50 and self.slideCount >= 0:
                    self.characterImage = self.slide[self.slideCount]
                    self.slideCount -= 1
                    self.elapsed = now
            else:
                self.characterX -= 15
                if now - self.elapsed >= 30:
                    self.characterImage = self.characterRun[self.runCount]
                    self.runCount += 1
                    self.elapsed = now
                if self.runCount == len(self.characterRun):
                    self.runCount = 0
            self.facing = "left"

        elif keys[pygame.K_d]:
            if keys[pygame.K_d] and keys[pygame.K_LSHIFT]:
                self.characterX += 40
            elif keys[pygame.K_s] and not self.isJump:
                self.characterX += 15
                self.characterY = self.characterYValue + 50
                if now - self.elapsed >= 50 and self.slideCount >= 0:
                    self.characterImage = self.slide[self.slideCount]
                    self.slideCount -= 1
                    self.elapsed = now
            else:
                self.characterX += 15
                if now - self.elapsed >= 30:
                    self.characterImage = self.characterRun[self.runCount]
                    self.runCount += 1
                    self.elapsed = now
                if self.runCount == len(self.characterRun):
                    self.runCount = 0

            self.facing = "right"

        else:
            self.runCount = len(self.characterRun) - 1
            self.slideCount = len(self.slide) - 1
            if now - self.elapsed >= 50:
                self.characterImage = self.characterIdle[self.idleCount]
                self.idleCount -= 1
                self.elapsed = now
                if self.idleCount <= -1:
                    self.idleCount = len(self.characterIdle) - 1
            if not self.isJump:
                self.characterY = 800
                
        # Attack and Jumping/ more advance movements
        if not self.isAttack:
            if keys[pygame.K_e]:
                self.isAttack = True
                self.attackX = self.characterX
                self.attackY = self.characterY
                self.attackImage = self.star
        else:
            if self.attackX <= 1920 and self.facing == "left" and not self.directionDecided:
                self.attackSpeed = - 40
                self.directionDecided = True
            elif self.attackX >= 0 and self.facing == "right" and not self.directionDecided:
                self.attackSpeed = 40
                self.directionDecided = True
            elif 0 <= self.attackX <= 1920:
                if now - self.elapsed >= 30 and self.attackCount < len(self.characterThrow) - 1:
                    self.attackCount += 1
                    self.characterImage = self.characterThrow[self.attackCount]
                    self.elapsed = now
                else:
                    self.attackX += self.attackSpeed


            else:
                self.isAttack = False
                self.attackX = self.characterX
                self.attackImage = self.transparentImage
                self.directionDecided = False
                self.attackCount = 0

        if not self.isJump:
            if keys[pygame.K_SPACE] and not keys[pygame.K_s]:
                self.isJump = True
        else:
            if self.jumpCount >= -10:

                now = pygame.time.get_ticks()
                if now - self.elapsed >= 10:
                    self.characterY -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                    if self.jumpCount >= 0:
                        self.characterImage = self.characterJump[self.jumpCount - 1]
                    self.elapsed = now
                    self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.isJump = False
                self.jumpImageCount = len(self.characterJump) - 1