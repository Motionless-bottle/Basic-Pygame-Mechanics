import pygame,sys

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

player = pygame.Rect(100,100, 50, 80) #player
tiles = [pygame.Rect(200, 350, 50, 50),pygame.Rect(260, 320, 50, 50)]
bullets = []

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

def shoot(x,y):
    x = x + 1
    bullets.append(pygame.Rect(x, y, 25, 25))

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

    for bullet in bullets:
        pygame.draw.rect(display, (100, 100, 100), bullet)


    for x in range(len(bullets)):
        bullets[x][0] += 10

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
            
            if event.key == pygame.K_SPACE:
                shoot(player.x, player.y)
                
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
