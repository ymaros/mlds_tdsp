# Reporte del Modelo Baseline

Este documento presenta los resultados obtenidos con el modelo baseline basado en una red neuronal LSTM para la tarea de generación de descripciones de imágenes (image captioning) utilizando el dataset Flickr8k.

## Descripción del modelo

El modelo baseline es un modelo LSTM que combina visión por computadora y procesamiento de lenguaje natural para generar descripciones textuales de imágenes. La arquitectura se divide en dos partes:

* **Encoder**: Utiliza características extraídas de una imagen, normalizadas y pasadas a través de capas densas para alinear las dimensiones con el decodificador.
* **Decoder**: Se basa en una capa de incrustación (embedding), seguida de una capa LSTM para generar secuencias de palabras. Las salidas son generadas por una capa de adición y dos capas densas.

Este modelo fue entrenado utilizando el dataset Flickr8k, y el objetivo es generar descripciones de imágenes a través de una red neuronal LSTM, minimizando el error en la predicción de palabras en las secuencias.

## Variables de entrada

Las variables de entrada utilizadas en el modelo son:

* **Características de la imagen (x_image)**: Características extraídas de las imágenes mediante el modelo preentrenado Inception v3. Estas características se pasan como entrada al encoder.
* **Palabras de la descripción (x_captions)**: Las cinco descripciones asociadas a cada imagen se utilizan como secuencias para entrenar el decodificador.

## Variable objetivo

La variable objetivo es:

* **Palabra siguiente en la secuencia (y_target)**: En cada paso de tiempo, el modelo predice la siguiente palabra en la secuencia de la descripción de la imagen. El objetivo es minimizar la pérdida en la predicción de esta palabra.

## Evaluación del modelo

### Métricas de evaluación

Las métricas utilizadas para evaluar el rendimiento del modelo incluyen:

* **BLEU score**: Métrica que evalúa la calidad de las descripciones generadas comparándolas con las descripciones reales, midiendo la coincidencia de n-gramas entre las descripciones generadas y las de referencia.

### Resultados de evaluación

A continuación se muestran algunos resultados obtenidos en las métricas de evaluación para el modelo baseline:

|   Métrica   |   Resultado   |
|-------------|---------------|
| BLEU-1      | 0.31434       |
| BLEU-2      | 0.21291       |
| BLEU-1      | 0.29492       |
| BLEU-2      | 0.1775        |

## Análisis de los resultados

El modelo baseline muestra un rendimiento inicial que sirve como referencia para la mejora de modelos más complejos. Se observaron los siguientes puntos:

### Fortalezas

* **Simplicidad**: La arquitectura LSTM es bastante accesible y fácil de implementar, lo que hace que sea ideal para establecer una línea base en tareas de captioning de imágenes.
Adecuación para secuencias: El uso de LSTM permite capturar dependencias a largo plazo en las secuencias de palabras generadas.

### Debilidades

* **Bajo rendimiento en BLEU**: Aunque el modelo baseline ofrece una referencia, los valores de BLEU, especialmente para n-gramas más grandes (BLEU-3 y BLEU-4), son relativamente bajos. Esto indica que el modelo aún tiene dificultades para generar descripciones coherentes y completas.
Capacidad limitada de generalización: El modelo podría beneficiarse de un mayor ajuste de hiperparámetros o la incorporación de técnicas más avanzadas como Beam Search o el uso de redes neuronales más profundas.

## Conclusiones

El modelo baseline ha establecido una referencia útil para evaluar el rendimiento de modelos más complejos en tareas de captioning de imágenes. Aunque el rendimiento es adecuado para un primer paso, las métricas BLEU sugieren que se deben realizar mejoras en el modelo. Las áreas de mejora incluyen:

* Mejora en la calidad de las descripciones generadas mediante el ajuste de los hiperparámetros y la inclusión de técnicas avanzadas de búsqueda como Beam Search.
* Explorar redes neuronales más complejas o incorporar mecanismos de atención para capturar mejor las relaciones entre las palabras y las características visuales.

## Referencias

* [InceptionV3](https://www.mathworks.com/help/deeplearning/ref/inceptionv3.html)
* [¿Qué son las Redes LSTM?](https://codificandobits.com/blog/redes-lstm/)
* [What is a BLEU score?](https://learn.microsoft.com/en-us/azure/ai-services/translator/custom-translator/concepts/bleu-score)
