import sys
import pygame
import constants

from states.playstate import PlayState

class Game:
    def __init__(self, states, init_state):
        self.done = False

        #State variables
        self.states = states
        self.state_name = init_state
        self.state = states[init_state]

        pygame.init()

        self.clock = pygame.time.Clock()

        #Surfaces
        self.screen = pygame.display.set_mode(tuple(axis * constants.WINDOW_ZOOM for axis in constants.WINDOW_SIZE), pygame.DOUBLEBUF)
        self.surface = pygame.Surface(constants.WINDOW_SIZE)

        #Finally, start state!
        self.state.start({})

    def set_state(self):
        #Set new state, pass persistent data
        
        next_state = self.state.next_state
        persistent_data = self.state.persistent_data

        if next_state in self.states.keys():
            self.state = self.states[next_state]
            self.state_name = list(self.states.keys())[list(self.states.values()).index(self.state)]
        else:
            print(f'Failed to find {next_state}. Reloading state')
        
        self.state.start(persistent_data)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.state.handle_event(event)
            
            #pass event to state
    
    def tick(self, dt):
        if self.state.done: self.set_state()
        self.state.tick(dt)

    def draw(self, screen):
        self.state.draw(self.surface)
        screen.blit(pygame.transform.scale_by(self.surface, constants.WINDOW_ZOOM), (0, 0))

    def begin(self):
        while not self.done:
            dt = self.clock.tick(constants.FRAME_RATE) / 1000

            self.handle_events()
            self.tick(dt)
            self.draw(self.screen)

            pygame.display.flip()

states = {
    'PlayState': PlayState(),
}

Game(states, 'PlayState').begin()