from typing import TypeVar
from maze.structs import Directions


class Exporter:

    def __init__(self, graph: Graph, maze: list[Wall], solution: list[Cell], specs: MazeSpecs) -> None:
        self._dir_dict: dict[tuple, str] = {(d.value[0], d.value[1]): d for d in Directions}
        self.all_cells: list[Cell] = graph.cells
        self.maze_walls: list[Wall] = maze
        self.solution_path = solution
        self.ent, self.ext: tuple[int, int] = specs.entry_point, specs.exit_point
        self.output_file: str = specs.output_name
        

    def _build_bitmask(self) -> dict[C, int]:
        # separate the concerns
        # compute bitmasks
        c_bits: dict[C, int] = {c: 0 for c in c_items}

        for wall in self.maze_walls:
            dx = wall.b.x - wall.a.x
            dy = wall.b.y - wall.a.y
            a_direction = self._dir_dict[(dx, dy)]
            b_direction = self._dir_dict[(-dx, -dy)]
            c_bits[wall.a] |= (1 << a_direction.value[2])
            c_bits[wall.b] |= (1 << b_direction.value[2])

        return c_bits

    def _build_path_str(self) -> list[str]:
        # compute path str from list
        path_str: list[str] = []
        for c_a, c_b in zip(self.solution_path, self.solution_path[1:]):
            dx = c_b.x - c_a.x
            dy = c_b.y - c_a.y
            path_dir = self._dir_dict[(dx, dy)]
            path_str.append(path_dir.name[0])
        return path_str

    def _build_grid(self) -> list[str]:
        # build list of output str from bitmask
        bitmask: dict[C, int] = self._build_bitmask()
        lookup_dict: dict[tuple, int] = {(c.x, c.y): bits for c, bits in bitmask.items()}
        max_x: int = max(c.x for c in c_bits)
        max_y: int = max(c.y for c in c_bits)

        string_lst: list[str] = []
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                string_lst.append(format(lookup_dict[(x,y)], 'x'))
        return string_lst

    def write_to_file(self) -> None:
        # writes to output file
        grid_str: list[str] = self._build_grid()
        path_str: str = self._build_path_str()
        entry: str = ','.join(self.ent)
        extry: str = ','.join(self.ext)
        try:
            with open(self.output_file) as f:
                f.write('\n'.join(grid_str))
                f.write('\n')
                f.write('\n'.join([entry, extry]))
                f.write('\n')
                f.write(path_str)
                f.write('\n')
        except FileExistsError, Exception as e:
            print(f"Error writing to output - {e}")




            