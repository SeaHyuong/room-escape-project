# Example file showing a circle moving on screen
import pygame
from setting import *
#from setting import *

# pygame setup
pygame.init()

clock = pygame.time.Clock()
fps = 30                       #1초당 업데이트 30회
running = True

#배경
screen = pygame.display.set_mode((1200, 800))
backgrand = pygame.image.load("모눈배경.jpg")

#플레이어 좌표초기화(중앙)
y_pos=(screen.get_height()-204)/2
x_pos=(screen.get_width()-204)/2

#플레이어 이동값
p_y=0 
p_x=0
direction = ""           #플레이어 방향
walkcount=0              #플레이어 이동 프레임
#screen.blit(player,((screen.get_width()-player_width/5)/2, (screen.get_height()-player_height/5)/2))

screen.blit(player_left[0],(0,0))

def animation(direction):         #플레이어 이동 애니메이션
    global walkcount
    screen.blit(backgrand,(0,0))

    if walkcount>=16:      
        walkcount=0
    
    if direction=="": 
        screen.blit(player_left[1],(x_pos,y_pos))
    elif direction == "left":
        screen.blit(player_left[int(walkcount/4)],(x_pos,y_pos))
        walkcount+=1
    elif direction == "right":
        screen.blit(pygame.transform.flip(player_left[int(walkcount/4)],True,False),(x_pos,y_pos))
        walkcount+=1
    elif direction == "up":
        screen.blit(pygame.transform.flip(player_up[int(walkcount/4)],True,False),(x_pos,y_pos))
        walkcount+=1
    elif direction == "down":
        screen.blit(pygame.transform.flip(player_down[int(walkcount/4)],True,False),(x_pos,y_pos))
        walkcount+=1
    


while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #벙향키 플레이어 이동

        if event.type == pygame.KEYUP:       
            # keyup한 값과 방향이 같을경우에만 정지_(모든 키를 누르지않았을 때 정지 & 연속클릭시 애니메이션 오류 방지)
            if (event.key == pygame.K_w and direction=="up") or (event.key == pygame.K_s and direction=="down"):
                direction=""
                p_y=0
                p_x=0 
            elif (event.key == pygame.K_a and direction=="left") or (event.key == pygame.K_d and direction=="right"):  
                direction=""
                p_y=0
                p_x=0                 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p_y = -10
                p_x=0   #사선움직임 차단
                direction = "up"   
            elif event.key == pygame.K_s:
                p_y = 10
                p_x=0   
                direction = "down"
            elif event.key == pygame.K_a:
                p_x = -10
                p_y=0   #사선움직임 차단
                direction = "left"
            elif event.key == pygame.K_d:
                p_x = 10
                p_y=0   
                direction = "right"
       
    x_pos += p_x
    y_pos += p_y
            
    
    animation(direction)

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
