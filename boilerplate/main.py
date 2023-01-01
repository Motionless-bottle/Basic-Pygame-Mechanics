import pygame, sys

#initialize it
pygame.init()

# configs
frames_per_second = 60
display_height = 700
display_width = 1000

display = pygame.display.set_mode((display_width, display_height))

# variables
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)