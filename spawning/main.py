import pygame, sys, random

# initialize it
pygame.init()

# configurations
frames_per_second = 60
window_height = 700
window_width = 1000

display = pygame.display.set_mode((window_width, window_height))
display_rect = display.get_rect()
display.fill((54, 134, 173))

# variables
clock = pygame.time.Clock() #frame regulator
running = True

player = pygame.Rect(100,100, 50, 50) #player
#tiles = [pygame.Rect(200, 350, 50, 50),pygame.Rect(260, 320, 50, 50)]
tiles = []

def collision_test(rect, tiles):
    collisions = []
    for tile in tiles:
        if rect.colliderect(tile):
            collisions.append(tile)
    return collisions

def move(rect,movement,tiles):
    rect.x += movement[0]
    collisions = collision_test(rect, tiles)
    for tile in collisions:
        if movement[0] > 0:
            rect.right = tile.left
        if movement[0] < 0:
            rect.left = tile.right

    rect.y += movement[1]
    collisions = collision_test(rect, tiles)
    for tile in collisions:
        if movement[1] > 0:
            rect.bottom = tile.top
        if movement[1] < 0:
            rect.top = tile.bottom

    # so that the player stays inside the window
    if rect.left < 0:
        rect.left = 0
    if rect.right > window_width:
        rect.right = window_width
    if rect.top <= 0:
        rect.top = 0
    if rect.bottom >= window_height:
        rect.bottom = window_height



    return rect

def spawn():
    #pygame.Rect(x,y,50,50)
    new_rect = pygame.Rect(random.randint(0,window_width//50 - 1) * 50,random.randint(0, window_height//50 - 1) * 50,50,50)

    collisions = collision_test(new_rect, tiles)
    if len(collisions) == 0:
        tiles.append(new_rect)
    else:
        spawn()

def despawn():
    if len(tiles) > 0:
        tiles.pop(-1)

up    = False
down  = False
left  = False
right = False

# game loop
while running:
    display.fill((0, 0, 0))
    
    movement = [0,0]
    if right == True:
        movement[0] += 5
    if left == True:
        movement[0] -=5
    if up == True:
        movement[1] -=5
    if down == True:
        movement[1] += 5
    
    player = move(player, movement, tiles)

    pygame.draw.rect(display, (16, 173, 204), player)

    for tile in tiles:
        pygame.draw.rect(display, (242, 57, 44), tile)

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right = True

            if event.key == pygame.K_LEFT:
                left = True

            if event.key == pygame.K_DOWN:
                down = True

            if event.key == pygame.K_UP:
                up = True

            if len(tiles) == 240:
                print("too many tiles, press x to remove blocks ")
            else:
                if event.key == pygame.K_z:
                    spawn()

            if event.key == pygame.K_x:
                despawn()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right = False

            if event.key == pygame.K_LEFT:
                left = False

            if event.key == pygame.K_DOWN:
                down = False

            if event.key == pygame.K_UP:
                up = False
    
    pygame.display.update()
    clock.tick(60)
