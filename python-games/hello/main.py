import asyncio

import pygame


WIDTH = 640
HEIGHT = 360


async def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hello")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 64)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((24, 30, 42))
        text = font.render("Hello from pygbag", True, (240, 240, 240))
        screen.blit(text, (20, 20))
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)


asyncio.run(main())

