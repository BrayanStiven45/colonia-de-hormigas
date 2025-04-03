from Parcial2 import TSP

tsp = TSP()

tsp.load_initial_variables("initializer_files/burma14.tsp", 100, 100, 1, 1, 0.5)

best_path, best_lenght = tsp.solve()
distances = tsp.get_distances()
cities = tsp.get_cities()
# print("Distances:", distances)
# print("Cities:", cities)
print("Best path:", best_path)
print("Best distance:", best_lenght)
tsp.graph_soluction()