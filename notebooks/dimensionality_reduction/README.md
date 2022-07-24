# Dimensionality Reduction 
 
### Introduccion

Las tecnicas de reduccion de dimensionalidad son muy utiles para evitar la multicolinealidad, es decir, multiples features con multiples correlaciones entre si. Por tanto, deberian mejorar el performance de algoritmos predictivos al asegurarse de evitar este problema usando unicamente feautures totalmente independientes entre si sin perdida de informacion. Por tanto, es mejor alternativa que ponerse a eliminar variables correlacionadas entre si. Eso si, esta tecnica reduce la explicabilidad.

Por otro lado, estas tecnicas pueden ser usadas para el analisis de los datos, para encontrar patrones ocultos, para conocer mejor las relaciones entre las variables. 

Las dos tecnicas mas predominantes son PCA y Factor Analysis. 

### PCA

La primera transforma la variables a subespacios alternativos de tal manera que a la primera le otorga la dimension de maxima variabilidad, y sucesivamente va adjudicando las siguientes componentes manteniendo la independencia entre ellas hasta que explican toda la variabilidad de los features originales. Matematicamente estos componentes son combinanciones lineales de los features.

Esta tecnica es la mas recomendable para ser usada para reducir dimensiones paso previo de un algoritmo predictivo pues no pierdes casi variabilidad (segun el numero de PCs finalmente escogidos, por supuesto).

### Factor Analysis

Esta tecnica tiene muchos aspectos comunes a PCA pero se diferencia en su objetivo. Factor Analysis extrae factores (latentes) o donde se concentra la variabilidad comun de las variables originales. Matematicamente, las variables originales son combinaciones lineales de estos factores. 

Esta tecnica se usa mas para analisis permitiendo extraer agrupaciones de variables a traves de sus partes comunes.El problema es que puede dejarse atras mucha informacion por lo que es mejor no ser usada como paso previo a algoritmos predictivos.


### Tecnicas de interes

- Principal component analysis (PCA): Para variables numericas.
- Correspondence analysis (CA): Para dos variables categoricas.
- Multiple correspondence analysis (MCA): Para multiples variables categoricas.
- Kernel Principal component analysis (KernelPCA): Para variables numericas. Admite relaciones no lineales entre variables y su los PCs resultantes si que consiguen una separabilidad lineal.
- Linear Discriminant Analysis (LDA): Esta tecnica es supervisada, es decir, requiere features y labels (clasificacion). Es muy parecido a PCA pero intenta escoger el subespacio de features mejorando la separabilidad de las clases del label.


- Factor analysis: Es para vairables numericas. Los Factor Analaysis son mas recomendables para analysis (variabilidad comun entre variables) y no como tecnica de reduccion de dimensionalidad para ser usada con un algoritmo predictivo pues puede que se deja mas variabilidad sin explicar.
- Factor analysis of mixed data (FAMD): Para variables categoricas y numericas. 