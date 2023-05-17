import pygame
pygame.init()
player_left =   [pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/2.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/1.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/3.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/1.png"),0,0.1)]

player_up =     [pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/5.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/4.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/6.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/4.png"),0,0.1)]

player_down =   [pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/8.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/7.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/9.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/7.png"),0,0.1)]

pygame.quit()