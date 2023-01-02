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

player = pygame.Rect(100, 550, 50, 80)
tiles = [pygame.Rect(0, 650, 1000, 50)]




def collision_test(rect, tiles):
    collisions = []
    for tile in tiles:
        if rect.colliderect(tile):
            collisions.append(tile)

    return collisions


def move(rect,movement,tiles):

    move.collision_types = {'top': False,
                    'bottom': False,
                    'left': False,
                    'right': False}

    rect.x += movement[0]
    collisions = collision_test(rect, tiles)
    for tile in collisions:
        if movement[0] > 0:
            rect.right = tile.left
            move.collision_types['right'] = True
        if movement[0] < 0:
            rect.left = tile.right
            move.collision_types['left'] = True

    rect.y += movement[1]
    collisions = collision_test(rect, tiles)
    for tile in collisions:
        if movement[1] > 0:
            rect.bottom = tile.top
            move.collision_types['bottom'] = True
        if movement[1] < 0:
            rect.top = tile.bottom
            move.collision_types['top'] = True

    # so that the player stays inside the window
    if rect.left < 0:
        rect.left = 0
    if rect.right > display_width:
        rect.right = display_width
    if rect.top <= 0:
        rect.top = 0
    if rect.bottom >= display_height:
        rect.bottom = display_height

    return rect

left = False
right = False

player_y_momentum = 0
air_timer = 0

while running:
    display.fill((0, 0, 0))

    movement = [0,0]
    if right == True:
        movement[0] += 5
    if left == True:
        movement[0] -=5
    
    movement[1] += player_y_momentum
    player_y_momentum += 5
    if player_y_momentum > 5:
        player_y_momentum = 5

    player = move(player, movement, tiles)
    
    if move.collision_types['bottom'] == True:
        player_y_momentum = 0
        air_timer = 0
    else:
        air_timer += 1

    pygame.draw.rect(display, (16, 173, 204), player)

    for tile in tiles:
        pygame.draw.rect(display, (242, 57, 44), tile)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right = True

            if event.key == pygame.K_LEFT:
                left = True

            if event.key == pygame.K_SPACE:
                if air_timer < 6:
                    player_y_momentum = -30

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right = False

            if event.key == pygame.K_LEFT:
                left = False

    pygame.display.update()
    clock.tick(60)
