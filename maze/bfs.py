
import numpy as np
from collections import deque
from maze.structs import Cell, Wall, Directions
from src.graph import Graph

class BFS():
    def __init__(self, graph: Graph, maze: list[Wall]) -> None:
        self.all_cells: list[Cell] = graph.cells
        self.all_walls: list[Wall] = graph.walls
        self.maze = maze
        self.adj_map = self._build_adj(all_cells, all_walls, maze)


    def _build_adj(self) -> dict[Cell, list[Cell]]:
        
        adj_map: dict[Cell, list[Cell]] = {cell: [] for cell in self.all_cells}

        open_walls: set[Wall] = set(self.all_walls) - set(self.maze)
        for wall in open_walls:
            adj_map[wall.cell_a].append(wall.cell_b)
            adj_map[wall.cell_b].append(wall.cell_a)
        return adj_map


    def solve_maze(self, entry_point: tuple[int, int], exit_point: tuple[int, int]) -> list[Cell]:
        # actual BFS implementation
        entry_cell: Cell = Cell(*entry_point)
        exit_cell: Cell = Cell(*exit_point)
        visited: set[Cell] = {entry_cell}
        came_from: dict[Cell, Cell | None] = {entry_cell: None}

        q = deque()
        q.append(entry_cell)

        while q:
            current = q.popleft()
            if current == exit_cell:
                break

            for neighbour in self.adj_map[current]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    came_from[neighbour] = current
                    q.append(neighbour)

        solution: list[Cell] = []
        crumbs: Cell = exit_cell
        while crumbs is not None:
            solution.append(crumbs)
            crumbs = came_from.get(crumbs)
        solution.reverse()
        
        return solution
