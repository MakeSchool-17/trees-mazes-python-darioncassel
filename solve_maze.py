import maze
import generate_maze
import sys
from random import randint
from collections import deque


# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(m):
    backtrack = []
    current_cell = 0
    visited_cells = 0
    goal = m.cell_index(m.w_cells-1, m.h_cells-1)
    while current_cell != goal:
        neighbors = m.cell_neighbors(current_cell)
        if len(neighbors) >= 1:
            new_cell, index = neighbors[randint(0, len(neighbors)-1)]
            m.visit_cell(current_cell, new_cell, index)
            backtrack.append(current_cell)
            current_cell = new_cell
            visited_cells += 1
        else:
            m.backtrack(current_cell)
            current_cell = backtrack.pop()
        m.refresh_maze_view()
    m.state = "idle"


# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    queue = deque()
    current_cell = 0
    in_dir = 0b0000
    visited_cells = 0
    queue.append((current_cell, in_dir))
    goal = m.cell_index(m.w_cells-1, m.h_cells-1)
    while current_cell != goal:
        current_cell, in_dir = queue.popleft()
        m.bfs_visit_cell(current_cell, in_dir)
        visited_cells += 1
        m.refresh_maze_view()
        neighbors = m.cell_neighbors(current_cell)
        for neighbor in neighbors:
            queue.append(neighbor)
    m.reconstruct_solution(current_cell)
    m.state = "idle"
    pass


def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
