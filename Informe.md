

<Center> 

# Algoritmo de Colonias de Hormigas para el Problema del Agente Viajero (TSP)

### Informe técnico desarrollado en Python
</Center>


## Tabla de Contenido
- [Algoritmo de Colonias de Hormigas para el Problema del Agente Viajero (TSP)](#algoritmo-de-colonias-de-hormigas-para-el-problema-del-agente-viajero-tsp)
    - [Informe técnico desarrollado en Python](#informe-técnico-desarrollado-en-python)
  - [Tabla de Contenido](#tabla-de-contenido)
  - [Introducción](#introducción)
  - [Descripción del Problema TSP](#descripción-del-problema-tsp)
  - [Descripción del Algoritmo de Colonias de Hormigas (ACO) en Python](#descripción-del-algoritmo-de-colonias-de-hormigas-aco-en-python)
    - [Se importan las librerías necesarias para realizar el algoritmo](#se-importan-las-librerías-necesarias-para-realizar-el-algoritmo)
    - [Se crea la clase TSP](#se-crea-la-clase-tsp)
  - [Pruebas](#pruebas)
    - [Instancias Pequeñas:](#instancias-pequeñas)
      - [Tablas](#tablas)
      - [Gráficas](#gráficas)
      - [Concluciones](#concluciones)
    - [Instancias Medianas:](#instancias-medianas)
      - [Tablas](#tablas-1)
      - [Gráficas](#gráficas-1)
      - [Concluciones](#concluciones-1)
    - [Instancias Grandes:](#instancias-grandes)
      - [Tablas](#tablas-2)
      - [Gráficas](#gráficas-2)
      - [Concluciones](#concluciones-2)

## Introducción

En este informe se aborda la implementación del algoritmo de Colonias de Hormigas (Ant Colony Optimization, ACO) para resolver el Problema del Agente Viajero (TSP). El objetivo del TSP es encontrar la ruta más corta posible que permita visitar un conjunto de ciudades una sola vez y regresar al punto de partida. Aunque puede parecer sencillo, este problema se vuelve muy complejo a medida que aumenta el número de ciudades, por lo que se utilizan algoritmos metaheurísticos para encontrar soluciones aproximadas.

El algoritmo de Colonias de Hormigas se basa en el comportamiento real de las hormigas cuando buscan comida. A través de la simulación del rastro y evaporación de feromonas, las hormigas artificiales logran construir rutas que, con el tiempo, tienden a mejorar y acercarse a la solución óptima.

La implementación fue desarrollada en Python, utilizando una estructura general del algoritmo vista en clase y que se fue implementando en python en el transcurso de la materia, con algunas adaptaciones necesarias. Para las pruebas, se usaron nueve archivos con extensión .tsp obtenidos del repositorio TSPLIB95, los cuales contienen instancias de diferentes tamaños: pequeñas (de 10 a 20 ciudades), medianas (de 50 a 100 ciudades), y grandes (más de 100 ciudades).

A lo largo del trabajo se realizaron distintos experimentos con los parámetros del algoritmo (como el número de hormigas, el valor de alfa y beta, la tasa de evaporación, entre otros) y se evaluó el rendimiento en función del tiempo de ejecución, la calidad de la solución, y la cercanía a la solución óptima. El propósito de este informe es poner en práctica lo aprendido en clase sobre metaheurísticas y demostrar cómo un algoritmo bioinspirado puede ser una alternativa eficiente frente a problemas difíciles de resolver por métodos exactos.

## Descripción del Problema TSP
El Problema del Agente Viajero (TSP) busca encontrar la ruta más corta para visitar un conjunto de ciudades exactamente una vez y regresar al punto de partida. Aunque parece simple, es un problema complejo ya que el número de posibles rutas crece rápidamente con más ciudades.

Este tipo de problema es muy común en áreas como logística y planificación de rutas. No hay un método eficiente para resolverlo de forma exacta cuando las instancias son grandes.

En este trabajo se usaron archivos .tsp del repositorio TSPLIB95, que contienen las coordenadas de las ciudades. A partir de estos datos, se aplicó el algoritmo de Colonias de Hormigas para encontrar la solución optima o soluciones aproximadas al problema.

## Descripción del Algoritmo de Colonias de Hormigas (ACO) en Python
El algoritmo de Colonias de Hormigas (Ant Colony Optimization o ACO) se basa en cómo las hormigas reales encuentran caminos cortos entre su nido y una fuente de alimento. En este caso, usamos esa lógica para encontrar rutas óptimas en el problema del Agente Viajero (TSP).

Cada “hormiga” del algoritmo representa una posible solución: una ruta que recorre todas las ciudades. Las decisiones de cada hormiga se basan en dos cosas: la cantidad de feromonas (que refleja qué tan buena ha sido una ruta) y la distancia (preferimos rutas más cortas). Al finalizar cada iteración, se actualizan las feromonas: se evaporan un poco, pero se refuerzan en los caminos más prometedores.

A continuación se explicara detalladamente la implementación:

### Se importan las librerías necesarias para realizar el algoritmo
  <pre>  import numpy as np 
  import matplotlib.pyplot as plt 
  import tsplib95 from tsplib95 
  import load import time  </pre>

  - **numpy:** Nos permite trabajar de manera eficiente con matrices y realizar operaciones matemáticas, fundamentales para la creación de la matriz de distancias entre las ciudades y para los cálculos durante el proceso iterativo.

  - **matplotlib:** Es utilizado para graficar y visualizar la ruta óptima encontrada, facilitando la interpretación visual de los resultados.

  - **tsplib95:** Permite leer y procesar archivos con extensión .tsp, extrayendo la información necesaria para construir la matriz de distancias a partir de las coordenadas de las ciudades.

  - **time:** Se utiliza para medir el tiempo de ejecución del algoritmo, lo que ayuda a evaluar el desempeño en términos de eficiencia.

### Se crea la clase TSP
En la clase TSP se agrupan todos los métodos necesarios para resolver el problema utilizando el algoritmo de Colonias de Hormigas. Entre los métodos implementados se encuentran

  - **Cargar Parámetros Iniciales:**

    El método **load_initial_variables** se encarga de recibir y asignar los parámetros iniciales necesarios para ejecutar el algoritmo. Este método recibe los siguientes parámetros:

    - **file_path (str):** La ruta del archivo .tsp que contiene la instancia del problema.

    - **n_ants (int):** La cantidad de hormigas que se utilizarán. Este valor define el tamaño del espacio de soluciones explorado en cada iteración.

    - **n_iters (int):** El número de iteraciones que realizará el algoritmo, lo que impacta directamente en la calidad de la solución y en el tiempo de ejecución.

    - **alpha (float):** Parámetro que controla la influencia de las feromonas en la decisión de la hormiga para elegir la siguiente ciudad.

    - **beta (float):** Parámetro que determina la importancia de la distancia a la hora de seleccionar el siguiente nodo.

    - **ro (float):** Tasa de evaporación de feromonas, la cual es crucial para evitar que el algoritmo se estanque en soluciones subóptimas.

  - **Carga de la Instancia y Cálculo de Distancias:**

    El método **load_tsp_instance** emplea la librería **tsplib95** para cargar la instancia del **TSP** desde el archivo y extraer las coordenadas de las ciudades. Posteriormente, el método **calculate_distances** se encarga de construir una matriz de distancias entre todas las ciudades utilizando los pesos definidos en el archivo.

  - **Construcción y Evaluación de Soluciones:**
  
    El método **solve** representa el corazón del algoritmo ACO para resolver el problema del Agente Viajero (TSP). Aquí se simula el comportamiento de un conjunto de hormigas virtuales que exploran rutas entre ciudades, guiadas por la información de feromonas y la distancia entre nodos.

    Este método sigue la lógica de construir soluciones mediante decisiones probabilísticas y actualizar la información de feromonas para reforzar las mejores rutas encontradas. A continuación se describe su funcionamiento paso a paso:

    - **Preparación e inicialización:**
      <pre>n = len(self.cities)
      d = self.distances
      tho = np.ones([n, n])
      delta = self.ro
      best_path = []
      best_p_length = np.inf </pre>
      
      - **n:** número de ciudades.

      - **d:** matriz de distancias entre ciudades.

      - **tho:** matriz de feromonas, inicializada con 1s.

      - **delta:** factor de refuerzo para actualizar feromonas.

      - **best_path y best_p_length:** variables para guardar la mejor solución encontrada.

    - **Bucle principal de iteraciones:**
      <pre> for iter in range(maxIter): </pre>

      Se ejecutan **maxIter** iteraciones. En cada una, varias hormigas generarán soluciones y se actualizarán las feromonas.

    - **Simulación del movimiento de cada hormiga:**
      <pre> for ant in range(n_ants): </pre>

      Para cada hormiga:

        Se elige una ciudad inicial aleatoriamente.

        Se construye una ruta eligiendo ciudades no visitadas basándose en la probabilidad de transición pij, que considera:

        La cantidad de feromonas en el camino (entre más alta, más atractiva).

        La inversa de la distancia entre ciudades (entre más corta, más atractiva).

      <pre> pij[j] = tho[current_city, unvisited_city]**self.alpha * (1/d[current_city, unvisited_city])**self.beta
          pij /= np.sum(pij)
          next_city = np.random.choice(unvisited, p=pij)</pre>

      alpha y beta controlan la influencia relativa de la feromona y la distancia, respectivamente.

      Se acumula la distancia (**path_length**) y se marca la ciudad como visitada.

    - **Cierre del ciclo:**
      Una vez la hormiga ha recorrido todas las ciudades:

      <pre>path_length += d[current_city, path[0]]
        path.append(path[0])</pre>


      Se regresa a la ciudad de origen para completar el ciclo.

      Se guarda la ruta y su longitud.

      Si la nueva ruta es mejor que la mejor conocida, se actualiza **best_path** y **best_p_length**.

    - **Actualización de feromonas:**

      Después de que todas las hormigas han completado su ruta:

      <pre> tho *= (1 - self.ro) </pre>

      **Evaporación**: Se reduce la cantidad de feromonas en todos los caminos, simulando el tiempo.

      <pre> for path, path_length in zip(paths, path_lengths):
          for i in range(n - 1):
              tho[path[i], path[i + 1]] += delta / path_length
          tho[path[-1], path[0]] += delta / path_length </pre>

      **Refuerzo**: Se agrega feromona adicional a los caminos usados, con mayor cantidad en rutas más cortas (mejores).

    - **Resultados:**

      <pre>self.best_path = best_path
      self.best_p_lenght = float(best_p_length)
      fin = time.time()
      total_time = fin - inicio </pre>

      Se guarda la mejor solución encontrada y se calcula el tiempo total de ejecución del algoritmo.

      <pre>return self.best_path, self.best_p_lenght, total_time</pre>

      Finalmente, el método retorna:

      La mejor ruta (**best_path**).

      La distancia total de esa ruta (**best_p_length**).

      El tiempo de ejecución (**total_time**).

  - **Visualización:**

    Para facilitar la interpretación de la solución, se implementa el método **graph_soluction**, que utiliza matplotlib para mostrar gráficamente el recorrido óptimo, dibujando el recorrido entre cada una de las ciudades.

Esta estructura modular en la clase TSP permite no solo organizar mejor el código, sino también facilita la realización de pruebas cambiando parámetros y evaluando el desempeño del algoritmo en distintas instancias del problema.


## Pruebas

### Instancias Pequeñas:

#### Tablas

- **Burma14:** 
  
  **Optimal path length 3323**
  
    Config|Hormigas|Iteraciones|Alpha |Beta | Ro  |Time(s)| Path        |Path Length | Gap (%)
    :----:|:------:|:---------:|:----:|:---:|:---:|:-----:|:-----------:|:----------:|:---:
    1     |10      | 1000      |0.5   |0.5  |0.1  |31.21  | [2, 13, 3, 4, 5, 11, 6, 12, 9, 8, 10, 0, 7, 1, 2]     | 3516   | 5.81
    2     |20      | 1000      |0.5   |0.5  |0.1  |58.18  | [3, 4, 11, 5, 6, 13, 12, 8, 10, 9, 0, 7, 1, 2, 3]     | 3644   | 9.66
    3     |5       | 1000      |0.5   |0.5  |0.1  |14.42  | [3, 4, 5, 11, 6, 1, 7, 0, 9, 8, 10, 12, 13, 2, 3]     | 3600   | 8.33
    4     |10      | 500       |0.5   |0.5  |0.1  |15.24  | [5, 11, 6, 7, 0, 10, 8, 9, 1, 12, 13, 2, 3, 4, 5]     | 3651   | 9.87
    5     |10      | 1000      |1.0   |0.5  |0.1  |49.77  | [7, 9, 8, 10, 12, 6, 11, 5, 4, 3, 2, 13, 1, 0, 7]     | 3336   | 0.39
    6     |10      | 1000      |0.5   |1.5  |0.1  |32.22  | [5, 11, 6, 12, 10, 8, 9, 7, 0, 1, 13, 2, 3, 4, 5]     | 3336   | 0.39
    7     |10      | 1000      |0.5   |0.5  |0.3  |31.33  | [10, 8, 7, 0, 1, 2, 13, 3, 4, 11, 5, 6, 12, 9, 10]    | 3534   | 6.35
    8     |50      | 2000      |1.0   |1.0  |0.5  |330.87 | [3, 4, 5, 11, 6, 12, 7, 10, 8, 9, 0, 1, 13, 2, 3]     | 3323   | 0
    9     |50      | 1000      |0.6   |1.0  |0.5  |182.14 | [12, 6, 11, 5, 4, 3, 2, 13, 1, 0, 9, 8, 10, 7, 12]    | 3323   | 0
    10    |20      | 1000      |0.6   |0.8  |0.6  |57.47  | [12, 6, 5, 11, 4, 3, 2, 13, 1, 0, 7, 9, 8, 10, 12]    | 3359   | 1.08

- **Ulysses16:**

  **Optimal path length 6859**

    Config|Hormigas|Iteraciones|Alpha |Beta  | Ro  |Time(s)| Path        |Path Length | Gap (%)
    :----:|:------:|:---------:|:----:|:---:|:---:|:------:|:-----------:|:----------:|:---:
    1     |20      | 2000      |1.0   |1.0  |0.2  |149.79  | [0, 7, 3, 1, 2, 15, 9, 8, 10, 4, 14, 5, 6, 11, 12, 13, 0]  |6859  |0
    2     |20      | 1000      |1.0   |1.0  |0.2  |63.87   | [9, 8, 10, 4, 14, 5, 6, 11, 12, 13, 0, 7, 3, 1, 2, 15, 9]  |6859  |0 
    3     |10      | 1000      |1.0   |1.0  |0.2  |30.72   | [11, 13, 12, 0, 7, 3, 1, 2, 15, 9, 8, 10, 4, 14, 5, 6, 11] |6865  |0.09 
    4     |10      | 1000      |0.6   |1.0  |0.2  |31.28   | [14, 5, 6, 11, 13, 12, 15, 0, 7, 3, 1, 2, 9, 8, 10, 4, 14] |6909  |0.73 
    5     |10      | 1000      |1.0   |0.6  |0.2  |33.16   | [0, 7, 3, 1, 2, 15, 11, 6, 5, 9, 8, 10, 4, 14, 13, 12, 0]  |6875  |0.23 
    6     |10      | 1000      |1.0   |0.6  |0.5  |31.04   | [0, 7, 3, 1, 2, 15, 11, 6, 5, 9, 8, 10, 4, 14, 13, 12, 0]  |6875  |0.23
    7     |20      | 1000      |0.6   |0.6  |0.1  |67.02   | [8, 9, 15, 0, 7, 3, 1, 2, 6, 5, 12, 11, 13, 14, 4, 10, 8]  |7209  |5.10 
    8     |20      | 1000      |0.6   |1.0  |0.1  |65.00   | [4, 14, 5, 6, 11, 13, 12, 0, 7, 3, 1, 2, 15, 9, 8, 10, 4]  |6865  |0.09 
    9     |20      | 1000      |0.6   |1.5  |0.1  |70.31   | [4, 14, 5, 6, 11, 13, 12, 15, 0, 7, 3, 1, 2, 9, 8, 10, 4]  |6909  |0.73 
    10    |20      | 500       |1.0   |1.0  |0.2  |32.34   | [2, 1, 3, 7, 0, 13, 12, 11, 6, 5, 14, 4, 10, 8, 9, 15, 2]  |6859  |0 
  
- **Ulysses22:**

  **Optimal path length 7013**

    Config|Hormigas|Iteraciones|Alpha |Beta  | Ro  |Time(s)| Path        |Path Length | Gap (%)
    :----:|:------:|:---------:|:----:|:---:|:---:|:------:|:-----------:|:---------:|:---:
    1     |20      | 2000      |1.0   |1.0  |0.2  |197.20  | [0, 7, 13, 12, 11, 6, 5, 14, 4, 10, 8, 9, 18, 20, 19, 15, 2, 1, 16, 3, 17, 21, 0]     |7063       |0.71
    2     |30      | 2000      |1.0   |1.0  |0.2  |284.98  | [3, 17, 21, 16, 1, 2, 20, 19, 18, 9, 8, 10, 4, 14, 5, 6, 11, 12, 13, 15, 0, 7, 3]   |7112       |1.41
    3     |20      | 2000      |0.6   |1.5  |0.4  |202.44  | [8, 9, 18, 20, 19, 2, 1, 16, 21, 17, 3, 7, 0, 15, 13, 12, 11, 6, 5, 14, 4, 10, 8]      |7129       |1.65
    4     |50      | 1000      |1.0   |1.5  |0.4  |233.67  | [3, 17, 21, 16, 1, 2, 15, 20, 19, 18, 9, 8, 10, 4, 14, 5, 6, 11, 12, 13, 7, 0, 3]   |7077       |0.91
    5     |50      | 1000      |1.0   |1.0  |0.2  |255.31  | [5, 6, 11, 12, 13, 15, 0, 7, 3, 17, 21, 16, 1, 2, 20, 19, 18, 9, 8, 10, 4, 14, 5]      |7112       |1.41
    6     |50      | 1000      |0.6   |1.0  |0.2  |232.61  | [14, 5, 6, 12, 13, 11, 2, 1, 16, 21, 3, 17, 7, 0, 15, 20, 19, 18, 9, 8, 10, 4, 14]     |7174       |2.29
    7     |50      | 2000      |0.6   |1.5  |0.2  |475.70  | [14, 5, 6, 13, 12, 11, 0, 7, 17, 3, 21, 16, 1, 2, 15, 20, 19, 18, 9, 8, 10, 4, 14]     |7043       |0.42
    8     |60      | 1000      |0.6   |1.5  |0.2  |318.33  | [5, 6, 11, 12, 13, 0, 7, 17, 3, 21, 16, 1, 2, 15, 19, 20, 18, 9, 8, 10, 4, 14, 5]      |7029       |0.23
    9     |60      | 1000      |1.0   |1.5 |0.3  |289.71   | [0, 7, 17, 3, 21, 16, 1, 2, 15, 11, 12, 13, 5, 6, 20, 19, 18, 9, 8, 10, 4, 14, 0]      |7097       |1.20
    10    |60      |1000       |1.5   |0.6  |0.3 |369.69   | [13, 12, 11, 15, 0, 7, 21, 17, 3, 16, 1, 2, 20, 19, 18, 9, 8, 10, 4, 14, 5, 6, 13]  |7113       |1.43

#### Gráficas
- **Burma14:** Mejor ruta encontrada en el problema Burma14
  
    ![Burma14](Graficas\Burma14-9.png)

- **Ulysses16:** Mejor ruta encontrada en el problema Ulysses16

    ![Ulysses16](Graficas\ulysses16-10.png)

- **Ulysses22:** Mejor ruta encontrada en el problema Ulysses22

    ![Ulysses22](Graficas\Ulysses22-8.png)

#### Concluciones

  - **Burma14:**

      Al observar la tabla correspondiente a las instancias del TSP "Burma14", se evidencia que la mejor solución se obtuvo en la configuración número 9. A continuación, se detallan las variables iniciales utilizadas en dicha configuración:

      *Número de hormigas: 50*

      *Número de iteraciones: 1000*

      *Alpha: 0.6*

      *Beta: 1.0*

      *Ro: 0.5*

      Con esta combinación de parámetros se encontró el camino óptimo con una longitud de 3323, que coincide con la mejor solución conocida para el problema. La ruta óptima identificada fue:

      [12, 6, 11, 5, 4, 3, 2, 13, 1, 0, 9, 8, 10, 7, 12]

      Este resultado se observa también en la gráfica correspondiente de Burma14. El tiempo registrado para encontrar esta solución fue de 182.14 segundos y se alcanzó un Gap de 0%, lo que confirma la efectividad y precisión de la configuración.

      Cabe destacar que la configuración número 8 de la tabla también logró alcanzar la solución óptima de 3323.
  
  - **Ulysses16:** 

      En la tabla correspondiente a la instancia Ulysses16, se pueden observar tres configuraciones diferentes que permitieron alcanzar la solución óptima del problema (6859). Estas configuraciones son la 1, 2 y 10; sin embargo, la que logró encontrar dicha solución en el menor tiempo (32.34 segundos) fue la configuración 10. A continuación, se detallan los valores de los parámetros utilizados en dicha configuración:

      *Número de hormigas: 20*

      *Número de iteraciones: 500*

      *Alpha: 1.0*

      *Beta: 1.0*

      *Ro: 0.2*

      Con esta combinación de parámetros, se encontró el recorrido óptimo con una longitud de 6859, el cual coincide con la mejor solución conocida para el problema. La ruta óptima identificada fue:

      [2, 1, 3, 7, 0, 13, 12, 11, 6, 5, 14, 4, 10, 8, 9, 15, 2]

      Este resultado también se refleja en la gráfica correspondiente a Ulysses16. El tiempo registrado para encontrar esta solución fue de 32.34 segundos, alcanzando un gap del 0%, lo que confirma la efectividad y precisión de esta configuración.

  - **Ulysses22:**

      Para la instancia Ulysses22, ninguna de las 10 configuraciones presentadas en la tabla correspondiente logró alcanzar la solución óptima del problema, la cual es 7013. Durante la prueba, se intentó variar los valores de las variables con el objetivo de acercarse a dicha solución, siendo la configuración 8 la que obtuvo el mejor resultado.

      A continuación, se detallan los valores de los parámetros utilizados en esta configuración:

      *Número de hormigas: 60*

      *Número de iteraciones: 1000*

      *Alpha: 0.6*

      *Beta: 1.5*

      *Ro: 0.2*

      Con esta combinación de parámetros, se encontró el recorrido más cercano a la solución óptima, con una longitud de 7029, lo que representa un gap de 0.23%, un valor bastante aceptable considerando que la mejor solución conocida es 7013. La ruta correspondiente a esta solución fue la siguiente:

      [5, 6, 11, 12, 13, 0, 7, 17, 3, 21, 16, 1, 2, 15, 19, 20, 18, 9, 8, 10, 4, 14, 5]

      Este resultado también se refleja en la gráfica correspondiente a Ulysses22. El tiempo registrado para encontrar esta solución fue de 318.33 segundos. Aunque no se logró alcanzar la solución óptima, se puede concluir que esta configuración permite obtener una solución muy cercana, demostrando un buen desempeño del algoritmo.

### Instancias Medianas:

#### Tablas

- **Berlin52:** 
  
  **Optimal path length 7542**
  
    Config| Hormigas | Iteraciones | Alpha | Beta | Ro  | Time(s) |  Path     | Path Length | Gap (%)
    :----:|:--------:|:-----------:|:-----:|:----:|:---:|:-------:|:---------:|:-----------:|:---:
    1     |     70   |    1000     |  1.0  | 1.0  | 0.5 | 186.97  | [40, 7, 44, 18, 2, 16, 20, 41, 6, 1, 29, 28, 49, 19, 22, 30, 17, 21, 0, 48, 31, 43, 15, 45, 36, 39, 38, 35, 34, 33, 37, 47, 23, 4, 14, 5, 3, 24, 11, 27, 26, 25, 46, 12, 13, 51, 10, 50, 32, 42, 9, 8, 40]        |    7997     |6.03 
    2     |    70    |    1000     |  0.6  | 1.0  | 0.4 | 189.38  | [40, 7, 18, 44, 31, 48, 38, 35, 34, 33, 0, 21, 30, 17, 22, 19, 49, 28, 25, 27, 26, 46, 13, 51, 12, 10, 50, 11, 24, 3, 5, 47, 23, 14, 37, 36, 4, 39, 43, 15, 29, 2, 16, 1, 6, 41, 20, 45, 42, 32, 9, 8, 40]    |    9829     |30.32 
    3     |    70    |    1000     |  1.0  | 1.5  | 0.5 | 192.07  | [7, 40, 18, 44, 31, 48, 0, 21, 30, 17, 2, 16, 20, 41, 6, 1, 29, 28, 49, 19, 22, 15, 45, 43, 33, 34, 35, 38, 39, 37, 36, 47, 23, 4, 14, 5, 3, 24, 11, 27, 26, 25, 46, 12, 13, 51, 10, 50, 32, 42, 9, 8, 7]         |    7676     |1.78 
    4     |    70    |    2000     |  1.0  | 1.5  | 0.2 | 387.95  | [22, 19, 49, 15, 45, 43, 33, 34, 35, 38, 39, 37, 36, 47, 23, 4, 14, 5, 3, 24, 11, 27, 26, 25, 46, 12, 13, 51, 10, 50, 32, 42, 9, 8, 7, 40, 18, 44, 31, 48, 0, 21, 30, 17, 2, 16, 20, 41, 6, 1, 29, 28, 22]      |    7662     |1.59 
    5     |    70    |    2000     |  1.5  | 1.5  | 0.1 | 380.43  | [22, 19, 49, 28, 15, 45, 43, 33, 34, 35, 38, 39, 37, 36, 47, 23, 4, 14, 5, 3, 24, 11, 27, 26, 25, 46, 12, 13, 51, 10, 50, 32, 42, 9, 8, 7, 40, 18, 44, 31, 48, 0, 21, 30, 17, 2, 16, 20, 29, 41, 6, 1, 22]        |    7755     |2.82 
    6     |    80    |    2000     |  1.5  | 1.5  | 0.2 | 497.502 | [45, 43, 33, 34, 35, 38, 39, 37, 36, 47, 23, 4, 14, 5, 3, 24, 11, 27, 26, 25, 46, 12, 13, 51, 10, 50, 32, 42, 9, 8, 7, 40, 18, 44, 31, 48, 0, 21, 30, 17, 2, 16, 20, 41, 6, 1, 29, 22, 19, 49, 15, 28, 45]      |    7679     |1.81 
    7     |    80    |    2000     |  1.0  | 1.0  | 0.2 | 490.30  | [35, 34, 33, 43, 15, 45, 36, 37, 39, 38, 47, 23, 4, 14, 5, 3, 24, 11, 27, 26, 25, 46, 12, 13, 51, 10, 50, 32, 42, 9, 8, 7, 40, 18, 44, 2, 16, 20, 41, 6, 1, 29, 28, 49, 19, 22, 30, 17, 21, 0, 48, 31, 35]  |    7798     |3.39
    8 |    90    |    2000     |  1.0  | 1.5  | 0.2 |  361.75  | [45, 47, 23, 4, 14, 5, 3, 24, 11, 27, 26, 25, 46, 12, 13, 51, 10, 50, 32, 42, 9, 8, 7, 40, 18, 44, 31, 48, 0, 21, 30, 17, 2, 16, 20, 41, 6, 1, 29, 22, 19, 49, 28, 15, 43, 33, 34, 35, 38, 39, 37, 36, 45]  |7596  |0.72
    9 |    90    |    2000     |  1  | 1.5  | 0.2 |  456.68  |[15, 45, 43, 36, 39, 38, 35, 34, 33, 37, 23, 47, 4, 14, 5, 3, 24, 11, 27, 26, 25, 46, 12, 13, 51, 10, 50, 32, 42, 9, 8, 7, 40, 18, 44, 31, 48, 0, 21, 30, 17, 2, 16, 20, 41, 6, 1, 29, 22, 19, 49, 28, 15]   |7675  |1.76
    10 |   90    |    3000     |  1.0  | 1.5  | 0.2 |  535.15  | [40, 18, 44, 31, 48, 0, 21, 30, 17, 2, 16, 20, 41, 6, 1, 29, 28, 49, 19, 22, 15, 45, 43, 33, 34, 35, 38, 36, 39, 37, 47, 23, 4, 14, 5, 3, 24, 11, 27, 26, 25, 46, 12, 13, 51, 10, 50, 32, 42, 9, 8, 7, 40]  | 7676 |1.78

- **KroA100:** 
  
  **Optimal path length 21282**
  
    Config|Hormigas|Iteraciones|Alpha |Beta | Ro  |Time(s)| Path        |Path Length | Gap (%)
    :----:|:------:|:---------:|:----:|:---:|:---:|:-----:|:-----------:|:----------:|:---:
    1     |50      | 1000      |1.0   |1.0  |0.5  |141.78 | [45, 28, 33, 82, 54, 6, 8, 50, 86, 56, 19, 11, 26, 85, 34, 61, 59, 76, 22, 97, 90, 44, 31, 10, 16, 14, 58, 73, 20, 71, 9, 83, 35, 37, 23, 17, 78, 52, 87, 15, 21, 93, 69, 65, 64, 3, 25, 96, 55, 79, 30, 88, 41, 7, 91, 0, 62, 5, 48, 89, 18, 74, 98, 46, 92, 27, 66, 57, 60, 24, 80, 68, 63, 39, 53, 1, 43, 49, 72, 67, 84, 38, 29, 95, 77, 51, 4, 36, 32, 75, 12, 94, 81, 47, 99, 70, 40, 13, 2, 42, 45]  |23912    |12.36 
    2     |100      | 1000      |1   |1.5  |0.2  |282  |   [57, 76, 19, 56, 6, 8, 86, 50, 60, 24, 80, 68, 63, 39, 53, 1, 43, 49, 72, 67, 84, 38, 29, 95, 77, 51, 4, 36, 32, 75, 12, 94, 81, 47, 99, 70, 40, 13, 2, 42, 45, 28, 33, 82, 54, 11, 26, 85, 34, 61, 59, 22, 97, 90, 44, 31, 10, 14, 16, 58, 73, 20, 71, 9, 83, 35, 98, 37, 23, 17, 78, 52, 87, 15, 21, 93, 69, 65, 64, 3, 25, 18, 74, 96, 55, 79, 30, 88, 41, 7, 91, 0, 62, 5, 48, 89, 46, 92, 27, 66, 57]   |  22570.0  | 6.05
    3     |100      | 1000      |1   |1.5  |0.8  |280  |   [8, 6, 86, 50, 60, 24, 80, 68, 63, 39, 53, 1, 43, 49, 72, 67, 84, 38, 29, 95, 77, 51, 4, 36, 32, 75, 12, 94, 81, 47, 99, 70, 40, 13, 2, 42, 45, 28, 33, 82, 54, 11, 26, 85, 34, 19, 56, 61, 59, 76, 22, 97, 90, 44, 31, 10, 16, 14, 58, 73, 20, 71, 9, 83, 35, 98, 37, 23, 17, 78, 52, 87, 15, 21, 93, 69, 65, 64, 3, 25, 96, 74, 18, 89, 48, 5, 62, 0, 91, 7, 41, 88, 30, 79, 55, 46, 92, 27, 66, 57, 8]   |  23455  | 10.21
    4     |100      | 1000      |1   |1.5  |0.1  |281  |   [92, 27, 66, 57, 19, 56, 6, 8, 86, 50, 60, 24, 80, 68, 63, 39, 53, 1, 43, 49, 72, 67, 84, 38, 29, 95, 77, 51, 4, 36, 32, 75, 12, 94, 81, 47, 99, 70, 40, 13, 2, 42, 45, 28, 33, 82, 54, 11, 26, 85, 34, 61, 59, 76, 22, 97, 90, 44, 31, 10, 14, 16, 58, 73, 20, 71, 9, 83, 35, 98, 37, 23, 17, 78, 52, 87, 15, 21, 93, 69, 65, 64, 3, 25, 96, 74, 18, 89, 48, 5, 62, 46, 91, 7, 41, 88, 30, 79, 55, 0, 92]  |  23141.0  | 8.74
    5     |100      | 1000      |0.5   |1.5  |0.2  |279  |   [3, 64, 65, 15, 87, 21, 69, 93, 17, 78, 52, 18, 74, 55, 79, 30, 88, 41, 7, 89, 48, 5, 62, 0, 66, 27, 92, 57, 60, 54, 82, 33, 99, 70, 40, 45, 28, 13, 42, 2, 47, 29, 38, 81, 94, 12, 32, 75, 36, 4, 95, 51, 77, 11, 6, 8, 56, 34, 85, 26, 19, 76, 59, 61, 86, 50, 84, 67, 72, 49, 68, 80, 24, 63, 39, 53, 1, 43, 98, 23, 37, 35, 83, 9, 20, 58, 73, 16, 14, 10, 31, 44, 22, 97, 90, 46, 71, 91, 25, 96, 3]   |  32283  | 51.69
    6     |100      | 1000      |1.5   |1.5  |0.2  |279  |   [61, 76, 59, 22, 97, 90, 44, 31, 10, 14, 16, 73, 58, 20, 71, 9, 83, 35, 98, 37, 23, 17, 78, 52, 87, 15, 21, 93, 69, 65, 64, 3, 25, 96, 74, 18, 89, 48, 5, 62, 0, 91, 7, 41, 88, 30, 79, 55, 46, 92, 27, 66, 57, 60, 24, 80, 68, 63, 39, 53, 1, 43, 49, 72, 67, 84, 38, 29, 95, 77, 51, 4, 36, 12, 75, 32, 94, 81, 47, 99, 70, 40, 13, 2, 42, 45, 28, 33, 82, 54, 11, 26, 85, 34, 6, 8, 86, 50, 56, 19, 61]   |  23394  | 9.92
    7     |120      | 2000      |1   |1.5  |0.2  |678  |   [57, 60, 24, 80, 68, 63, 39, 53, 1, 43, 49, 72, 67, 84, 38, 29, 95, 77, 51, 4, 36, 32, 75, 12, 94, 81, 47, 99, 70, 40, 13, 2, 42, 45, 28, 33, 82, 54, 11, 26, 85, 34, 19, 56, 6, 8, 86, 50, 76, 59, 61, 22, 97, 90, 44, 31, 10, 14, 16, 58, 73, 20, 71, 9, 83, 35, 98, 37, 23, 17, 78, 52, 87, 15, 21, 93, 69, 65, 64, 3, 25, 18, 74, 96, 55, 79, 30, 88, 41, 7, 91, 0, 62, 5, 48, 89, 46, 92, 27, 66, 57]   |  22503  | 5.74
    8     |200      | 2000      |1   |1.5  |0.2  |4951 |   [98, 37, 23, 17, 78, 52, 87, 15, 21, 93, 69, 65, 64, 3, 25, 18, 89, 48, 5, 62, 0, 91, 7, 41, 88, 30, 79, 55, 96, 74, 46, 92, 27, 66, 57, 60, 24, 80, 68, 63, 39, 53, 1, 43, 49, 72, 67, 84, 38, 29, 95, 77, 51, 4, 36, 32, 75, 12, 94, 81, 47, 99, 70, 40, 13, 2, 42, 45, 28, 33, 82, 54, 11, 26, 85, 34, 19, 56, 8, 6, 86, 50, 76, 61, 59, 22, 97, 90, 44, 31, 10, 14, 16, 58, 73, 20, 71, 9, 83, 35, 98]   |  22772  | 7.00
    9     |120      | 2000      |1   |2  |0.2  |9262  |   [76, 61, 59, 22, 97, 90, 44, 31, 10, 14, 16, 58, 73, 20, 71, 9, 83, 35, 98, 37, 23, 17, 78, 52, 87, 15, 21, 93, 69, 65, 64, 3, 25, 18, 74, 96, 55, 79, 30, 88, 41, 7, 91, 0, 62, 5, 48, 89, 46, 92, 27, 66, 57, 60, 24, 80, 68, 63, 39, 53, 1, 43, 49, 72, 67, 84, 38, 29, 95, 77, 51, 4, 36, 32, 75, 12, 94, 81, 47, 99, 70, 40, 13, 2, 42, 45, 28, 33, 82, 54, 11, 26, 85, 34, 19, 56, 8, 6, 86, 50, 76]   |  22435.0  | 5.42
    10    |10      | 2000      |1   |2  |0.2  |58  |   [27, 92, 66, 57, 60, 24, 80, 68, 63, 39, 53, 1, 43, 49, 72, 67, 84, 29, 38, 95, 77, 51, 4, 36, 32, 12, 75, 94, 81, 47, 99, 70, 40, 13, 2, 45, 42, 28, 33, 82, 54, 11, 26, 34, 85, 19, 56, 8, 6, 86, 50, 59, 76, 61, 22, 97, 90, 44, 31, 10, 14, 16, 58, 73, 20, 71, 9, 83, 35, 98, 37, 23, 17, 78, 52, 87, 15, 21, 93, 69, 65, 64, 3, 25, 18, 89, 48, 5, 62, 0, 91, 7, 41, 88, 30, 79, 55, 96, 74, 46, 27]   |  23449.0  | 10.18


#### Gráficas
- **Berlin52:** Mejor ruta encontrada en el problema Berlin52
  
    ![Berlin52](Graficas\Berlin52-8.png)

- **kroA100:** Mejor ruta encontrada en el problema kroA100
  
    ![kroA100](Graficas\kroA100.png)

#### Concluciones

  - **Berlin52:**

    En la tabla para las instancias TSP de "Berlin52", utilizando los 10 diferentes parámetros evaluados para este problema, ninguna configuración alcanzó la solución óptima; sin embargo, se pudieron encontrar soluciones locales muy cercanas a la óptima. En particular, se profundizará en la configuración número 8, que presentó la solución más próxima al óptimo. A continuación, se detallan los valores de los parámetros utilizados en esta configuración:

    *Número de hormigas: 90*

    *Número de iteraciones: 2000*

    *Alpha: 1.0*

    *Beta: 1.5*

    *Ro: 0.2*

    Con esta configuración se alcanzó un gap del 0.72%, obteniéndose una solución con una longitud de 7596, en comparación con la solución óptima de 7542. Esta solución se halló en un tiempo de 361.75 segundos.

    La ruta encontrada para esta configuración, con el mejor gap hallado, es la siguiente:
    [45, 47, 23, 4, 14, 5, 3, 24, 11, 27, 26, 25, 46, 12, 13, 51, 10, 50, 32, 42, 9, 8, 7, 40, 18, 44, 31, 48, 0, 21, 30, 17, 2, 16, 20, 41, 6, 1, 29, 22, 19, 49, 28, 15, 43, 33, 34, 35, 38, 39, 37, 36, 45]

    A pesar de que ninguna de las diferentes configuraciones logró alcanzar la solución óptima, el algoritmo demuestra ser robusto y capaz de encontrar soluciones muy cercanas a la óptima. Con una mayor exploración y variación de los parámetros, es posible que se logre obtener la solución óptima.

  - **KroA100:**

    En la tabla para las instancias TSP de "kroA100", con las 10 configuraciones de parámetros probadas, ninguna alcanzó la solución óptima (longitud óptima: 21282). Sin embargo, se observaron resultados bastante aceptables, acercándose a soluciones de buena calidad. Se profundizará en la configuración número 2, que fue la más cercana al óptimo. A continuación, se detallan los valores de los parámetros utilizados en esta configuración:

    **Número de hormigas: 100**

    **Número de iteraciones: 1000**

    **Alpha: 1.0**

    **Beta: 1.5**

    **Ro: 0.2**

    Con esta configuración se logró obtener una ruta con una longitud de 22570, lo que representa un gap del 6.05% respecto al óptimo. Esta solución fue hallada en un tiempo de 282 segundos, un resultado eficiente considerando el tamaño y complejidad del problema.

    La ruta obtenida para esta configuración, con el menor gap registrado, es la siguiente:
    [57, 76, 19, 56, 6, 8, 86, 50, 60, 24, 80, 68, 63, 39, 53, 1, 43, 49, 72, 67, 84, 38, 29, 95, 77, 51, 4, 36, 32, 75, 12, 94, 81, 47, 99, 70, 40, 13, 2, 42, 45, 28, 33, 82, 54, 11, 26, 85, 34, 61, 59, 22, 97, 90, 44, 31, 10, 14, 16, 58, 73, 20, 71, 9, 83, 35, 98, 37, 23, 17, 78, 52, 87, 15, 21, 93, 69, 65, 64, 3, 25, 18, 74, 96, 55, 79, 30, 88, 41, 7, 91, 0, 62, 5, 48, 89, 46, 92, 27, 66, 57]

    Aunque no se logró alcanzar la solución óptima, los resultados obtenidos muestran que el algoritmo tiene un buen desempeño. Ajustando adecuadamente los parámetros, es posible reducir significativamente el gap. Esto demuestra que el algoritmo es capaz de ofrecer soluciones competitivas y eficientes para problemas más complejos como kroA100.


### Instancias Grandes:

#### Tablas

- **lin105:** 
  
  **Optimal path length 14379**
  
    Config|Hormigas|Iteraciones|Alpha |Beta | Ro  |Time(s)| Path        |Path Length | Gap (%)
    :----:|:------:|:---------:|:----:|:---:|:---:|:-----:|:-----------:|:----------:|:---:
    1     |120      | 2000      |1.0   |1.5  |0.25  |3009 | [82, 81, 77, 70, 67, 66, 63, 72, 75, 79, 80, 74, 73, 68, 69, 62, 61, 104, 58, 55, 54, 49, 44, 47, 48, 39, 103, 41, 40, 42, 45, 51, 52, 57, 56, 53, 50, 46, 43, 36, 35, 32, 27, 22, 19, 102, 20, 21, 28, 29, 30, 31, 14, 10, 9, 6, 5, 1, 0, 2, 11, 18, 23, 26, 25, 24, 17, 15, 16, 8, 7, 4, 3, 12, 13, 33, 34, 37, 38, 59, 60, 64, 65, 86, 87, 93, 94, 99, 98, 97, 92, 90, 91, 95, 96, 100, 101, 88, 89, 85, 78, 76, 71, 83, 84, 82]  |15379    |6.95 
    2     |120      | 1000      |1   |1.5  |0.5  |364  |  [69, 62, 61, 104, 58, 55, 54, 49, 47, 44, 39, 48, 103, 43, 46, 50, 53, 56, 57, 52, 51, 45, 42, 40, 41, 36, 35, 32, 27, 22, 19, 102, 20, 21, 28, 29, 30, 31, 14, 10, 9, 6, 5, 1, 0, 2, 11, 18, 23, 26, 25, 24, 17, 15, 16, 8, 7, 4, 3, 12, 13, 33, 34, 37, 38, 59, 60, 64, 65, 86, 87, 93, 94, 99, 98, 97, 88, 89, 80, 74, 73, 68, 63, 66, 67, 70, 77, 81, 82, 83, 84, 90, 91, 95, 96, 100, 101, 92, 85, 78, 76, 71, 72, 75, 79, 69]    |  15142  | 5.31
    3     |120      | 1000      |0.5   |1.5  |0.5  |518  |   [52, 51, 56, 53, 50, 46, 43, 48, 54, 49, 58, 66, 67, 70, 77, 81, 82, 83, 84, 85, 76, 78, 71, 79, 75, 72, 80, 74, 73, 68, 69, 62, 61, 104, 44, 55, 47, 39, 103, 31, 32, 22, 27, 19, 102, 21, 20, 28, 30, 29, 11, 23, 26, 8, 7, 2, 0, 1, 5, 6, 10, 9, 14, 15, 17, 18, 24, 25, 16, 35, 36, 33, 4, 3, 12, 13, 34, 38, 37, 59, 60, 64, 65, 87, 86, 94, 93, 99, 98, 97, 92, 91, 90, 95, 96, 101, 100, 89, 88, 63, 57, 45, 42, 40, 41, 52]   |  19565.0  | 36.07
    4     |120      | 1000      |1   |0.5  |0.5  |562  |   [23, 18, 24, 25, 17, 11, 20, 21, 28, 29, 30, 31, 39, 44, 47, 49, 54, 55, 58, 104, 61, 62, 60, 59, 64, 65, 86, 87, 93, 94, 99, 98, 97, 92, 90, 91, 95, 96, 100, 101, 84, 82, 81, 77, 70, 67, 66, 71, 76, 78, 83, 85, 88, 89, 80, 69, 73, 74, 68, 72, 79, 75, 63, 48, 41, 42, 45, 51, 52, 57, 56, 53, 50, 46, 43, 40, 35, 103, 32, 27, 22, 19, 102, 14, 10, 9, 6, 5, 1, 0, 2, 7, 8, 16, 15, 13, 4, 3, 12, 33, 34, 38, 37, 36, 26, 23]   |  17481  | 21.57
    5     |120      | 1000      |1.5   |1  |0.5  |379  |   [102, 20, 21, 28, 29, 30, 31, 32, 27, 22, 19, 11, 18, 23, 26, 25, 16, 15, 17, 24, 35, 36, 41, 42, 45, 51, 52, 57, 56, 53, 50, 46, 43, 40, 103, 39, 48, 47, 44, 49, 54, 55, 58, 104, 63, 71, 76, 78, 83, 82, 81, 77, 70, 67, 66, 84, 90, 91, 95, 96, 100, 101, 92, 97, 98, 89, 88, 85, 75, 72, 68, 69, 73, 74, 80, 79, 61, 62, 65, 64, 87, 86, 93, 94, 99, 60, 59, 38, 37, 34, 33, 13, 12, 4, 3, 7, 8, 2, 1, 0, 5, 6, 10, 9, 14, 102]   |  16455.0  | 14.44
    6     |120      | 1000      |1   |1.5  |0.5  | 1485  |  [63, 71, 76, 78, 83, 85, 79, 75, 72, 68, 73, 74, 80, 69, 62, 61, 104, 58, 55, 54, 49, 47, 44, 39, 48, 103, 43, 46, 50, 53, 56, 57, 52, 51, 45, 42, 40, 41, 36, 35, 32, 27, 22, 19, 102, 20, 21, 28, 29, 30, 31, 14, 10, 9, 6, 5, 1, 0, 2, 11, 18, 23, 26, 25, 24, 17, 15, 16, 8, 7, 4, 3, 12, 13, 33, 34, 37, 38, 59, 60, 64, 65, 86, 87, 93, 94, 99, 98, 97, 89, 88, 92, 91, 90, 95, 96, 100, 101, 84, 82, 81, 77, 70, 67, 66, 63]    | 15073   | 4.83
    7     |200      | 1000      |1   |1.5  |0.5  |2293  |   [57, 52, 51, 45, 42, 40, 41, 36, 35, 32, 27, 22, 19, 102, 20, 21, 28, 29, 30, 31, 14, 10, 9, 6, 5, 1, 0, 2, 11, 18, 23, 26, 25, 24, 17, 15, 16, 8, 7, 4, 3, 12, 13, 33, 34, 37, 38, 59, 60, 64, 65, 86, 87, 93, 94, 99, 98, 97, 92, 91, 90, 95, 96, 100, 101, 84, 82, 81, 77, 70, 67, 66, 63, 71, 76, 78, 83, 85, 88, 89, 80, 74, 73, 68, 72, 75, 79, 69, 62, 61, 104, 55, 58, 54, 49, 48, 47, 44, 39, 103, 43, 46, 50, 53, 56, 57]   |  15327  | 6.59
    8     |80      | 1000      |1   |1  |0.5  | 243  |   [85, 79, 75, 72, 68, 73, 74, 80, 69, 62, 61, 104, 58, 55, 54, 49, 47, 44, 39, 48, 103, 43, 46, 50, 53, 56, 57, 52, 51, 45, 42, 40, 41, 36, 35, 32, 27, 22, 19, 102, 20, 21, 28, 29, 30, 31, 14, 10, 9, 6, 5, 1, 0, 2, 11, 18, 23, 26, 25, 24, 17, 15, 16, 8, 7, 13, 12, 4, 3, 38, 37, 34, 33, 59, 60, 64, 65, 86, 87, 93, 94, 99, 98, 97, 89, 88, 92, 90, 91, 95, 96, 100, 101, 84, 82, 81, 77, 70, 67, 66, 63, 71, 76, 78, 83, 85]   |  16072.0  | 11.77
    9     |120      | 1000      |1   |1  |0.5  |370  |   [69, 62, 61, 104, 58, 48, 39, 103, 44, 47, 49, 54, 55, 56, 53, 50, 46, 43, 40, 42, 45, 51, 52, 57, 41, 36, 35, 32, 27, 22, 19, 102, 20, 21, 28, 29, 30, 31, 14, 10, 9, 6, 5, 1, 0, 2, 11, 18, 23, 26, 25, 24, 17, 15, 16, 8, 7, 13, 12, 4, 3, 34, 33, 38, 37, 59, 60, 64, 65, 86, 87, 93, 94, 99, 98, 97, 92, 90, 91, 95, 96, 100, 101, 84, 82, 81, 77, 70, 67, 66, 63, 71, 76, 78, 83, 85, 88, 89, 80, 74, 73, 68, 72, 75, 79, 69]   |  16009.0  | 11.34
    10    |120      | 1000      |1   |1.5  |0.5  |359  |   [100, 101, 92, 85, 78, 76, 71, 72, 75, 79, 80, 74, 73, 68, 69, 62, 61, 104, 58, 55, 54, 49, 47, 44, 39, 48, 103, 43, 46, 50, 53, 56, 57, 52, 51, 45, 42, 40, 41, 36, 35, 32, 27, 22, 19, 102, 20, 21, 28, 29, 30, 31, 14, 10, 9, 6, 5, 1, 0, 2, 11, 18, 23, 26, 25, 24, 17, 15, 16, 8, 7, 4, 3, 12, 13, 33, 34, 37, 38, 59, 60, 64, 65, 86, 87, 93, 94, 99, 98, 97, 88, 89, 63, 66, 67, 70, 77, 81, 82, 83, 84, 90, 91, 95, 96, 100]   |  15203.0  | 5.73

#### Gráficas
- **lin105:** Mejor ruta encontrada en el problema lin105
  
    ![lin105](Graficas\lin105best.png)



#### Concluciones

  - **Lin105:**
      