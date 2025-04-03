from turtle import distance
import numpy as np
import matplotlib.pyplot as plt
import tsplib95
from tsplib95 import load

#Load the TSP instance from a file
def load_tsp_instance(file_path):
   """
   Load a TSP instance from a file using tsplib95.
   
   Parameters:
   file_path (str): The path to the TSP instance file.
   
   Returns:
   cities (list): A list of coordinates of the cities in the TSP instance.
   """
   problem = tsplib95.load(file_path)
   nodes = problem.node_coords # Load the coordinates of the nodes
   cities = np.array([cord[1] for cord in nodes.items()]) # Extract the coordinates

   return cities


def distances(cities):
  n=len(cities)
  d=np.zeros([n,n])
  for i in range(n):
        for j in range(n):
            d[i,j]=np.linalg.norm(cities[i]-cities[j])

  return d

def plot_path(cities, path):
   for i in range(len(path) - 1):
      ini = cities[path[i]]
      fin = cities[path[i+1]]
      plt.arrow(ini[0], ini[1], fin[0] - ini[0], fin[1] - ini[1])
   ini = cities[path[-1]]
   fin = cities[path[0]]
   plt.arrow(ini[0], ini[1], fin[0] - ini[0], fin[1] - ini[1])

cities = load_tsp_instance('initializer_files/burma14.tsp')
n = len(cities) #Número de ciudades
np.random.seed(0)
print(cities)
plt.scatter(cities[:,0],cities[:,1], c='blue', alpha=0.5)

for i in range(len(cities)):
    plt.text(cities[i,0], cities[i,1], str(i), fontsize=10)
plt.grid()
plt.show()

#ejercicio
#Definir una funcion para calcular la matriz de distancias dij

d = distances(cities)

#nij = 1/d
#print(f'Actractivness: {nij})

tho = np.ones([n,n])
alpha = 1
beta = 1
#print(tho)
ro = 0.5 #Factor de evaporacion
delta = ro # Factor de refuerzo
best_path = []
best_p_length = np.inf

maxIter = 1
n_ants = 1

for iter in range(maxIter):
   paths = []
   path_lengths = []

   for ant in range(n_ants):
      # Setting S set univisited cities
      S = np.zeros(n) # n cities
      current_city = np.random.randint(n) #ith city
      #print(f'current city: {current_city})
      S[current_city] = True
      #print(S)
      path = [current_city]
      path_length = 0
      while False in S:
         unvisited = np.where(S==False)[0] #first column (axes)
         # print(unvisited)
         pij = np.zeros(len(unvisited))
         for j, unvisited_city in enumerate(unvisited):
            pij[j] = tho[current_city, unvisited_city]**alpha*(1/d[current_city, unvisited_city])**beta

         pij /= np.sum(pij)

         #choosing the next city
         next_city = np.random.choice(unvisited, p=pij)
         print(f'Next city: {next_city}')
         path.append(int(next_city))
         path_length += d[current_city, next_city]
         print(path_length)

         #Updating the current city
         current_city = next_city
         S[current_city] = True

   
   path_length += d[current_city, path[0]]
   path.append(path[0])

   #las arc

   # path_length += d[current_city, path[0]]
   #print(path_length)
   paths.append(path)
   path_lengths.append(path_length)
   # print(paths)

   if path_length < best_p_length:
      best_p_length = path_length
      best_path = path

   #updating pheromones (tho)
   tho *= (1-ro)

  #reinforce factor
   for path, path_length in zip(paths, path_lengths):
      # print(f'Path: {path}, path_length: {path_length}')
      for i in range(n - 1):
         tho[path[i], path[i + 1]] += delta / path_length
      tho[path[-1], path[0]] += delta / path_length
  #print(tho)



print(f'Best path: {best_path}')
print(f'Best path length: {best_p_length}')
plot_path(cities, best_path)
plt.show()