import os
import pygame
from engine.settings import BASE_PATH

class SpriteManager:
    def __init__(self):
        self.sprites = {}

    def load(self, name, path, size=None):
        full_path = os.path.join(BASE_PATH, path)
        image = pygame.image.load(full_path).convert_alpha()
        if size:
            image = pygame.transform.scale(image, size)
        self.sprites[name] = image

    def load_with_aspect_ratio(self, name, path, target_height):
        full_path = os.path.join(BASE_PATH, path)
        image = pygame.image.load(full_path).convert_alpha()
        original_width, original_height = image.get_width(), image.get_height()
        aspect_ratio = original_width / original_height
        scaled_width = int(target_height * aspect_ratio)
        scaled_image = pygame.transform.scale(image, (scaled_width, target_height))
        self.sprites[name] = scaled_image

    def get(self, name):
        return self.sprites.get(name)
