import pygame

class Tile(pygame.sprite.Sprite):
    
    def __init__(self, x, y, colour = (0,0,0), grid_dimension = 9):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((grid_dimension,grid_dimension))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.__colour = colour

    def set_colour(self, colour):
        self.__colour = colour
        self.image.fill(colour)

    def get_colour(self):
        return self.__colour

def id_to_pos(x, y, x_min, y_min, interval):
    #Returns the midpoint of the Tile from its ID.
    return ((x+0.5) * interval + x_min, (y+0.5) * interval + y_min)

def generate_grid(rows, columns, x_min, y_min, interval = 10):

    all_tiles = pygame.sprite.Group()
    grid_map = {}
    grid_dimension = interval - 1

    for x in range(columns):
        for y in range(rows):
            pos = id_to_pos(x, y, x_min, y_min, interval)
            new_tile = Tile(pos[0], pos[1], grid_dimension=grid_dimension)
            all_tiles.add(new_tile)
            grid_map[(x,y)] = new_tile

    return all_tiles, grid_map


#This is an ancient piece of code from my A Level coursework
#Leaving the dreadful long lines for that genuine vintage feel.
def draw_grid(screen, grid_colour, horizontal = 50, vertical = 100, x_min = 140, y_min = 110, gap = 10):
    #Draws a horizontal x vertical (50 x 100 by default) grid.
    #Grid serves as outline of tiles. So strips are thin.
    #First draw horizontal rectangles, width 2 and length gap*vertical.
    #Then draw vertical rectangles, width 2 and length gap*horizontal.
    #Grid is of size (gap*horizontal)x(gap*vertical) px.

    pygame.draw.rect(screen, grid_colour, pygame.Rect(x_min, y_min, gap*vertical, 1))
    for h in range(horizontal - 1):
        pygame.draw.rect(screen, grid_colour, pygame.Rect(x_min, (y_min + gap*(h+1)), gap*vertical, 2))
    pygame.draw.rect(screen, grid_colour, pygame.Rect(x_min, (y_min + gap*horizontal), gap*vertical, 1))

    pygame.draw.rect(screen, grid_colour, pygame.Rect(x_min, y_min, 1, gap*horizontal))
    for v in range(vertical - 1):
        pygame.draw.rect(screen, grid_colour, pygame.Rect((x_min + gap*(v+1)), y_min, 2, gap*horizontal))
    pygame.draw.rect(screen, grid_colour, pygame.Rect((x_min+gap*vertical), y_min, 1, gap*horizontal))