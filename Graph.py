from math import inf

class Graph():

    #General Graph with adjacency matrix approach.

    def __init__(self):

        #map_to_row and map_to_id are dictionaries where the key is the node
        #id and the row in the adjacency matrix respectively, to allow for
        #access to nodes directly.

        self.map_to_row = {}
        self.map_to_id = {}
        self.adj_matrix = []

    def add_node(self, id):
        #adds a node with specified id with no edges.
        dimension = len(self.adj_matrix)
        self.map_to_row[id] = dimension
        self.map_to_id[dimension] = id

        for i in range(dimension):
            self.adj_matrix[i].append(inf)

        self.adj_matrix.append([inf] * (dimension + 1))

    def edge_edit(self, id1, id2, weight):
        #Change the weight of the edge from node 1 to node 2 for 
        #non-bidirectional case.
        try:
            i, j = self.map_to_row[id1], self.map_to_row[id2]
        except KeyError:
            raise KeyError("Referenced node is not in the graph.")
        self.adj_matrix[i][j] = weight

    def bi_edge_edit(self, id1, id2, weight):
        #Change the weight of the edge between node with id1 and node with 
        #id2.
        try:
            i, j = self.map_to_row[id1], self.map_to_row[id2]
        except KeyError:
            raise KeyError("Referenced node is not in the graph.")
        self.adj_matrix[i][j] = weight; self.adj_matrix[j][i] = weight

    def edge_remove(self, id1, id2):
        #To avoid unecessary imports in other files.
        self.bi_edge_edit(id1, id2, inf)

    def neighbours(self, id):
        #Returns the ids and weights of the neighbours of the passed node.
        #Keys are neighbours, values are weights.
        index = self.map_to_row[id]
        neighbours = {self.map_to_id[x]: self.adj_matrix[index][x] for x\
                      in range(len(self.adj_matrix)) if \
                      self.adj_matrix[index][x] != inf}
        return neighbours

    def edge(self, id1, id2):
        #Returns the edge weight from node 1 to node 2.
        i, j = self.map_to_row[id1], self.map_to_row[id2]
        return self.adj_matrix[i][j]

    def generate_adjacency_dic(self):
        adj_dic = {self.map_to_id[x]: self.neighbours(self.map_to_id[x]) \
                   for x in range(len(self.adj_matrix))}
        return adj_dic
        
    def nodes(self):
        return list(self.map_to_row.keys())

def initialise_grid_graph(rows, columns, diag_cost = 2**0.5):

    g = Graph()

    # g.map_to_row = {(x,y): x + y*columns for x in range(columns) for y in \
    #                 range(rows)}
    # g.map_to_id = {row: pos for pos, row in g.map_to_row.items()}

    g.add_node((0,0))

    for y in range(1, rows):
        g.add_node((0, y))
        g.bi_edge_edit((0,y-1), (0,y), 1)

    for x in range(1, columns):
        g.add_node((x, 0))
        g.bi_edge_edit((x-1,0), (x, 0), 1)

    for y in range(1, rows):
        for x in range(1, columns):
            g.add_node((x, y))
            g.bi_edge_edit((x,y), (x-1, y), 1)
            g.bi_edge_edit((x,y), (x, y - 1), 1)
            g.bi_edge_edit((x,y), (x-1, y - 1), diag_cost)

    for y in range(1, rows):
        g.bi_edge_edit((0,y), (1,y-1), diag_cost)

    for x in range(1, columns):
        g.bi_edge_edit((x,0), (x-1,1), diag_cost)

    # for y in range(rows):
    #     for x in range(columns):
    #         g.add_node((x,y))
    
    # for y in range(rows):
    #     for x in range(columns):
    #         pass
    
    return g

# def grid_weight(x0,y0,x,y, diag = 2**0.5):
#     dist = (x - x0)**2 + (y - y0)**2
#     if dist > 2:
#         return inf
#     elif dist > 1:
#         return diag
#     return 1

if __name__ == "__main__":

    # g = Graph()

    # g.add_node((0,0))
    # g.add_node((0,1))
    # g.add_node((1,0))

    # print(g.adj_matrix)
    # print(g.map_to_id)
    # print(g.map_to_row)

    # # g.edge_edit((2,0), (0,0), 1)

    # g.edge_edit((0,0), (0,1), 1)
    
    # print(g.adj_matrix)

    # print(g.map_to_id[0] is (0,0))

    # print(g.neighbours((0,0)))

    # g.edge_edit((0,0), (1,0), 2)

    # print(g.neighbours((0,0)))

    # print(g.edge)

    g = initialise_grid_graph(4, 4)

    print(g.map_to_row.keys())
    print(g.neighbours((1,1)).keys())