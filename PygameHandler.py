#Just a class to hold parameters used 

import pygame
from Grid import generate_grid, draw_grid
from Graph import initialise_grid_graph
from math import floor

class Handler():

    def __init__(self, rows, columns, screen_res, background_colour, \
                grid_colour, x_min, y_min, interval):

        self.screen = pygame.display.set_mode(screen_res)
        self.clock = pygame.time.Clock()
        self.all_tiles, self.grid = generate_grid(rows, columns, x_min, \
                                                y_min, interval)
        self.graph = initialise_grid_graph(rows, columns)
        self.background_colour = background_colour
        self.grid_colour = grid_colour
        self.rows = rows
        self.columns = columns
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = screen_res[0] - x_min
        self.y_max = screen_res[1] - y_min
        self.interval = interval
        self.grid_rectangle = pygame.Rect(x_min, y_min, columns * interval, \
            rows * interval)
        self.start = False

    def window_update(self):
        #To save on rewriting all the pygame window drawing.

        self.screen.fill(self.background_colour)
        draw_grid(self.screen, self.grid_colour, self.rows, self.columns, \
            self.x_min, self.y_min, self.interval)
        self.all_tiles.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)

    def generate_new_graph(self, rows, columns):
        self.graph = initialise_grid_graph(rows, columns)

        y_interval_max = (self.y_max - self.y_min) // rows
        x_interval_max = (self.x_max - self.x_min) // columns
        self.interval = min(x_interval_max, y_interval_max)

        self.all_tiles, self.grid = generate_grid(rows, columns, self.x_min, \
                                        self.y_min, self.interval)
        self.rows = rows
        self.columns = columns
        self.grid_rectangle = pygame.Rect(self.x_min, self.y_min, columns *\
            self.interval, rows * self.interval)