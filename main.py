import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# start menu
menu = pygame.image.load("Untitled.png")

run = True
while run:
    screen.blit(menu, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            import start
            run = False
    pygame.display.update()
