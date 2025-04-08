

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
  - [Resultados](#resultados)
    - [Instancias Pequeñas:](#instancias-pequeñas)
      - [Tablas](#tablas)
      - [Gráficas](#gráficas)
      - [Concluciones](#concluciones)
    - [Instancias Medianas:](#instancias-medianas)
      - [Tablas](#tablas-1)

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

  - **Visualización:**

    Para facilitar la interpretación de la solución, se implementa el método graph_soluction, que utiliza matplotlib para mostrar gráficamente el recorrido óptimo, dibujando flechas entre las ciudades según el orden de visita.

Esta estructura modular en la clase TSP permite no solo organizar mejor el código, sino también facilita la realización de pruebas cambiando parámetros y evaluando el desempeño del algoritmo en distintas instancias del problema.


## Resultados

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
    8     |    80    |    2000     |  1.0  | 1.5  | 0.2 |  520.68  | [43, 33, 34, 35, 38, 39, 37, 36, 47, 23, 4, 14, 5, 3, 24, 11, 27, 26, 25, 46, 12, 13, 51, 10, 50, 32, 42, 9, 8, 7, 40, 18, 44, 31, 48, 0, 21, 30, 17, 2, 16, 20, 41, 6, 1, 29, 28, 49, 19, 22, 15, 45, 43]  |    7676     |1.78
    9 |    20    |    1000     |  0.5  | 0.5  | 0.1 |  58.18  |   |  |
    10|    20    |    1000     |  0.5  | 0.5  | 0.1 |  58. 18 |   |  |
- **KroA100:** 
  
  **Optimal path length 21282**
  
    Config|Hormigas|Iteraciones|Alpha |Beta | Ro  |Time(s)| Path        |Path Length | Gap (%)
    :----:|:------:|:---------:|:----:|:---:|:---:|:-----:|:-----------:|:----------:|:---:
    1     |50      | 1000      |1.0   |1.0  |0.5  |3451.78 | [45, 28, 33, 82, 54, 6, 8, 50, 86, 56, 19, 11, 26, 85, 34, 61, 59, 76, 22, 97, 90, 44, 31, 10, 16, 14, 58, 73, 20, 71, 9, 83, 35, 37, 23, 17, 78, 52, 87, 15, 21, 93, 69, 65, 64, 3, 25, 96, 55, 79, 30, 88, 41, 7, 91, 0, 62, 5, 48, 89, 18, 74, 98, 46, 92, 27, 66, 57, 60, 24, 80, 68, 63, 39, 53, 1, 43, 49, 72, 67, 84, 38, 29, 95, 77, 51, 4, 36, 32, 75, 12, 94, 81, 47, 99, 70, 40, 13, 2, 42, 45]  |23912    |12.36 
    2     |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
    3     |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
    4     |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
    5     |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
    6     |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
    7     |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
    8     |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
    9     |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
    10    |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
