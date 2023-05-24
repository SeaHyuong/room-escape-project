import pygame
import random
from setting import *


class Game():
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fps = 30                    #1초당 업데이트 30회
        #배경
        self.screen = pygame.display.set_mode((700, 700))
        self.running = True

        #플레이어
        self.p_xpos=(self.screen.get_width()-204)/2
        self.p_ypos=(self.screen.get_height()-204)/2         #플레이어 x위치값
        self.p_x=0
        self.p_y=0                                           #플레이어 이동값
        self.p_direc = 0                #플레이어 방향
        self.damage=0                   #플레이어 데미지
        self.p_walkcount=0              #플레이어 이동 애니메이션 프레임

        # 크리쳐
        self.c_xpos=350      #괴물x위치값
        self.c_ypos=500
        self.c_y=0 
        self.c_x=0
        self.c_direc = 0
        self.c_walkcount=0 
        self.c_prame=31

        self.run() #메인 루프 실행direction



    def animation(self, key, direc, xpos, ypos): #플레이어 이동 애니메이션
        
        if self.p_walkcount>=32:      
            self.p_walkcount=0
        if key=='player':
            self.screen.blit(image.player_pixel[direc][int(self.p_walkcount/8)],(xpos,ypos))
        elif key=='creature':
            self.screen.blit(image.creature_pixel[direc][int(self.p_walkcount/8)],(xpos,ypos))
        self.p_walkcount+=1


    def creature_run(self):
   
            if self.c_prame > 30:       # 30 fps동안 한 방향으로 이동
                self.c_direc=random.randint(1,4)
                self.c_prame=0
            else:
                if self.c_direc==1 and self.p_xpos <= self.c_xpos:          #left
                    self.c_x = -5
                    self.c_y=0                  
                elif self.c_direc==2 and self.p_xpos >= self.c_xpos:        #right      
                    self.c_x = 5        
                    self.c_y=0   
                elif self.c_direc==3 and self.p_ypos <= self.c_ypos:        #up
                    self.c_y=-5
                    self.c_x=0              
                elif self.c_direc==4 and self.p_ypos >= self.c_ypos:        #down
                    self.c_y = 5
                    self.c_x=0   
                else:           #랜덤으로 나온 방향쪽에 플레이어가 없을때 c_direc=0 >> stop 애니메이션
                    self.c_y=0
                    self.c_x=0
                    self.c_direc = 0 
                self.c_prame+=1

            # game.screen 밖으로 못나가게 제어
            if self.c_xpos<0 and self.c_x<0: 
                self.c_x+=11        #좌측 끝
                self.c_prame=31
            if self.c_xpos>550 and self.c_x>0: 
                self.c_x-=11        #우측 끝
                self.c_prame=31
            if self.c_ypos<0 and self.c_y<0: 
                self.c_y+=11        #상단 끝
                self.c_prame=31
            if self.c_ypos>550 and self.c_y>0: 
                self.c_y-=11        #하단 끝
                self.c_prame=31

            self.c_xpos += self.c_x
            self.c_ypos += self.c_y
    

            self.animation('creature',self.c_direc, self.c_xpos,self.c_ypos)

    # 메인 반복문
    def run(self):
        while self.running:
            self.clock.tick(self.fps)
            self.screen.fill("gray")
            self.creature_run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running=False
               

                #벙향키 플레이어 이동
                if event.type == pygame.KEYUP:       
                    # KEYUP한 값과 방향이 같을경우에만 정지_(모든 키를 누르지않았을 때 정지 & 연속클릭시 애니메이션 오류 방지)
                    if (event.key == pygame.K_w and self.p_direc==3) or (event.key == pygame.K_s and self.p_direc==4):
                        self.p_direc=0
                        self.p_y=0
                        self.p_x=0 
                    elif (event.key == pygame.K_a and self.p_direc==1) or (event.key == pygame.K_d and self.p_direc==2):  
                        self.p_direc=0
                        self.p_y=0
                        self.p_x=0                 

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.p_x = -5
                        self.p_y=0              #사선움직임 차단
                        self.p_direc = 1        # left
                    elif event.key == pygame.K_d:
                        self.p_x = 5
                        self.p_y=0   
                        self.p_direc = 2        #right
                    elif event.key == pygame.K_w:
                        self.p_y = -5
                        self.p_x=0 
                        self.p_direc = 3        # up
                    elif event.key == pygame.K_s:
                        self.p_y = 5
                        self.p_x=0   
                        self.p_direc = 4        # down
                    
            

            # self.screen 밖으로 못나가게 제어
            if self.p_xpos<-50 and self.p_x<0: self.p_x+=11 #좌측 끝
            if self.p_xpos>550 and self.p_x>0: self.p_x-=11 #우측 끝
            if self.p_ypos<-20 and self.p_y<0: self.p_y+=11 #상단 끝
            if self.p_ypos>550 and self.p_y>0: self.p_y-=11 #하단 끝

            self.p_xpos += self.p_x
            self.p_ypos += self.p_y


            
            #데미지 에니메이션 
            if (self.p_xpos-self.c_xpos)<10 and (self.p_xpos-self.c_xpos)>-85 and abs(self.p_ypos-self.c_ypos)<100 and self.damage==0:
                self.damage=1
            if self.damage>0 and self.damage<6:
                if self.damage%2!=0 : self.screen.blit(image.damage_pixel,(self.p_xpos,(self.p_ypos-self.damage*3)))
                self.damage+=1
            else: 
                self.animation('player',self.p_direc, self.p_xpos,self.p_ypos)
                self.damage=0
            
            # print(self.p_xpos-self.c_xpos, self.p_ypos-self.c_ypos)
            # print(self.c_xpos, self.c_ypos)
            

            

            pygame.display.flip()


game=Game() #class 게임 실행

pygame.quit()