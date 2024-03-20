# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:04:07 2024

@author: owen.merrill
"""
def main():
    import pygame
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Move a box")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 255))
    
    box = pygame.Surface((25, 25))
    box = box.convert()
    box.fill((225, 0, 0))
    box_x = 0
    box_y = 200
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        box_x += 5
        if box_x > screen.get_width():
            box_x = 0
        screen.blit(background, (0, 0))
        screen.blit(box, (box_x, box_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
    
main()