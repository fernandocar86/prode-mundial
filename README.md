# Prode para mundial

Código para prode mundialista de uso casero. 

# Funcionamiento

Correr el archivo main.py desde la terminal:

```python main.py ```

Un cuadro de diálogo va a pedir confirmar si se van a usar los puntajes estándar o si se prefiere personalizarlos.

La información de los resultados se va a buscar en la carpeta resultados y la información de las estimaciones de cada participante se va a buscar en la carpeta estimaciones-participantes. Un cuadro de diálogo en la terminal va a permitir cambiar estos directorios. Las estimaciones de cada participante deben estar guardadas en una planilla que lleve por denominación el nombre con el que se desea que ese participante aparezca en la grilla de puntajes.

# Puntajes

Los puntajes que se asignan por defecto son los siguientes:

Resultado exacto | orientación del resultado + goles de un equipo | orientación del resultado | goles de un equipo	| 
| --- | --- | --- | --- | 
10 |7 | 5 |2 |

Para cada carga de resultados se puede configurar el peso que tienen los puntajes. Lo recomendado es utilizar el doble para los partidos a partir de los octavos de final.

Recordar que si esto se usa para el mundial de 2022, la cantidad de partidos por fase son las siguientes:

| Fase | Total de partidos |
| --- | --- |
| Fase eliminatorias | 48 |
| Octavos de final | 8
| Cuartos de final | 4 |
| Semifinales | 2 |
| 3er lugar | 1 |
| final | 1 |

Dependiendo del peso que se le dé a cada fase, se obtendrán puntajes máximos diferentes.

Una vez que se corre el código, los puntajes y ganadores del prode según los resultados cargados, ya sean totales o parciales, se van a visualizar en el archivo home.html. 
