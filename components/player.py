import os
import json
import pygame

from components.object import Object
from components.animation import Animation

class Player(Object):
    def __init__(self, character_name = 'sonic'):
        self.character_name = character_name

        self.position = [30, 30]
        self.speed = [0, 0]

        self.character_data = self.load_character_data()

        self.radii = self.character_data['radii']
        self.jump_force = self.character_data['jump_force']

        self.sprite_size = self.character_data['sprite_size']
        
        #create animations list
        self.animations = self.load_character_animations()
        
        self.animation_name = 'default'
        self.animation_frame = 0

        super().__init__(self.position, self.speed, self.radii['default'])

        self.set_hitbox()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.radius != self.radii['ball']:
                    self.animation_name = 'ball'
                    self.radius = self.radii['ball']
                else:
                    self.animation_name = 'default'
                    self.radius = self.radii['default']
                
                self.set_hitbox()

            if event.key == pygame.K_DOWN and self.animation_name == 'default':
                self.hitbox.h -= 12
                self.hitbox.y += 12
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.set_hitbox()

    def tick(self, dt):
        pass

    def draw(self, surface):
        surface.blit(self.animations[self.animation_name][self.animation_frame], (-4, -4))
    
    def set_hitbox(self, width_radius = 8):
        self.hitbox = pygame.FRect(
            self.position[0] - width_radius,
            self.position[1] - self.radius[1] + 3,
            (width_radius * 2) + 1,
            ((self.radius[1] - 3) * 2) + 1,
        )

    def load_character_data(self):
        path = [
            'assets', 'data', 'characters', self.character_name + '.json'
        ]

        with open(os.path.join(*path)) as data_file:
            return json.load(data_file)
        
    def load_character_animations(self):
        animations = {}

        #Load whole spritesheet into memory yo!
        spritesheet_path = [
            'assets', 'images', 'characters', self.character_name + '.png'
        ]
        spritesheet = pygame.image.load(os.path.join(*spritesheet_path)).convert_alpha()

        #populate animations dict; {animname: [animframe surfaces]}
        for anim_name, anim_data in self.character_data['animations'].items():
            animation_frames = []

            for frame_data in anim_data:
                frame_position = [-axis for axis in frame_data]

                surface = pygame.surface.Surface((self.character_data['sprite_size'],) * 2, pygame.SRCALPHA)
                surface.blit(spritesheet, frame_position)

                animation_frames.append(surface)
            
            animations[anim_name] = animation_frames
        
        #finally, return animations!
        return animations