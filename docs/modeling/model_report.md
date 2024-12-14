# Reporte del Modelo Final

## Resumen Ejecutivo

El modelo final desarrollado es un sistema de generación de descripciones de imágenes basado en redes neuronales LSTM. Utiliza características visuales extraídas por un modelo InceptionV3 y secuencias de texto procesadas por una arquitectura LSTM para generar descripciones coherentes de las imágenes. Las evaluaciones se realizaron utilizando BLEU scores y comparando los resultados de dos métodos de inferencia: Greedy y Beam Search.

## Descripción del Problema

La generación automática de descripciones para imágenes es un problema desafiante que combina procesamiento de lenguaje natural y visión por computadora. El objetivo principal es crear un modelo que pueda generar descripciones precisas y naturales para imágenes del conjunto de datos Flickr8k. Este problema es relevante en aplicaciones como accesibilidad, sistemas de búsqueda de imágenes, y más.

## Descripción del Modelo

El modelo incluye las siguientes etapas:

### Preprocesamiento de datos

* Se utilizó el dataset Flickr8k.
* Las imágenes se procesaron mediante un modelo preentrenado InceptionV3 para extraer características.
* Las descripciones se normalizaron y tokenizaron.

### Arquitectura del modelo

* Encoder: Extrae características visuales de las imágenes mediante InceptionV3 y las pasa por una capa densa con normalización.
* Decoder: Combina una capa de incrustación (embedding) con una capa LSTM que genera la secuencia de salida.
* El modelo incluye capas densas adicionales para generar la predicción final.

### Entrenamiento

* Se entrenó con un optimizador Adam y la función de pérdida categorical crossentropy.
* Se utilizó Early Stopping y un Learning Rate Scheduler.
* La pérdida en entrenamiento disminuyó significativamente, alcanzando un val_loss mínimo de 3.260 en la octava época.

## Evaluación del Modelo

### Métricas de Evaluación

Se utilizaron las siguientes métricas:

* BLEU-1 y BLEU-2 para evaluar la calidad de las descripciones generadas.
* Comparación entre Greedy y Beam Search para identificar el mejor método de inferencia.

### Resultados de Evaluación

|   Método   |   BLEU-1   |   BLEU-2   |
|------------|------------|------------|
| Greedy    | 0.327    | 0.201         |
| Beam Search (K=5)     | 0.285    |  0.285          |

El método Beam Search mostró resultados ligeramente superiores en BLEU-2, indicando una mejor capacidad para generar secuencias más largas y coherentes.

Visualización de Resultados
Las descripciones generadas para las imágenes incluyen:

Greedy: "A brown dog is running through the grass."
Beam Search: "A brown and white dog is running through the grass."
Los resultados muestran que el modelo tiene un buen desempeño para capturar la esencia de las imágenes, aunque en ocasiones las descripciones son genéricas o repiten elementos.

## Conclusiones y Recomendaciones

Incluir un mecanismo de atención (attention mechanism) para mejorar la relación entre las características visuales y las palabras generadas.

Aumentar el tamaño del dataset para mejorar la capacidad del modelo de generalizar.

Experimentar con ajustes en el tamaño del beam en Beam Search para optimizar la generación de descripciones.

## Referencias

* Dataset Flickr8k: https://forms.illinois.edu/sec/1713398
* Modelo InceptionV3 preentrenado: Keras Applications
* BLEU Score: Evaluación estándar para tareas de generación de lenguaje.
