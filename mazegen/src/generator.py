
from typing import Any
from mazegen.src.graph import Graph
from mazegen.src.parser import ConfigParser
from mazegen.src.structs import Wall, Cell, MazeSpecs
from mazegen.src.strategies import AlgorithmStrategy
from mazegen.src.strategies import KruskalGenerator, WilsonGenerator
from mazegen.src.bfs import BFS


class MazeGenerator():
    """Unified interface for generating and solving maze.
    Handles parsing, algorithm selection and solving."""

    def __init__(self, config: str | dict[str, Any]) -> None:

        parser = ConfigParser()
        if isinstance(config, str):
            input_config = parser.read_txt(config)
            self._specs: MazeSpecs = parser.validate_config(input_config)
        else:
            self._specs = parser.validate_config(config)

        self._graph: Graph = Graph(self._specs)
        self._maze: list[Wall] = []
        self._solution: list[Cell]
        self._execute()

    def _execute(self) -> None:
        algorithm: AlgorithmStrategy = WilsonGenerator()
        if self._specs.perfect:
            algorithm = KruskalGenerator()

        self._maze = algorithm.generate(self._graph)
        solver: BFS = BFS(self._graph, self._maze)
        self._solution = solver.solve_maze(self._specs.entry_point,
                                           self._specs.exit_point)

    @property
    def maze_structure(self) -> list[Wall]:
        return self._maze

    @property
    def solution(self) -> list[Cell]:
        return self._solution
