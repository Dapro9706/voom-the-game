import pygame

win = pygame.display.set_mode((500,480))
clock = pygame.time.Clock()
exit_flag = False

pygame.init ()

while not exit_flag:
    clock.tick (27)

    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            exit_flag = True


pygame.quit ()
