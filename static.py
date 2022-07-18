import pygame
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 700
MAIN_COLOR = (125,125,125)
INPUT_COLOR = (25, 25 ,25)
SPACE_WIDTH, SPACE_HEIGHT = 50, 50
image = pygame.transform.rotate(pygame.transform.scale( pygame.image.load('plane.png'), (SPACE_WIDTH, SPACE_HEIGHT)), -90)


rect = pygame.Rect(300 , 400, SPACE_WIDTH, SPACE_HEIGHT)
chat_rect = pygame.Rect(WIDTH-50, HEIGHT-50, 30, 30)
base_font = pygame.font.Font(None, 32)
upper_font = pygame.font.Font(None, 25)

active = False


