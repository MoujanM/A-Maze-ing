
import sys
from mazegen.src.structs import MazeSpecs
from mazegen.src.graph import Graph
from mazegen.src.generator import MazeGenerator
from utils.exporter import Exporter
from utils.ui import run_ui


def main() -> None:
    if len(sys.argv) == 2:
        config = sys.argv[1]

        try:
            generator_solver: MazeGenerator = MazeGenerator(config)
        except Exception as e:
            print(f"Program encountered an error - {e}")

        try:
            graph: Graph = generator_solver._graph
            maze_specs: MazeSpecs = generator_solver._specs
            if not generator_solver._graph._graph_mask.all():
                run_ui(maze_specs, generator_solver)
            else:
                exporter = Exporter(graph.cell_lookup,
                                    generator_solver.maze_structure,
                                    generator_solver.solution,
                                    maze_specs)
                exporter.write_to_file()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
