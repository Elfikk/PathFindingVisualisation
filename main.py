import pygame 
from Grid import Tile, generate_grid, draw_grid
from Graph import initialise_grid_graph
from Interface import Intermediate
from a_star_algo import a_star_setup, visit_next_node, mark_neighbour
from Heap import Min_Heap

#pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,720))

done = False
running = False
clock = pygame.time.Clock()

grid_rectangle = pygame.Rect(140, 110, 1000, 500)

#Some globals
background_colour = (0,0,0)
grid_colour = (255,255,255)

rows, columns = 25, 25
x_min, y_min = 140, 110
interval = 20

start = (0, 0)
target = (columns - 1, rows - 1)

#Graph + Tiles setup.
all_tiles, grid = generate_grid(rows, columns, x_min, y_min, interval)
graph = initialise_grid_graph(rows, columns)

adapter = Intermediate(graph, grid, interval, rows, columns, x_min, y_min)
adapter.change_status(start, "start")
adapter.change_status(target, "goal")

def window_update(screen, clock, background_colour, grid_colour, columns, \
    rows, x_min, y_min, interval):
    #To save on rewriting all the pygame window drawing.

    screen.fill(background_colour)
    draw_grid(screen, grid_colour, columns, rows, x_min, y_min, \
                interval)
    all_tiles.draw(screen)

    pygame.display.flip()
    clock.tick(60)

while not done:

    for event in pygame.event.get():
        
        #Clicking the red cross quit cross
        if event.type == pygame.QUIT:
            done = True

        #Left Mouse Button Click - Add/Remove Obstacle
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            position = event.pos
            if grid_rectangle.collidepoint(position):
                id = adapter.pos_to_id(position)
                adapter.obstacle(id)

        #Middle Mouse Button Click - Set Start
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            position = event.pos
            if grid_rectangle.collidepoint(position):
                adapter.change_status(start, "unvisited")
                id = adapter.pos_to_id(position)
                start = id
                adapter.change_status(id, "start")

        #Right Mouse Button Click - Set Target
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            position = event.pos
            if grid_rectangle.collidepoint(position):
                adapter.change_status(target, "unvisited")
                id = adapter.pos_to_id(position)
                target = id
                adapter.change_status(id, "goal")

        #Spacebar - start algo
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

            open_set, closed_set, h, g = a_star_setup(graph, start, target)

            neighbours = []

            while len(open_set) != 0 and neighbours != None:

                #Prevents pygame from believing the program has crashed - as it 
                #turns out, not handling events for a few seconds makes pygame 
                #assume a crash. pump() allows it to handle internal actions, so
                #the window remains up.
                pygame.event.pump() 

                open_set, closed_set, h, g, neighbours, pos, previous_pos =\
                    visit_next_node(graph, target, open_set, closed_set, h, g,\
                                    adapter)

                if neighbours != None:

                    for neighbour_pos in neighbours:
                        mark_neighbour(graph, open_set, closed_set, h, g, \
                                       adapter, pos, neighbour_pos)
                                
                        screen.fill(background_colour)
                        draw_grid(screen, grid_colour, columns, rows, x_min,\
                                  y_min, interval)
                        all_tiles.draw(screen)

                        pygame.display.flip()
                        clock.tick(60)

                closed_set[pos] = previous_pos, g[pos]
                adapter.change_status(pos, "visited")

                window_update(screen, clock, background_colour, grid_colour, \
                              columns, rows, x_min, y_min, interval)

            path = [target]
            prev = target
            while prev != start:
                prev = closed_set[prev][0]
                adapter.change_status(prev, "on_path")
                window_update(screen, clock, background_colour, grid_colour, \
                              columns, rows, x_min, y_min, interval)

    window_update(screen, clock, background_colour, grid_colour, \
                              columns, rows, x_min, y_min, interval)


