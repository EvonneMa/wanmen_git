import pygame
from pygame.locals import *
from sys import exit
import random
#资源地址
BACKGROUND_PATH = 'D:/file/selflearning/ml/Week3_FlappyBird/assets/sprites/png.png'
PLAYER_PATH = ['D:/file/selflearning/ml/Week3_FlappyBird/assets/sprites/redbird-downflap.png',\
'D:/file/selflearning/ml/Week3_FlappyBird/assets/sprites/redbird-midflap.png',\
'D:/file/selflearning/ml/Week3_FlappyBird/assets/sprites/redbird-upflap.png']
PIPE_PATH = 'D:/file/selflearning/ml/Week3_FlappyBird/assets/sprites/pipe-green.png'
BASE_PATH = 'D:/file/selflearning/ml/Week3_FlappyBird/assets/sprites/base.png'
NUMBER_PATH = [
'D:/file/selflearning/ml/Week3_FlappyBird/assets/sprites/0.png',\
'D:/file/selflearning/ml/Week3_FlappyBird/assets/sprites/1.png',\
'D:/file/selflearning/ml/Week3_FlappyBird/assets/sprites/2.png',\
'D:/file/selflearning/ml/Week3_FlappyBird/assets/sprites/3.png',\
'D:/file/selflearning/ml/Week3_FlappyBird/assets/sprites/4.png',\
'D:/file/selflearning/ml/Week3_FlappyBird/assets/sprites/5.png',\
'D:/file/selflearning/ml/Week3_FlappyBird/assets/sprites/6.png',\
'D:/file/selflearning/ml/Week3_FlappyBird/assets/sprites/7.png',\
'D:/file/selflearning/ml/Week3_FlappyBird/assets/sprites/8.png',\
'D:/file/selflearning/ml/Week3_FlappyBird/assets/sprites/9.png'
]
#屏幕尺寸
SCREEN_HEIGHT = 512
SCREEN_WIDTH = 288
IMAGE = {}
#初始化、定义屏幕
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Sakura')
#读取图片
IMAGE['BG'] = pygame.image.load(BACKGROUND_PATH).convert()
IMAGE['BASE'] = pygame.image.load(BASE_PATH).convert_alpha()
IMAGE['PLAYER'] = [pygame.image.load(PLAYER_PATH[0]).convert_alpha(),
				   pygame.image.load(PLAYER_PATH[1]).convert_alpha(),
				   pygame.image.load(PLAYER_PATH[2]).convert_alpha()]
IMAGE['PIPE'] = [pygame.transform.rotate(pygame.image.load(PIPE_PATH).convert_alpha(),180),
				 pygame.image.load(PIPE_PATH).convert_alpha()]
IMAGE['NUMBER'] = [
pygame.image.load(NUMBER_PATH[0]).convert_alpha(),
pygame.image.load(NUMBER_PATH[1]).convert_alpha(),
pygame.image.load(NUMBER_PATH[2]).convert_alpha(),
pygame.image.load(NUMBER_PATH[3]).convert_alpha(),
pygame.image.load(NUMBER_PATH[4]).convert_alpha(),
pygame.image.load(NUMBER_PATH[5]).convert_alpha(),
pygame.image.load(NUMBER_PATH[6]).convert_alpha(),
pygame.image.load(NUMBER_PATH[7]).convert_alpha(),
pygame.image.load(NUMBER_PATH[8]).convert_alpha(),
pygame.image.load(NUMBER_PATH[9]).convert_alpha()
]
#常用参数
PIPE_HEIGHT = IMAGE['PIPE'][0].get_height()
PIPE_WIDTH = IMAGE['PIPE'][0].get_width()
BASE_HEIGHT = IMAGE['BASE'].get_height()

x = 1 #/2*SCREEN_WIDTH
y = 1/2*SCREEN_HEIGHT
move_x = 0
move_y = 0

BIRD_HEIGHT = IMAGE['PLAYER'][0].get_height()
BIRD_WIDTH = IMAGE['PLAYER'][1].get_width()
#控制帧速率，每秒更新多少次
FPS = 30
FPSCLOCK = pygame.time.Clock()
#翅膀状态
flap = 0
new_pipe = True
gap = 100
#飞行速度
vy = 0
yg = y
deltay = 0
ay_g = 0.5
ay_max = 8
ay_min = -6
ay_temp = -1.5
flapped = False
count_flag = True
number = 0
while(True):
	
	for event in pygame.event.get():
		if event.type == QUIT:
			quit()
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				move_x = -5
			elif event.key == K_RIGHT:
				move_x = 5
			elif event.key == K_UP:
				move_y = -5
			else:
				move_y = 5
		else:
			move_x = 0
			move_y = 0
	x += move_x
	y += move_y
	if x < 0:
		x = SCREEN_WIDTH
	if y < 0:
		y = SCREEN_HEIGHT
	if x > SCREEN_WIDTH:
		x = 0
	if y > SCREEN_HEIGHT:
		y = 0
	
	SCREEN.blit(IMAGE['BG'],[0,0])
	
	if new_pipe == True:
		h = random.randint(0,PIPE_HEIGHT-30)
		p_x = SCREEN_WIDTH
		SCREEN.blit(IMAGE['PIPE'][0],[p_x,h-PIPE_HEIGHT])
		SCREEN.blit(IMAGE['PIPE'][1],[p_x,h + gap])
		new_pipe = False
	elif p_x > -1*PIPE_WIDTH:
		p_x -= 5
		SCREEN.blit(IMAGE['PIPE'][0],[p_x,h-PIPE_HEIGHT])
		SCREEN.blit(IMAGE['PIPE'][1],[p_x,h + gap])
	else:
		new_pipe = True
	SCREEN.blit(IMAGE['BASE'],[0,SCREEN_HEIGHT-BASE_HEIGHT])

	if y > h+gap/2:
		flapped = True
	if flapped == True:
		if y < h + gap and deltay < 0:
			vy += 0.5*(ay_temp + ay_g)
		else:
			vy += (ay_temp+ay_g)
		flapped = False
	else:
		if y > h and deltay > 0:
			vy += 0.5*ay_g
		else:
			vy += ay_g	
	if vy > ay_max:
		vy = ay_max
	if vy < ay_min:
		vy = ay_min
	y += vy
	deltay = y - yg
	yg = y
	#print(y)
	if y < 0:
		y = 0
	if y > SCREEN_HEIGHT-BASE_HEIGHT:
		y = SCREEN_HEIGHT-BASE_HEIGHT
	if number < 10:
		SCREEN.blit(IMAGE['NUMBER'][number],[0.5*SCREEN_WIDTH,0.1*SCREEN_HEIGHT])
	elif number < 100:
		SCREEN.blit(IMAGE['NUMBER'][int(number/10)],[0.45*SCREEN_WIDTH,0.1*SCREEN_HEIGHT])
		SCREEN.blit(IMAGE['NUMBER'][number%10],[0.55*SCREEN_WIDTH,0.1*SCREEN_HEIGHT])
	else:
		SCREEN.blit(IMAGE['NUMBER'][int(number/100)],[0.45*SCREEN_WIDTH,0.1*SCREEN_HEIGHT])
		SCREEN.blit(IMAGE['NUMBER'][int((number%100)/10)],[0.5*SCREEN_WIDTH,0.1*SCREEN_HEIGHT])
		SCREEN.blit(IMAGE['NUMBER'][(number%100)%10],[0.6*SCREEN_WIDTH,0.1*SCREEN_HEIGHT])
	SCREEN.blit(IMAGE['PLAYER'][flap],[x,y])
	flap = (flap+1)%3

	if x >= p_x and count_flag:
		number+=1
		count_flag = False
	elif x < p_x and not count_flag:
		count_flag = True
	pygame.display.update()
	FPSCLOCK.tick(FPS)