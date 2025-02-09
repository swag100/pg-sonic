import os
import json
import pygame

from components.object import Object

class Player(Object):
    def __init__(self, character_name = 'sonic'):
        self.character_name = character_name

        self.position = [30, 30]
        self.speed = [0, 0]

        data = self.load_character_data()

        self.radii = data['radii']
        self.jump_force = data['jump_force']

        super().__init__(self.position, self.speed, self.radii['default'])

        self.set_hitbox()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.radius != self.radii['ball']:
                    self.radius = self.radii['ball']
                else:
                    self.radius = self.radii['default']
                self.set_hitbox()

            if event.key == pygame.K_DOWN:
                self.hitbox.h -= 12
                self.hitbox.y += 12

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.set_hitbox()

    def draw(self, surface):
        pass
    
    def set_hitbox(self, width_radius = 8):
        self.hitbox = pygame.FRect(
            self.position[0] - width_radius,
            self.position[1] - self.radius[1] + 3,
            (width_radius * 2) + 1,
            ((self.radius[1] - 3) * 2) + 1,
        )

    def load_character_data(self):
        path = [
            'assets', 'data', self.character_name + '.json'
        ]

        with open(os.path.join(*path)) as data_file:
            return json.load(data_file)