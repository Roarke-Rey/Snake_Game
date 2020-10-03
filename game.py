import pygame
import random
import time
import numpy as np
from models import Snake, Food

pygame.init()
WIDTH = 1000
HEIGHT = 600
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw(snake_list, food):
	screen.fill(BLACK)
	for snake in snake_list:
		pygame.draw.rect(screen, WHITE, (snake.x, snake.y, snake.size, snake.size))

	pygame.draw.rect(screen, WHITE, (food.x, food.y, food.size, food.size))
	pygame.display.update()

def game_over(score):
	message_display('Game over, score: ' + str(score))

def text_objects(text, font):
	TextSurface = font.render(text, True, WHITE)
	return TextSurface, TextSurface.get_rect()

def message_display(text):
	DiplayingTextFont = pygame.font.Font('freesansbold.ttf',50)
	TextSurface, TextRect = text_objects(text, DiplayingTextFont)
	TextRect.center = ((WIDTH/2),(HEIGHT/2))
	screen.blit(TextSurface, TextRect)
	pygame.display.update()
	time.sleep(3)

def is_colliding(snake, food):
	return np.linalg.norm(np.array([snake.x, snake.y]) - np.array([food.x, food.y])) < (snake.size/2 + food.size/2)

def make_new_snake(snake_list, snake_length, food):
	old_snake = snake_list[0]
	if food.x > old_snake.x:
		if food.y > old_snake.y:
			new_snake = Snake(WIDTH, HEIGHT, old_snake.x+old_snake.size, old_snake.y)
		elif food.y == old_snake.y:
			new_snake = Snake(WIDTH, HEIGHT, old_snake.x+old_snake.size, old_snake.y)
		else:
			new_snake = Snake(WIDTH, HEIGHT, old_snake.x+old_snake.size, old_snake.y)

	elif food.x == old_snake.x:
		if food.y > old_snake.y:
			new_snake = Snake(WIDTH, HEIGHT, old_snake.x, old_snake.y+old_snake.size)
		else:
			new_snake = Snake(WIDTH, HEIGHT, old_snake.x, old_snake.y-old_snake.y)

	elif food.x < old_snake.x:
		if food.y > old_snake.y:
			new_snake = Snake(WIDTH, HEIGHT, old_snake.x-old_snake.size, old_snake.y)
		elif food.y == old_snake.y:
			new_snake = Snake(WIDTH, HEIGHT, old_snake.x-old_snake.size, old_snake.y)
		else:
			new_snake = Snake(WIDTH, HEIGHT, old_snake.x-old_snake.size, old_snake.y)

	snake_length += 1
	snake_list.insert(0, new_snake)
	return snake_list, snake_length

def handle_collisions(snake_list, food, speed, snake_length, score):
	over = False
	head = snake_list[0]
	if is_colliding(head, food):
		score += 1
		speed += 1
		snake_list, snake_length = make_new_snake(snake_list, snake_length, food)
		head = snake_list[0]
		food = Food(WIDTH, HEIGHT)
	if head.boundary_colliding():
		game_over(score)
		game()
	return snake_list, food, speed, snake_length, score

def start_game():
	message_display('Ready to go....')
	screen.fill(BLACK)
	message_display('Navigate the snake using arrow keys')
	screen.fill(BLACK)
	message_display('Collecting food will increase your score')
	screen.fill(BLACK)

def move_snake(snake_list, x_movement, y_movement):
	head = snake_list[0]

	if len(snake_list) == 1:
		head.move(x_movement, y_movement)
	else:
		snake_list.pop()
		old_snake = head
		snake_list.insert(1, old_snake)
		head.move(x_movement, y_movement)
	return snake_list

def game():
	speed = 5	
	x_movement = speed
	y_movement = 0
	snake_length = 1
	score = 0

	screen.fill(BLACK)
	snake_list = []
	initial_x = random.randint(10,WIDTH-10)
	initial_y = random.randint(10,HEIGHT-10)
	snake = Snake(WIDTH, HEIGHT, initial_x, initial_y)
	snake_list.append(snake)

	food = Food(WIDTH, HEIGHT)
	flag = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					flag = 1
					x_movement = -speed
					y_movement = 0
				if event.key == pygame.K_UP:
					flag = 2
					y_movement = -speed
					x_movement = 0
				if event.key == pygame.K_RIGHT:
					flag = 3
					x_movement = speed
					y_movement = 0
				if event.key == pygame.K_DOWN:
					flag = 4
					y_movement = speed
					x_movement = 0

		snake_list, food, speed, snake_length, score = handle_collisions(snake_list, food, speed, snake_length, score)
		if flag == 1:
			x_movement = -speed
			y_movement = 0
		elif flag == 2:
			y_movement = -speed
			x_movement = 0
		elif flag == 3:
			x_movement = speed
			y_movement = 0
		elif flag == 4:
			y_movement = speed
			x_movement = 0

		draw(snake_list,food)

		snake_list = move_snake(snake_list, x_movement, y_movement)
		
		# for i in snake_list:
		# 	i.move(x_movement,y_movement)
		pygame.time.delay(30)

def main():
	screen.fill(BLACK)
	#start_game()
	game()

		
if __name__ == '__main__':
	main()