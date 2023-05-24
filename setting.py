# Example file showing a circle moving on screen/
import pygame
pygame.init()


class image:
    #플레이어 이미지
    player_pixel =      [[pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/1.png"),0,0.15),         #stop
                        pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/1.png"),0,0.15),
                        pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/1.png"),0,0.15),
                        pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/1.png"),0,0.15)],
                
                        [pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/2.png"),0,0.15),           #left
                        pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/1.png"),0,0.15),
                        pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/3.png"),0,0.15),
                        pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/1.png"),0,0.15)],
                
                        [pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/2.png"),0,0.15),True,False),           #right
                        pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/1.png"),0,0.15),True,False),
                        pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/3.png"),0,0.15),True,False),
                        pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/1.png"),0,0.15),True,False)],

                        [pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/4.png"),0,0.15),           #up
                        pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/5.png"),0,0.15),
                        pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/4.png"),0,0.15),
                        pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/6.png"),0,0.15)],

                        [pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/7.png"),0,0.15),           #down
                        pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/8.png"),0,0.15),
                        pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/7.png"),0,0.15),
                        pygame.transform.rotozoom(pygame.image.load("./image/Soyeon/9.png"),0,0.15)]]
    
    #크리쳐_괴물 이미지
    creature_pixel =   [[pygame.transform.rotozoom(pygame.image.load("./image/Creature/1.png"),0,0.09),           #stop
                        pygame.transform.rotozoom(pygame.image.load("./image/Creature/3.png"),0,0.09),
                        pygame.transform.rotozoom(pygame.image.load("./image/Creature/2.png"),0,0.09),
                        pygame.transform.rotozoom(pygame.image.load("./image/Creature/1.png"),0,0.09)],
                
                        [pygame.transform.rotozoom(pygame.image.load("./image/Creature/4.png"),0,0.09),                  #left      
                        pygame.transform.rotozoom(pygame.image.load("./image/Creature/5.png"),0,0.09),
                        pygame.transform.rotozoom(pygame.image.load("./image/Creature/6.png"),0,0.09),
                        pygame.transform.rotozoom(pygame.image.load("./image/Creature/5.png"),0,0.09)],
                
                        [pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load("./image/Creature/4.png"),0,0.09),True,False),                  #right      
                        pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load("./image/Creature/5.png"),0,0.09),True,False),
                        pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load("./image/Creature/6.png"),0,0.09),True,False),
                        pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load("./image/Creature/5.png"),0,0.09),True,False)],

                        [pygame.transform.rotozoom(pygame.image.load("./image/Creature/7.png"),0,0.09),                 #up
                        pygame.transform.rotozoom(pygame.image.load("./image/Creature/8.png"),0,0.09),
                        pygame.transform.rotozoom(pygame.image.load("./image/Creature/9.png"),0,0.09),
                        pygame.transform.rotozoom(pygame.image.load("./image/Creature/8.png"),0,0.09)],

                        [pygame.transform.rotozoom(pygame.image.load("./image/Creature/10.png"),0,0.09),                #down
                        pygame.transform.rotozoom(pygame.image.load("./image/Creature/11.png"),0,0.09),
                        pygame.transform.rotozoom(pygame.image.load("./image/Creature/12.png"),0,0.09),
                        pygame.transform.rotozoom(pygame.image.load("./image/Creature/11.png"),0,0.09)]]

    # 데미지 이미지
    damage_pixel = pygame.transform.rotozoom(pygame.image.load("./image/damage.png"),0,0.15) 

pygame.quit()