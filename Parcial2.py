import numpy as np
import matplotlib.pyplot as plt
import tsplib95
from tsplib95 import load
import time

class TSP:

   def load_initial_variables(self, file_path: str, n_ants: int, n_iters: int, alpha: float = 1, beta: float = 1 , ro: float = 0.5):
      """
      Initialize the TSP instance with the given parameters.
      
      Parameters:
      file_path (str): The path to the TSP instance file.
      n_ants (int): The number of ants to use in the algorithm.
      n_iters (int): The number of iterations for the algorithm.
      alpha (float): The influence of pheromone on the path selection.
      beta (float): The influence of distance on the path selection.
      ro (float): The pheromone evaporation rate.
      """
      self.n_ants = n_ants
      self.n_iters = n_iters
      self.alpha = alpha
      self.beta = beta
      self.ro = ro
      self.cities, self.distances= self.load_tsp_instance(file_path)

   #Load the TSP instance from a file
   def load_tsp_instance(self, file_path):
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
      
      d = self.calculate_distances(problem, len(cities))
      return cities, d
   
   def calculate_distances(self, cities: tsplib95, n: int):

      d = np.zeros([n,n])
      
      for i in range(1, n+1):
         for j in range(1, n+1):
               if i == j:
                  d[i-1, j-1] = 0
                  continue
               
               d[i-1, j-1] = cities.get_weight(i, j)
      
      return d

   def plot_path(self, cities, path):
      for i in range(len(path) - 1):
         ini = cities[path[i]]
         fin = cities[path[i+1]]
         plt.arrow(ini[0], ini[1], fin[0] - ini[0], fin[1] - ini[1])
      ini = cities[path[-1]]
      fin = cities[path[0]]
      plt.arrow(ini[0], ini[1], fin[0] - ini[0], fin[1] - ini[1])

   def solve(self):
      n = len(self.cities) #Número de ciudades
      #ejercicio
      #Definir una funcion para calcular la matriz de distancias dij

      d = self.distances

      #nij = 1/d
      #print(f'Actractivness: {nij})

      tho = np.ones([n,n])
      delta = self.ro # Factor de refuerzo
      best_path = []
      best_p_length = np.inf

      maxIter = self.n_iters
      n_ants = self.n_ants

      inicio = time.time()
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
                  pij[j] = tho[current_city, unvisited_city]**self.alpha*(1/d[current_city, unvisited_city])**self.beta

               pij /= np.sum(pij)

               #choosing the next city
               next_city = np.random.choice(unvisited, p=pij)
               # print(f'Next city: {next_city}')
               path.append(int(next_city))
               path_length += d[current_city, next_city]
               # print(path_length)

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
         tho *= (1-self.ro)

         #reinforce factor
         for path, path_length in zip(paths, path_lengths):
            # print(f'Path: {path}, path_length: {path_length}')
            for i in range(n - 1):
               tho[path[i], path[i + 1]] += delta / path_length
            tho[path[-1], path[0]] += delta / path_length

      self.best_path = best_path
      self.best_p_lenght = float(best_p_length)

      fin = time.time()
      total_time = fin - inicio

      return self.best_path, self.best_p_lenght, total_time
   
   def get_cities(self):
      """
      Returns the coordinates of the cities.
      """
      return self.cities

   def get_soluction(self):
      """
      Returns the best path and its length.
      """

      return self.best_path, self.best_p_lenght
   
   def get_distances(self):
      """
      Returns the distance of the best path.
      """
      return self.distances

   def graph_soluction(self):
      """
      Plot the solution of the TSP problem.
      """
      plt.scatter(self.cities[:,0],self.cities[:,1], c='blue', alpha=0.5)

      for i in range(len(self.cities)):
         plt.text(self.cities[i,0], self.cities[i,1], str(i), fontsize=10)
      plt.grid()

      self.plot_path(self.cities, self.best_path)

      plt.show()
