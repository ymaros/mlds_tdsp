# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Generación automática de descripciones para imágenes (Image Captioning)

## Objetivo del Proyecto

Este proyecto tiene como objetivo desarrollar un sistema de inteligencia artificial capaz de describir el contenido visual de una imagen mediante texto. Para ello, combina redes neuronales convolucionales (CNN) que extraen las características de la imagen con redes recurrentes (RNN o LSTM) que generan una descripción en lenguaje natural a partir de esas características. Finalmente este modelo se desplegará a través de un API prototipo para validar su funcionamiento a usuario o sistemas externos.

Entre los beneficiarios potenciales de este proyecto se encuentran empresas tecnológicas, plataformas de comercio electrónico, instituciones para personas con discapacidades visuales, medios de comunicación, y plataformas educativas. En comercio electrónico, la automatización de descripciones de productos ahorra tiempo y recursos, mientras que en redes sociales y plataformas tecnológicas, como Google o Facebook, mejora la gestión y búsqueda de imágenes. Para las personas con discapacidades visuales, este sistema facilita el acceso a contenido visual a través de descripciones accesibles. Además, los medios de comunicación pueden generar descripciones instantáneas de imágenes para agilizar la publicación de noticias, y las instituciones educativas pueden ofrecer materiales más accesibles y fáciles de buscar.

Este proyecto aborda varios desafíos importantes, como la automatización del etiquetado y descripción de imágenes, lo que reduce costos y mejora la eficiencia en empresas que manejan grandes volúmenes de imágenes. También mejora la accesibilidad, permitiendo que personas con discapacidades visuales accedan a contenido visual mediante descripciones de texto, y facilita la búsqueda eficiente en bases de datos de imágenes, optimizando el acceso a contenido visual. Además, acelera la generación de contenido en tiempo real en los medios y mejora la experiencia del cliente en plataformas de comercio electrónico mediante descripciones precisas y automatizadas.

## Alcance del Proyecto

El proyecto de generación automática de descripciones para imágenes (Image Captioning) busca implementar una solución de Deep Learning que automatice la tarea de describir imágenes de manera precisa y eficiente. Esta solución combinará redes neuronales convolucionales (CNN) para extraer las características visuales de las imágenes, con redes neuronales recurrentes (RNN o LSTM) que generarán descripciones en lenguaje natural basadas en esas características. El objetivo es crear un sistema capaz de analizar imágenes y producir descripciones coherentes que representen su contenido visual, mejorando la eficiencia en diversos sectores y promoviendo la accesibilidad.

Para lograr esto, se desarrollará un modelo de inteligencia artificial que podrá extraer características visuales de las imágenes mediante una CNN preentrenada, y generar descripciones en texto utilizando una RNN o LSTM que esté entrenada para formar secuencias de palabras coherentes. El modelo se entrenará utilizando conjuntos de datos etiquetados como Flickr8k, que incluyen imágenes con descripciones correspondientes. Posteriormente, el modelo será optimizado para generar descripciones precisas de nuevas imágenes. También se llevará a cabo una fase de prueba y validación para asegurar que las descripciones producidas por el sistema sean relevantes, precisas y de alta calidad.

El producto resultante de este proyecto podrá ser utilizado de diversas maneras según el tipo de cliente o beneficiario. Las empresas de comercio electrónico podrán integrar esta solución en sus plataformas para generar descripciones automáticas de productos, optimizando el proceso de catalogación y mejorando la experiencia del usuario al ofrecer descripciones consistentes y detalladas. Las personas con discapacidades visuales podrán beneficiarse mediante herramientas de accesibilidad, como lectores de pantalla, que utilizarán las descripciones generadas para proporcionar una experiencia más inclusiva en sitios web y plataformas digitales. En los medios de comunicación y redes sociales, el sistema permitirá generar descripciones automáticas de imágenes en tiempo real, facilitando la publicación rápida de contenido con contexto textual adecuado. Finalmente, las plataformas educativas podrán usar esta tecnología para describir imágenes en materiales de aprendizaje, mejorando la accesibilidad y ayudando a los usuarios a comprender mejor los contenidos visuales.

### Incluye:

#### Descripción general de los datos
-  El conjunto de datos Flickr8k contiene 8,000 imágenes. Cada imagen en este dataset viene acompañada de cinco descripciones en lenguaje natural que proporcionan contexto sobre su contenido visual.
- Los datos se obtendrán directamente desde la plataforma Kaggle, accediendo al conjunto de datos Flickr8k. Desde allí, se utilizara la API de Kaggle para obtener el dataset que contiene tanto las imágenes, como un archivo de texto que almacena las descripciones correspondientes a cada imagen.
- El tamaño total del conjunto de datos Flickr8k es de aproximadamente 1 GB, incluyendo las imágenes y las descripciones. Cada imagen tiene un tamaño promedio de entre 50 y 100 KB, mientras que las descripciones ocupan poco espacio en el archivo de texto. El tamaño de los datos aumentará ligeramente durante el procesamiento debido a las transformaciones y la generación de matrices de características tanto de las imágenes como de las descripciones textuales.

#### Descripción de los resultados esperados
- El principal resultado esperado de este proyecto es el despliegue de un API que permita utilizar un modelo de Deep Learning capaz de generar descripciones en lenguaje natural que sean precisas, coherentes y relevantes para una amplia variedad de imágenes. La calidad de estas descripciones se evaluará en términos de consistencia, precisión y fluidez del lenguaje, asegurando que el contenido generado sea comprensible y adecuado para su propósito.

#### Criterios de éxito del proyecto
- Precisión y relevancia de las descripciones: El modelo deberá lograr un rendimiento mínimo, asegurando que las descripciones generadas sean coherentes con el contenido visual.
- Tiempo de generación: El prototipo deberá ser capaz de generar una descripción en menos de 2 segundo por imagen.
- Capacidad de Generalización: El modelo deberá demostrar una buena capacidad para generalizar y generar descripciones precisas sobre imágenes no presentes en el conjunto de datos de entrenamiento.
- Entrega de prototipo: entrega de API que permita obtener las descripciones de una imágen dada

### Excluye:

- Etiquetado manual de imágenes: No se incluirá la tarea de etiquetar manualmente nuevas imágenes. Todas las imágenes usadas para el entrenamiento y validación se obtendrán de conjuntos de datos preexistentes, como Flickr8k.
- Generación Multilingüe: Las descripciones generadas estarán únicamente en inglés. La generación de descripciones en otros idiomas queda fuera del alcance de este proyecto.

## Metodología

- Preparación del conjunto de datos: Se utilizará el conjunto de datos Flickr8k, descargándolo a través de la API de Kaggle. Se llevará a cabo un análisis exploratorio de los datos para verificar la calidad de las imágenes y sus descripciones, realizando cualquier limpieza necesaria.

- Diseño del modelo: Se desarrollará un modelo que combina CNN (para la extracción de características visuales) y RNN/LSTM (para la generación de descripciones). Se seleccionarán arquitecturas preentrenadas como VGG16 o Inception para la CNN, y una LSTM para la RNN.

- Entrenamiento del modelo: El modelo se entrenará utilizando los datos de Flickr8k. Se implementarán técnicas de optimización como dropout, ajuste de hiperparámetros y optimizadores como Adam para mejorar el rendimiento del modelo.

- Evaluación del modelo: Se evaluará el rendimiento del modelo con métricas como BLEU, METEOR y CIDEr, utilizando un conjunto de datos de validación separado. Además, se realizará una evaluación cualitativa del modelo con un grupo de usuarios objetivo para obtener feedback sobre la calidad de las descripciones.

- Optimización e iteración: Con base en los resultados de la evaluación, se realizarán ajustes en el modelo para mejorar la calidad y precisión de las descripciones. Se iterará el proceso hasta alcanzar los criterios de éxito definidos.

- Despliegue del prototipo: Finalmente, se desarrollará un API que muestre su aplicabilidad. Este prototipo servirá como prueba de concepto del impacto del proyecto en escenarios reales.

## Cronograma

| **Etapa** | **Duración Estimada** | **Fechas** |
|------|---------|-------|
| *Fase 1:* Entendimiento del negocio y carga de datos | 8 días | del 20 de noviembre al 28 de noviembre |
| *Fase 2:* Preprocesamiento, análisis exploratorio | 5 días | del 29 de noviembre al 05 de diciembre |
| *Fase 3:* Modelamiento y extracción de características | 5 días | del 06 de diciembre al 12 de diciembre |
| *Fase 4:* Despliegue | 5 días| del 13 de diciembre al 19 de diciembre |
| *Fase 5:* Evaluación y entrega final | 2 día | del 19 de diciembre al 21 de diciembre |

## Equipo del Proyecto

- Diego Saavedra
- Gerson Pineda
- Yeison Martínez
