import maze
from random import randint


# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    backtrack = []
    total_cells = len(m.maze_array)
    current_cell = m.maze_array[randint(0, total_cells-1)]
    visited_cells = 1
    while visited_cells < total_cells:
        neighbors = m.cell_neighbors(current_cell)
        if len(neighbors) >= 1:
            new_cell, index = neighbors[randint(0, len(neighbors)-1)]
            m.connect_cells(current_cell, new_cell, index)
            backtrack.append(current_cell)
            current_cell = new_cell
            visited_cells += 1
        else:
            current_cell = backtrack.pop()
        m.refresh_maze_view()
    m.state = "solve"


def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()
