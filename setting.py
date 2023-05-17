import pygame
pygame.init()
player_left =   [pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/Gunhi2.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/Gunhi1.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/Gunhi3.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/Gunhi1.png"),0,0.1)]

player_up =     [pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/Gunhi5.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/Gunhi4.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/Gunhi6.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/Gunhi4.png"),0,0.1)]

player_down =   [pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/Gunhi8.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/Gunhi7.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/Gunhi9.png"),0,0.1),
                 pygame.transform.rotozoom(pygame.image.load("./image/Gunhi/Gunhi7.png"),0,0.1)]

pygame.quit()