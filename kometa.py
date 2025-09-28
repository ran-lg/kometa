import pygame
from entities import Entity


HEIGHT = 720
WIDTH = 1280


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

my_entity = Entity(150, 400, (0, 0), 270, (-10, 0), (10, 0), (0, 20))

pygame.font.init() 
my_font = pygame.font.SysFont('Arial', 30)

angle_temp = (0, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        my_entity.rotate_left()
    if keys[pygame.K_RIGHT]:
        my_entity.rotate_right()
    if keys[pygame.K_UP]:
        my_entity.accelerate()
    if keys[pygame.K_DOWN]:
        my_entity.decelerate()
    if keys[pygame.K_ESCAPE]:
        break

    my_entity.update(HEIGHT, WIDTH)

    pygame.draw.polygon(screen, 'white', my_entity.polygon_to_draw())
    
    text_surface = my_font.render('Some Text', False, 'white')
    
    if my_entity.angle != angle_temp:
        angle_temp = my_entity.angle
        print(f'{angle_temp=}')
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
