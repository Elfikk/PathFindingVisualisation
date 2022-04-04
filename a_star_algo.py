from Graph import Graph, initialise_grid_graph
from Heap import Min_Heap

def a_star_path(graph, target, start = (0,0)):

    open_set = Min_Heap([0], [(start, None)])
    closed_set = {} #Closed set - key is position tuple, data is previous position and g.
    h = {}
    g = {}
    g[start] = 0

    for node in graph.map_to_row:
        cartesian_distance = ((node[0] - target[0])**2 + (node[1] - target[1])**2)**0.5
        h[node] = cartesian_distance

    # print(h)

    while len(open_set) != 0:
        f, data = open_set.pop()
        pos, previous_pos = data
        current_g = g[pos]

        neighbours = graph.neighbours(pos)

        if target in neighbours:
            closed_set[pos] = previous_pos, current_g
            closed_set[target] = pos, current_g + graph.edge(pos, target)
            return reconstruct_path(closed_set, target, start)

        for neighbour_pos in neighbours:
            neighbour_g = current_g + graph.edge(pos, neighbour_pos)

            if neighbour_pos in closed_set:
                neighbour_prev_cost = closed_set[neighbour_pos][1]
                if neighbour_prev_cost > neighbour_g:
                    closed_set[neighbour_pos] = [pos, neighbour_g]
            else:
                if neighbour_pos in g:
                    neighbour_prev_cost = g[neighbour_pos] + h[neighbour_pos]
                    if neighbour_prev_cost > neighbour_g:
                        pass
                else:
                    neighbour_cost = neighbour_g + h[neighbour_pos]
                    open_set.insert(neighbour_cost, (neighbour_pos, pos))
                    g[neighbour_pos] = current_g + graph.edge(pos, neighbour_pos)

        closed_set[pos] = previous_pos, current_g

def reconstruct_path(closed_set, target, start):
    path = [target]
    prev = target
    while prev != start:
        prev = closed_set[prev][0]
        path.append(prev)
    return path[::-1]

if __name__ == "__main__":

    # g = Graph()

    # for i in range(5):
    #     g.add_node((0, i))

    # for i in range(4):
    #     g.bi_edge_edit((0, i), (0, i + 1), 1)

    # g.add_node((1, 4))
    # g.bi_edge_edit((0, 4), (1, 4), 1)

    # print(g.adj_matrix)

    # print(a_star_path(g, (1, 4)))

    g = initialise_grid_graph(5, 5)

    print(g.neighbours((0,0)))

    print(a_star_path(g, (1, 4)))