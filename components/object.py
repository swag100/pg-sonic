import pygame

class Object:
    def __init__(self, position, speed, radius, ground_speed = 0, ground_angle = 0):
        self.radius = radius
        self.ground_speed = ground_speed
        self.ground_angle = ground_angle

        self.position = position
        self.speed = speed

        self.rect = self.get_rect()

    def handle_event(self, event):
        pass

    def tick(self, dt):
        pass

    def draw(self, surface):
        pass

    def get_rect(self):
        return pygame.FRect(
            self.position[0] - self.radius[0], 
            self.position[1] - self.radius[1], 
            (self.radius[0] * 2) + 1, 
            (self.radius[1] * 2) + 1
        )