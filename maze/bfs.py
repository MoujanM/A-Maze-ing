
import numpy as np
from collections import deque

from maze.exporter import Directions
from maze.data import Cell, Wall
from maze.graph import Graph

class BFS():
    def __init__(self, cells: list[Cell], walls: list[Wall],
                 maze: list[Wall]) -> None:
        self.adj_map = self._build_adj(cells, walls, maze)


    def _build_adj(self, cells: list[Cell], walls: list[Wall],
                   maze: list[Wall]) -> dict[Cell, list[Cell]]:
        
        adj_map: dict[Cell, list[Cell]] = {cell: [] for cell in cells}

        open_walls: list[Wall] = set(walls) - set(maze)
        for wall in open_walls:
            adj_map[wall.cell_a].append(wall.cell_b)
            adj_map[wall.cell_b].append(wall.cell_a)

        return adj_map


    def solve_maze(self, entry_point: Cell, exit_point: Cell) -> list[Cell]:
        # actual BFS implementation
        
        v_num: int = len(self.adj_map)
        visited: set[Cell] = {entry_point}
        came_from: dict[Cell, Cell | None] = {start: None}

        q = deque()
        q.append(entry_point)

        while q:
            current = q.popleft()
            if current == exit_point:
                break

            for neighbour in adj_map[current]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    came_from[neighbour] = current
                    q.append(neighbour)

        solution: list[Cell] = []
        crumbs: Cell = exit_point
        while crumbs is not None:
            solution.append(crumbs)
            crumbs = came_from[crumbs]
        solution.reverse()
        
        return solution
