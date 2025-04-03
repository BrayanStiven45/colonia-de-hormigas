import tsplib95

#Load the TSP instance from a file
def load_tsp_instance(file_path):
    """
    Load a TSP instance from a file using tsplib95.
    
    Parameters:
    file_path (str): The path to the TSP instance file.
    
    Returns:
    problem (tsplib95.models.TSP): The loaded TSP problem instance.
    """
    problem = tsplib95.load(file_path)
    return problem

ini = load_tsp_instance('initializer_files/ulysses16.tsp')
nodes = ini.node_coords
cities = [cord[1] for cord in nodes.items()]


print(len(cities))
print(cities)