
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Cell:
    """each cell is a dsu component"""
    x: int
    y: int

@dataclass(frozen=True)
class Wall:
    """remembers which 2 cells it connects"""
    cell_a: Cell = field(compare=True)
    cell_b: Cell = field(compare=True)



