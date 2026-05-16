
from maze.data import Wall, Cell
from maze.config_parser import MazeSpecs

class Graph():
    """Given a height & width, get all possible walls and cells"""
    
    def __init__(self, specs: MazeSpecs):
        self.width: int = specs.width
        self.height: int = specs.height

        self.cells: list[Cell] = self._build_cells()
        self.walls: list[Wall] = self._build_walls()

    def _build_cells(self) -> list[Cell]:
        cells = []
        for y in range(0, self.height):
            for x in range(0, self.width):
                cells.append(Cell(x, y))

        return cells

    def _inside_check(self, x: int, y: int) -> bool:
        # check to see if given coordinates within bounds of graph
        return 0 <= x < self.width and 0 <= y < self.height
    
    def _build_walls(self) -> list[Wall]:
        """
        Walls connect two cells together.
        func only checks two directions to avoid dups.
        """ 
        direction = [(1, 0), (0, 1)]
        walls = []

        for cell in self.cells:
            for dx, dy in direction:
                nx, ny = cell.x + dx, cell.y + dy
                if self._inside_check(nx, ny):
                    walls.append(Wall(cell, Cell(nx, ny)))
        return walls

            






        