import pygame 
from PyQt5.QtWidgets import QApplication
from Interface import Intermediate
from a_star_algo import a_star_setup, visit_next_node, mark_neighbour
from PygameHandler import Handler
from UI import MainMenu, placeholder
import sys

#pygame setup
pygame.init()
done = False

#Some globals
background_colour = (0,0,0)
grid_colour = (255,255,255)

rows, columns = 20, 20
x_min, y_min = 140, 110
interval = 10

start = (0, 0)
target = (columns - 1, rows - 1)

handler = Handler(rows, columns, (1280,720), background_colour, grid_colour,\
    x_min, y_min, interval)

adapter = Intermediate(handler.graph, handler.grid, interval, rows, columns,\
    x_min, y_min, handler, start, target)

app = QApplication([])
menu = MainMenu(adapter.update_grid, adapter.start_algo, adapter.reset)
menu.setWindowTitle("Path Finding Visualisation Menu")
menu.update_grid_size(columns, rows)
menu.update_start(start)
menu.update_target(target)
menu.show()

while not done:

    for event in pygame.event.get():
        
        #Clicking the red cross quit cross
        if event.type == pygame.QUIT:
            done = True
            sys.exit(app.exec())

        #Left Mouse Button Click - Add/Remove Obstacle
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            position = event.pos
            if handler.grid_rectangle.collidepoint(position):
                id = adapter.pos_to_id(position)
                adapter.obstacle(id)

        #Middle Mouse Button Click - Set Start
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            position = event.pos
            if handler.grid_rectangle.collidepoint(position):
                adapter.change_status(adapter.start, "unvisited")
                id = adapter.pos_to_id(position)
                adapter.start = id
                adapter.change_status(id, "start")
                menu.update_start(id)

        #Right Mouse Button Click - Set Target
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            position = event.pos
            if handler.grid_rectangle.collidepoint(position):
                adapter.change_status(adapter.target, "unvisited")
                id = adapter.pos_to_id(position)
                adapter.target = id
                adapter.change_status(id, "goal")
                menu.update_target(id)

        #Spacebar - start algo
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE \
            or handler.start == True:

            handler.start = False

            open_set, closed_set, h, g = a_star_setup(adapter.graph, \
                                        adapter.start, adapter.target)

            neighbours = []

            while len(open_set) != 0 and neighbours != None:

                #Prevents pygame from believing the program has crashed - as it 
                #turns out, not handling events for a few seconds makes pygame 
                #assume a crash. pump() allows it to handle internal actions, so
                #the window remains up.
                pygame.event.pump() 

                open_set, closed_set, h, g, neighbours, pos, previous_pos =\
                    visit_next_node(adapter.graph, adapter.target, open_set, \
                                    closed_set, h, g, adapter)

                if neighbours != None:

                    for neighbour_pos in neighbours:
                        mark_neighbour(adapter.graph, open_set, closed_set, h, g, \
                                       adapter, pos, neighbour_pos)
                                
                        handler.window_update()

                closed_set[pos] = previous_pos, g[pos]
                adapter.change_status(pos, "visited")

                handler.window_update()

            if neighbours == None:
                path = [adapter.target]
                prev = adapter.target
                while prev != adapter.start:
                    prev = closed_set[prev][0]
                    adapter.change_status(prev, "on_path")
                    handler.window_update()

            print("No possible path.")

    handler.window_update()

sys.exit(app.exec())