from typing import TypeVar

C = TypeVar('C')
W = TypeVar('W')

class Exporter:

    def hex_export(items1: list[C], items2: list[W]) -> dict:
        c_bits: dict[C, int] = {c: 0 for c in items1}

        for item in items2:
            pass