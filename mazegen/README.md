# Mazegen Documentation

`mazegen` offers high-performance maze generation utilizing two distinct algorithms depending on your desired topological outcome:

**Kruskal's Algorithm** (`PERFECT=True`): Generates a mathematically perfect maze (a minimum spanning tree with exactly one unique path between any two points).

**Wilson's Algorithm** (`PERFECT=False`): Generates an organic, imperfect loop-erased random walk maze, with uniform spanning tree properties.

An integrated **Breadth-First Search (BFS)** pathfinder automatically solves the generated maze layout, finding a path between specified entry and exit coordinates.

## Installation

To use mazegen package, install it in virtual env using the following command:

```bash
pip install mazegen-1.0.0-py3-none-any.whl
```
## Basic Usage

You can instantiate `MazeGenerator` by passing it either a file path to a text configuration file containing key-value parameters, or passing parameters directly as a python dictionary.
Note parameters `perfect` and `seed` are optional and can be ommitted.

```bash
# example of contents for a config.txt file
WIDTH=15
HEIGHT=15
ENTRY=0,0
EXIT=14,14
OUTPUT_FILE=my_maze.txt
PERFECT=True
SEED=42
```
```python
# example of a valid python dict
custom_config = {
    "width": 20,
    "height": 20,
    "perfect": True,
    "entry_point": (0, 0),
    "exit_point": (19, 19),
    "seed": 42
}
```

Desired config can be passed directly to the contructor. The `MazeGenerator` class handles parsing, validation, layout generation, and path solving automagically upon instantiation.

```python
from mazegen.generator import MazeGenerator

# 1. Instantiate and execute the pipeline
maze = MazeGenerator("config.txt")
# alternatively maze = MazeGenerator(custom_config)

# 2. Access the generated layout of standing walls
walls = maze.maze_structure
print(f"Generated maze with {len(walls)} standing walls.")

# 3. Access the solved coordinates list (the path)
path = maze.solution
print(f"Solution path length: {len(path)} steps.")
for cell in path[:5]:
    print(f"Step: ({cell.x}, {cell.y})")
```
## Access to Data Structures

he package provides direct structural access to the underlying graph components via exposed read-only properties:

**`maze_structure`**
Exposes a list[Wall] containing all remaining standing walls in the maze.
Each Wall object connects two Cell instances:

```python
for wall in maze.maze_structure[:3]:
    cell_a = wall.cell_a
    cell_b = wall.cell_b
    print(f"Wall stands between ({cell_a.x}, {cell_a.y}) and ({cell_b.x}, {cell_b.y})")
    print(f"Is boundary wall? {wall.is_boundary}")
```

**`solution`**
Exposes a list[Cell] representing the continuous sequence of cells starting at the entry cell and ending at the exit cell.

```python
# Print the exact coordinates traversed by the pathfinder
path_coords = [(cell.x, cell.y) for cell in maze.solution]
print("Solved Path:", " -> ".join(map(str, path_coords)))
```






