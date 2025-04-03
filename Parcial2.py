from turtle import distance
import numpy as np
import matplotlib.pyplot as plt

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

n = 5 #Número de ciudades
np.random.seed(0)
cities = np.random.uniform(0,10,[n,2])
plt.scatter(cities[:,0],cities[:,1], c='blue', alpha=0.5)
for i in range(n):
    plt.text(cities[i,0], cities[i,1], str(i), fontsize=10)
plt.grid()
plt.show()

d = distances(cities)
# print(d)

nij=1/d
# print(f'Atractividades:\n{nij}')

to = np.ones([n,n])
# print(f'Matriz de feromonas: {to}')

tho = np.ones([n,n])
ro = 0.5 #Factor de evaporacion
delta = ro 
beta = 1
alpha = 1
best_path = []


max_iter = 1
n_ants = 1

for iter in range(max_iter):
    paths = []
    path_lengths = []

    #for each ant
    for ant in range(n_ants):
      #setting S set unvisited cities
      S = np.zeros(n) #N cities
      current_city = np.random.randint(0, n)
      # print(f'Current city: {current_city}')
      S[current_city] = True
      # print(S)
      path = [current_city]
      path_length = 0

      while False in S:
        unvisited = np.where(S==False)[0] #first column (axes)
        print(unvisited)
        pij = np.zeros(len(unvisited))

        for j, unvisited_city in enumerate(unvisited):
          pij[j] = tho[current_city, unvisited_city]**alpha* 1 / d[current_city, unvisited_city]**beta

        pij /= np.sum(pij)
        # print(pij)
        # print(np.sum(pij))

        #chosing the next city
        next_city = np.random.choice(unvisited, p=pij)
        # print(f'Next city: {next_city}')
        path.append(next_city)
        path_length += d[current_city, next_city]
        print(path_length)

        #updating the current city
        current_city = next_city
        S[current_city] = True

        # if len(path) == n:
        #   path_length += d[current_city, path[0]]
        #   path.append(path[0])

        # plt.plot(cities[path,0], cities[path,1], 'o-')
        # plt.grid()
        # plt.show()
      
      #last arc
      path_length += d[current_city, path[0]]
      #print(path_length)
      paths.append(path)
      path_lengths.append(path_length)

      if path_length<best_p_length:
         best_p_length=path_length
         best_path=path
    
    #updating pheromones (tho)
    tho*=(1-ro)
    #reinforce factor
    for path, path_length in zip(paths, path_lengths):
       # print(f'path: {path}, length: {path_length}')
       for i in range(n-1):
          tho[path[i], path[i+1]]+=delta/path_length
       tho[path[-1], path[0]]+=delta/path_length
    print(tho)

print(f"Pheromones: {tho}")
print(f'best: {best_path}, length: {best_p_length}')
plot_path(cities, best_path)

#Encontrar el mejor path obtenido hasta ahora de forma aleatoria