import pygame
from network import Network
from player import Player

pygame.init()

win = pygame.display.set_mode((1920, 1080) , pygame.FULLSCREEN)
pygame.display.set_caption("Client")

attackBar = [pygame.image.load("pictures/transparent.png"),
             pygame.image.load("pictures/20.png"),
             pygame.image.load("pictures/40.png"),
             pygame.image.load("pictures/60.png"),
             pygame.image.load("pictures/80.png"),
             pygame.image.load("pictures/100.png")]

battleground = pygame.image.load("pictures/Bind.png")
ags = pygame.image.load("pictures/agent_select.png")

def redrawWindow(win, player, player2, health1, health2, attackBar, isattack1, isattack2):
    win.blit(battleground, (0, 0))
    character1X, character1Y, attack1X, attack1Y = player.draw(win)
    character2X, character2Y, attack2X, attack2Y = player2.draw(win)
    if character2X + 150 >= attack1X + 100 >= character2X and character1Y + 200 >= attack1Y >= character1Y and health1 > 0:
        if isattack1 == False:
            health1 -= 1
            isattack1 = True
    elif character1X + 150 >= attack2X + 100 >= character1X and character1Y + 200 >= attack2Y >= character1Y and health2 > 0:
        if isattack2 == False:
            health2 -= 1
            isattack2 = True
    else:
        isattack2 = False
        isattack1 = False
    if health1 == 0 or health2 == 0:
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("You Lose", True, (0, 255, 0), (255, 0, 0))
        win.blit(text, (100, 100))
    win.blit(attackBar[health2], (character1X, character1Y - 100))
    win.blit(attackBar[health1], (character2X, character2Y - 100))
    pygame.display.update()
    pygame.display.flip()
    return health1, health2, isattack1, isattack2



def main():
    run = True
    n = Network()
    p = Player(100, 800, 1)
    p2 = Player(1700, 800, 0)
    clock = pygame.time.Clock()
    health1 = 5
    health2 = 5
    isattack1 = False
    isattack2 = False
    agent_selected = False

    while run:
        clock.tick(60)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        p.move()
        health1, health2, isattack1, isattack2 = redrawWindow(win, p, p2, health1, health2, attackBar, isattack1, isattack2)
        print(health1, health2)


main()
