import os
import pygame

from engine.settings import BASE_PATH, BLACK, SPRITE_WIDTH, SPRITE_HEIGHT
from engine.dialogue import text_box
from engine.movement import move_player
from data.dialogue import SCENE_1_DIALOGUE


async def run(screen, game_state, keys, event):
    screen.fill(BLACK)

    sam = game_state["sprites"]["sam"]
    molly = game_state["sprites"]["molly"]

    sam_pos = game_state["sam_pos"]
    molly_pos = game_state["molly_pos"]

    screen.blit(sam, (sam_pos.x, sam_pos.y))
    screen.blit(molly, (molly_pos.x, molly_pos.y))

    if not game_state.get("scene_1_dialogue_done", False):
        await text_box(screen, *SCENE_1_DIALOGUE)
        game_state["scene_1_dialogue_done"] = True
        game_state["scene_1_actionable"] = True
        return

    if game_state.get("scene_1_actionable", False):
        move_player(keys, sam_pos)

    screen.blit(sam, (sam_pos.x, sam_pos.y))
    screen.blit(molly, (molly_pos.x, molly_pos.y))

    sam_rect = pygame.Rect(sam_pos.x, sam_pos.y, SPRITE_WIDTH, SPRITE_HEIGHT)
    molly_rect = pygame.Rect(molly_pos.x, molly_pos.y, SPRITE_WIDTH, SPRITE_HEIGHT)

    if sam_rect.colliderect(molly_rect) and not game_state.get("scene_1_finished", False):
        game_state["scene_1_finished"] = True
        gif_path = os.path.join(BASE_PATH, "assets/GIFs/LHA.gif")
        await game_state["display_gif"](screen, gif_path, duration=2500)
        game_state["scene"] = 2
