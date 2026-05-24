from typing import TypeVar


C = TypeVar('C')
W = TypeVar('W')


class Exporter:

    def hex_exporter(self, c_items: list[C], w_items: list[W]) -> dict:
        """
        Function takes list of cells, and walls.
        Input walls are result of generator - closed walls in maze.
        """
        c_bits: dict[C, int] = {c: 0 for c in c_items}
        
        directions_dict = {(d.value[0], d.value[1]): d for d in Directions}

        for item in w_items:
            dx = item.b.x - item.a.x
            dy = item.b.y - item.a.y
            a_direction = directions_dict[(dx, dy)]
            b_direction = directions_dict[(-dx, -dy)]
            c_bits[item.a] |= (1 << a_direction.value[2])
            c_bits[item.b] |= (1 << b_direction.value[2])

        return c_bits

    def output_file(self, c_bits: dict[C, int], file_name: str) -> None:
        lookup_dict: dict[tuple, int] = {(c.x, c.y): bits for c, bits in c_bits.itesm()}
        max_x: int = max(c.x for c in c_bits)
        max_y: int = max(c.y for c in c_bits)
        
        try:
            with open(file_name, 'x') as f:
                for y in range(max_y + 1):
                    for x in range(max_x + 1):
                        f.write(format(lookup_dict[(x,y)], 'x'))
                    f.write("\n")
        except FileExistsError as e:
            print(f"Error writing to output - {e}")

        # add aditional entry, exit, path 






            