
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Cell:
    """each cell is a dsu component"""
    x: int
    y: int
    is_active: bool = field(default=True)

@dataclass(frozen=True)
class Wall:
    """remembers which 2 cells it connects"""
    cell_a: Cell = field(compare=True)
    cell_b: Cell = field(compare=True)

# check the following again
# reasoning is Wall(cell_a, cell_b) == Wall(cell_b, cell_a)
    @classmethod
    def make(cls, a: Cell, b: Cell) -> cls:
        if (b.x, b.y) < (a.x, a.y):
            a, b = b, a
        return cls(a, b)




