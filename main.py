import asyncio
import sys
import pygame

from engine.settings import WIDTH, HEIGHT, FPS, SPRITE_WIDTH, SPRITE_HEIGHT
from engine.assets import SpriteManager
from engine.transitions import display_gif
from data.game_config import WINDOW_CAPTION
from scenes import scene_0, scene_1, scene_2

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(WINDOW_CAPTION)
clock = pygame.time.Clock()

sprites = SpriteManager()
sprites.load("sam", "assets/sprites/sam_sprite.png", (SPRITE_WIDTH, SPRITE_HEIGHT))
sprites.load("molly", "assets/sprites/molly_sprite.png", (SPRITE_WIDTH, SPRITE_HEIGHT))

game_state = {
    "scene": 0,
    "sprites": {
        "sam": sprites.get("sam"),
        "molly": sprites.get("molly"),
    },
    "sam_pos": pygame.Vector2(100, HEIGHT // 2 - SPRITE_HEIGHT // 2),
    "molly_pos": pygame.Vector2(WIDTH - 200, HEIGHT // 2 - SPRITE_HEIGHT // 2),
    "scene_1_dialogue_done": False,
    "scene_1_actionable": False,
    "scene_1_finished": False,
    "display_gif": display_gif,
}


async def main():
    running = True

    while running:
        event = None

        for current_event in pygame.event.get():
            event = current_event
            if current_event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if game_state["scene"] == 0:
            await scene_0.run(screen, game_state, keys, event)
        elif game_state["scene"] == 1:
            await scene_1.run(screen, game_state, keys, event)
        elif game_state["scene"] == 2:
            await scene_2.run(screen, game_state, keys, event)

        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(main())
