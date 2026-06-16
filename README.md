*This project has been created as part of the 42 curriculum by mmirdama, brisnovs*

# A-Maze-ing

A modular maze-generation, solver, and visualizer programme. 

## Description

A-Maze-ing is a Python-based maze generation and solving framework. Reading from a plain-text config file (or a python dictionary - see package documentation below), the program chooses between two algorithms to generate a perfect/imperfec maze, solves generated maze, renders visualization in the terminal, and writes result to a hex-encoded output file. The core generation logic is packaged as a standalone, pip-installable Python package (`mazegen`).

## Key Features

- **Multiple Generation Algorithms**: Choose between Kruskal's algorithm (for perfect mazes) or Wilson's algorithm (for varied maze characteristics)
- **Maze Solving**: Uses Breadth-First Search (BFS) to find the shortest path from entry to exit
- **Configurable Specifications**: Easy configuration via text files with validation using Pydantic
- **Graph-Based Representation**: Represents mazes as graphs with cells and walls
- **Easter Egg**: Embeds the number "42" in the center of larger mazes as a fun detail
- **Automated Output**: Exports solved mazes to text files with visual representation
- **Interactive terminal UI**: Toggle path display, regenerate, and switch colour themes
- **Reusable package**: `mazegen` can be imported independently or installed via pip

## Instructions
```bash
make install    # install virtual env + all necessary dependencies
make lint       # check code with flake8, mypy
make run        # run a_maze_ing.py with a sample config file provided

make clean      # find and remove caches
make clean-venv # remove caches and delete virtual env
```

## Configuration File Structure

The `sample_config.txt` file defines maze specifications using a simple `KEY=VALUE` format.

### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `WIDTH` | Integer | Width of the maze (≥ 2) | `10` |
| `HEIGHT` | Integer | Height of the maze (≥ 2) | `10` |
| `ENTRY` | Tuple(int, int) | Starting coordinates `x,y` | `1,3` |
| `EXIT` | Tuple(int, int) | Ending coordinates `x,y` | `9,8` |
| `OUTPUT_FILE` | String | Output filename (must end in `.txt`) | `maze.txt` |
| `PERFECT` | Boolean | Generate perfect maze if `True` | `False` |

### Optional Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `SEED` | Integer | Random seed for reproducibility (≥ 1) | `42` |


# Mazegen Documentation; Project Algorithms

`mazegen` offers high-performance maze generation utilizing two distinct algorithms depending on your desired topological outcome:

**Kruskal's Algorithm** (`PERFECT=True`): Generates a mathematically perfect maze (a minimum spanning tree with exactly one unique path between any two points).

**Wilson's Algorithm** (`PERFECT=False`): Generates an organic, imperfect loop-erased random walk maze, with uniform spanning tree properties.

An integrated **Breadth-First Search (BFS)** pathfinder automatically solves the generated maze layout, finding a path between specified entry and exit coordinates.

### Installallation

To use mazegen package, install it in virtual env using the following command:

```bash
pip install mazegen-1.0.0-py3-none-any.whl
```

### Basic Usage

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
from mazegen.src.generator import MazeGenerator

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
### Access to Data Structures

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
### Design Patterns Used

- **Abstract Base Class Pattern**: `MazeGenerator` allows extending with new algorithms
- **Strategy Pattern**: Different maze generation algorithms as interchangeable strategies
- **Validation with Pydantic**: Type-safe configuration handling
- **Separation of Concerns**: Parser, graph, generators, and solvers are independent







### Useful References

#### Maze Generation Algorithms
- [Kruskal's Algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)
- [Wilson's Algorithm](https://en.wikipedia.org/wiki/Loop-erased_random_walk)
- [Maze Generation Algorithms Comparison](http://www.amazeinc.com/mazes.html)

#### Graph Theory
- [Breadth-First Search (BFS)](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Disjoint Set Union](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)
- [Graph Representation](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics))

### Learning Resources

- Interactive maze algorithm visualizations: [Maze Generation Visualizer](https://www.netsecstudent.com/2021/08/maze-generator.html)
- Algorithm tutorials: [Computerphile - Maze Generation](https://www.youtube.com/watch?v=HyK_Q5rrcr4)
- Graph theory course: [Khan Academy - Graph Algorithms](https://www.khanacademy.org/computing/computer-science/algorithms)


