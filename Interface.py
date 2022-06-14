#Absolute mess of a program I have to say
#Was supposed to be a nice solution but as per usual, it got out of control

class Intermediate():

    colours = {"current": (255, 255, 0), "accessible": (255, 140, 0), \
               "visited": (0, 255, 0), "on_path": (0, 0, 255), \
               "obstacle": (255, 255, 255), "unvisited": (0,0,0),
               "start": (255, 0, 0), "goal": (255, 215, 0)}

    def __init__(self, graph, grid, grid_interval, rows, columns, x_min, y_min):

        #graph: Graph of the grid.
        #grid: dictionary of node IDs from the graph to the grid Tile instances.
        #grid_interval: int representing the width of a Tile on screen in px.
        #rows: int, number of rows of the grid.
        #columns: int, number of columns of the grid.
        #grid_x_min: the x-coordinate of top left corner of the entire grid.
        #grid_y_min: the y-coordinate of the top right corner of the entire grid.

        self.graph = graph
        self.grid = grid
        self.grid_interval = grid_interval
        self.rows = rows
        self.columns = columns 
        self.grid_x_min = x_min
        self.grid_y_min = y_min
        # self.grid_gen_method = grid_gen_method
        # self.graph_gen_method = graph_gen_method
        
    def change_status(self, node_id, code_word):
        #Used for changing the Tile colour in simple cases - can be used in 
        #the A* algorithm and in main.
        tile = self.grid[node_id]
        if tile.get_colour() == Intermediate.colours["obstacle"]:
            self.obstacle(node_id)
        self.grid[node_id].set_colour(Intermediate.colours[code_word])

    def obstacle(self, node_id):
        #Special case of change_status - adding/removing obstacles is not purely 
        #visual, as it requires changing the accessible edges too.

        tile = self.grid[node_id]
        if tile.get_colour() == Intermediate.colours["unvisited"]:
            neighbours = self.graph.neighbours(node_id)
            for neighbour in neighbours:
                self.graph.edge_remove(node_id, neighbour)
            self.grid[node_id].set_colour(Intermediate.colours["obstacle"])
        else:
            #Generates all legitimate neighbours to the tile in question and 
            #finds their Cartesian distances.
            neighbours = {(x, y): cartesian_distance(x, y, node_id[0], node_id[1]) \
                          for x in range(node_id[0]-1, node_id[0] + 2) \
                          for y in range(node_id[1]-1 , node_id[1] + 2) \
                          if -1 < x < self.columns and -1 < y < self.rows}
            for neighbour in neighbours:
                neighbour_colour = self.grid[neighbour].get_colour()
                if neighbour_colour == Intermediate.colours["unvisited"]:
                    self.graph.bi_edge_edit(node_id, neighbour, \
                        neighbours[neighbour])
            self.grid[node_id].set_colour(Intermediate.colours["unvisited"])

    def pos_to_id(self, pos):
        #Hash-like function. Maps position from grid to a legitimate ID.
        return ((pos[0] - self.grid_x_min)//self.grid_interval, \
                (pos[1] - self.grid_y_min)//self.grid_interval)

    def update_grid(self, columns, rows, start_x, start_y, target_x, target_y):
        if columns != self.columns or rows != self.rows:
            #Regenerate grid from scratch.
            self.graph


def cartesian_distance(x0, y0, x1, y1):
    return ((x0 - x1)**2 + (y0 - y1)**2)**0.5