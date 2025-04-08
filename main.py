from Parcial2 import TSP

tsp = TSP()

# Load the TSP instance from a file using tsplib95 
# and set the parameters for the algorithm path_file, n_ants, n_iters, alpha, beta, ro
tsp.load_initial_variables("initializer_files/berlin52.tsp", 60, 1000, 1, 1, 0.5)

best_path, best_lenght, total_time = tsp.solve()
distances = tsp.get_distances()
cities = tsp.get_cities()
# print("Distances:", distances)
# print("Cities:", cities)
print("Best path:", best_path)
print("Best distance:", best_lenght)
print("Total time:", total_time)
tsp.graph_soluction()