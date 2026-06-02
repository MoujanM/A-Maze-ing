
import sys
from src.graph import Graph
from src.parser import ConfigParser
from maze.generator import KruskalGenerator, WilsonGenerator
from maze.exporter import Exporter
from maze.bfs import BFS


def main():
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        try:
            parser = ConfigParser()
            input_config = parser.read_txt(file_name)
            maze_specs = parser.validate_config(input_config)
            graph = Graph(maze_specs)
            if maze_specs.perfect:
                generator = KruskalGenerator()
            else:
                generator = WilsonGenerator()
            maze = generator.generate(graph)
            maze_solver = BFS(graph, maze)
            solution = maze_solver.solve_maze(maze_specs.entry_point,
                                              maze_specs.exit_point)
            exporter = Exporter(graph, maze, solution, maze_specs)
            exporter.write_to_file()
        except Exception as e:
            print(e)
            return 1


main()
