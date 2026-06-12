import os

from src.renderer import MazeRenderer
from src.themes import DEFAULT_THEME, NEON_THEME, DARK_THEME

from mazegen.structs import MazeSpecs, Cell

from mazegen.graph import Graph
from mazegen.generator import MazeGenerator
from src.exporter import Exporter


def clear_screen() -> None:
    """Clear terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def generate_maze(
    specs: MazeSpecs,
    # graph: Graph,
    generator: MazeGenerator,
) -> tuple[list[list[int]], list[tuple[int, int]], list[Cell]]:

    generator._execute()
    maze_raw = generator.maze_structure
    path_raw = generator.solution
    graph: Graph = generator._graph

    exporter = Exporter(graph.cell_lookup, maze_raw, path_raw, specs)
    exporter.write_to_file()

    maze = exporter._maze_grid
    path = [(c.x, c.y) for c in path_raw]
    cells = graph.cells.copy()

    return maze, path, cells


def run_ui(specs: MazeSpecs, generator: MazeGenerator) -> None:
    """Run terminal UI."""

    entry = specs.entry_point
    exit_ = specs.exit_point

    maze, path, cells = generate_maze(specs, generator)

    show_path = True
    theme = DEFAULT_THEME

    while True:

        clear_screen()

        renderer = MazeRenderer(
            maze=maze,
            cells=cells,
            entry=entry,
            exit_=exit_,
            path=path if show_path else None,
            theme=theme,
        )

        renderer.render()

        print("\nCommands:")
        print("[p] Toggle path")
        print("[r] Regenerate maze")
        print("[t] switch theme")
        print("[q] Quit")

        command = input("\n> ").strip().lower()

        if command == "q":
            break

        elif command == "p":
            show_path = not show_path

        elif command == "r":
            if specs.seed:
                show_path = True
            else:
                maze, path, cells = generate_maze(specs, generator)
                show_path = True

        elif command == "t":
            if theme == DEFAULT_THEME:
                theme = NEON_THEME
            elif theme == NEON_THEME:
                theme = DARK_THEME
            else:
                theme = DEFAULT_THEME
