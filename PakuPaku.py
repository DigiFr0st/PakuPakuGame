import pygame

# pygame setup pieces
pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PakuDex")
clock = pygame.time.Clock()
gameRunning = True
dt = 0

playerPos = pygame.Vector2(display.get_width() / 2, display.get_height() / 2)

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    # fill the game screen to remove anything from the last frame
    display.fill("purple")

    # render game here
    pygame.draw.circle(display, "red", playerPos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerPos.y -= 300 * dt
    if keys[pygame.K_s]:
        playerPos.y += 300 * dt
    if keys[pygame.K_a]:
        playerPos.x -= 300 * dt
    if keys[pygame.K_d]:
        playerPos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
exit()
