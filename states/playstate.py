import pygame
from states.basestate import BaseState

from components.player import Player

class PlayState(BaseState):
    def start(self, persistent_data): 
        super().__init__()

        self.persistent_data = persistent_data

        self.objects = [
            Player()
        ]

    def handle_event(self, event):
        for object in self.objects:
            object.handle_event(event)

    def tick(self, dt):
        for object in self.objects: object.tick(dt)

    def draw(self, surface):
        surface.fill((255,255,255))

        for object in self.objects:
            object.draw(surface)

            if isinstance(object, Player):
                rect = object.get_rect()

                radius_surface = pygame.surface.Surface((rect.w, rect.h))
                radius_surface.fill((255,0,0))
                radius_surface.set_alpha(128)
                
                hitbox_surface = pygame.surface.Surface((object.hitbox.w, object.hitbox.h))
                hitbox_surface.fill((0,0,255))
                hitbox_surface.set_alpha(128)
                
                surface.blit(radius_surface, rect.topleft)
                surface.blit(hitbox_surface, object.hitbox.topleft)

                pygame.draw.rect(surface, (255,255,255), pygame.Rect(*object.position, 1, 1))