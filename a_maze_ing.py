
import sys
import maze

if len(sys.argv) == 2:
    file_name = sys.argv[1]
    try:
        input_config = maze.ConfigParser.read_txt(file_name)
        maze_specs = maze.ConfigParser.validate_config(input_config)
    except Exception as e:
        print(e)
        return 1

    graph = maze.Graph(maze_specs)
    maze = maze.KruskalGenerator(graph, maze_specs.perfect)

    # Exporter.hex_export(graph.cells, maze)

    



    