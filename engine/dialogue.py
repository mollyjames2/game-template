import asyncio
import pygame
import sys
import textwrap

from engine.settings import WIDTH, HEIGHT, WHITE, BLACK, FONT_SMALL


async def text_box(screen, *lines, font=FONT_SMALL):
    line_height = 40
    max_line_width = WIDTH - 140
    box_x, box_y = 50, HEIGHT - 150
    box_width, box_height = WIDTH - 100, 100

    dialog_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)

    processed_boxes = []
    for line in lines:
        wrapped = textwrap.wrap(line, width=max_line_width // font.size("A")[0])
        for i in range(0, len(wrapped), 2):
            processed_boxes.append(wrapped[i:i + 2])

    current_box_index = 0
    box_active = True

    while box_active:
        dialog_surface.fill((0, 0, 0, 0))
        pygame.draw.rect(dialog_surface, WHITE, (0, 0, box_width, box_height))
        pygame.draw.rect(dialog_surface, BLACK, (10, 10, box_width - 20, box_height - 20))

        if current_box_index < len(processed_boxes):
            current_box = processed_boxes[current_box_index]
            for i, line in enumerate(current_box):
                text_surface = font.render(line, True, WHITE)
                dialog_surface.blit(text_surface, (20, 20 + i * line_height))

        down_arrow = font.render("\u25BC", True, WHITE)
        dialog_surface.blit(down_arrow, (box_width - 40, box_height - 35))

        screen.blit(dialog_surface, (box_x, box_y))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if current_box_index + 1 < len(processed_boxes):
                        current_box_index += 1
                    else:
                        box_active = False
                elif event.key == pygame.K_UP and current_box_index > 0:
                    current_box_index -= 1

        await asyncio.sleep(0)
