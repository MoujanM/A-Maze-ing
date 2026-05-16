from abc import ABC, abstractmethod
from maze.graph import Graph
from maze.data import Wall

class MazeGenerator(ABC):

    @abstractmethod
    def generate(self, graph: Graph, perfect: bool) -> list[Wall]:
        walls: list[Wall] = graph.walls
        # algorithm implementation goes here
        return walls


class KruskalGenerator(MazeGenerator):

    def generate(self, graph: Graph, perfect: bool) -> list[Wall]:
        import random
        from maze.dsu import DSU

        walls = graph.walls
        dsu = DSU(graph.cells)

        removed_walls: list[Wall] = []
        random.shuffle(walls)
        dsu_count = len(graph.cells)
        for wall in walls:
            if not dsu.connected(wall.cell_a, wall.cell_b):
                root_a = dsu.find(wall.cell_a)
                root_b = dsu.find(wall.cell_b)

                dsu.union(root_a, root_b)
                dsu_count -= 1
                removed_walls.append(wall)
            if dsu_count == 1:
                break
        
        for wall in removed_walls:
            walls.remove(wall)
        
        if not perfect:
            extra = round(len(walls) * 0.05)
            random.shuffle(walls)
            for wall in walls[:extra]:
                walls.remove(wall)

        return walls


