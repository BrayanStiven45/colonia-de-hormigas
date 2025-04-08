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

    ![Ulysses22](Graficas\qwkdjkjjiwjsijsiusiquUlysses22-8.png)

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
  
    Config|Hormigas|Iteraciones|Alpha |Beta | Ro  |Time(s)| Path        |Path Length | Gap (%)
    :----:|:------:|:---------:|:----:|:---:|:---:|:-----:|:-----------:|:----------:|:---:
    1     |60      | 1000      |1.0   |1.0  |0.5  |885.91  | [2, 16, 20, 41, 6, 1, 29, 28, 49, 19, 22, 30, 17, 21, 0, 48, 31, 35, 34, 33, 43, 15, 45, 36, 38, 39, 37, 47, 23, 4, 14, 5, 3, 24, 11, 27, 26, 25 4, 14, 5, 3, 24, 11, 27, 26, 25, 46, 13, 12, 51, 10, 50, 32, 42, 9, 8, 40, 7, 18, 44, 2]    | 7839.28   |3.94 
    2     |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
    3     |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
    4     |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
    5     |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
    6     |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
    7     |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
    8     |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
    9     |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
    10    |20      | 1000      |0.5   |0.5  |0.1  |58.18  |      |    | 
