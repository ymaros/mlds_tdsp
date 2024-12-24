# Informe de salida

## Resumen Ejecutivo

Este informe describe los resultados del proyecto de machine learning y presenta los principales logros y lecciones aprendidas durante el proceso.

## Resultados del proyecto

Como resultado de este proyecto fueron generados múltiples scripts o notebooks de Python que abarcan desde la adquisición de los datos hasta el despliegue del modelo para su uso productivo:

- Notebook para la adquisión de datos del entrenamiento, pruebas y evaluación del modelo en `scripts/data_acquisition`.
- Notebook para el análisis exploratorio de los datos en `scripts/eda`.
- Notebook para el preprocesamiento de los datos en `scripts/preprocessing`.
- Notebook para el entrenamiento del modelo en `scripts/training`.
- Scripts para la evaluación y despliegue del modelo en `scripts/evaluation`.

En cada una de las etapas se consiguió el objetivo correspondiente de tal forma que al final se obtuvo una nueva versión del modelo base con un rendimiento 33 % mayor en el mejor de los casos.

| Modelo | BLEU-1 | Mejora | BLEU-2 | Mejora |
|--------|--------|--------|--------|--------|
| Base | 0.31434 | - | 0.21291 | - |
| Greedy | 0.327 | + 4 % | 0.201 | - 6 % |
| Beam Search (K=5) | 0.285 | - 9 %  | 0.285 | + 33 % |

Aunque con un amplio margen para mejorar, el modelo es capaz de entregar descripciones de imágenes textualmente coherentes, por lo que podría ser usado en páginas web o en medios de comunicación que muestren imágenes en contexto.

## Lecciones aprendidas

Como principal desafío se identificó el limitado tamaño del conjunto de datos del que se disponía para realizar el entrenamiento del modelo. El conjunto solo contaba con 8000 imágenes con 5 descripciones de cada una, lo que limitó la variedad de los datos de entrada del modelo.

Como lecciones aprendidas quedó que, aunque el modelo base tiene un rendimiento significativo, la mejoría de este implica una gran cantidad de datos y un amplio tiempo de entrenamiento, por lo que se debe evaluar el costo de obtener estos datos y entrenar el modelo contra el de dedicar a una persona a realizar esta tarea.

## Impacto del proyecto

El modelo es capaz de entregar descripciones textualmente correctas, aunque no tan precisas a la hora de describir la imagen a la que corresponden, por lo que puede usarse en imágenes que hacen parte de un contexto como en sitios web o en medios de comunicación.

En futuras implementaciones del modelo, mediante un conjunto de datos mayor y más variado, se espera que el rendimiento de este mejore lo suficiente como para ser implementado en otras áreas.

## Conclusiones

Dependiento de la estrategia y de la métrica se obtuvo una mejoría o un empeoramiento en el rendimiento del modelo. Sin embargo, para la estrategia Beam Search se obtuvo una mejoría total del 24 %, alcanzado con un conjunto de datos relativamente pequeño y limitado.

En este sentido, resulta intuitivo pensar que un conjunto de datos más grande y variado, y con un tiempo de entrenamiento mayor, se podría obtener una ganancia en todas las métricas.

## Agradecimientos

Agradecimientos a los integrantes del grupo por su esfuerzo, semana a semana, en este proyecto.

Agradecimientos a la empresa por financiar el proyecto.
