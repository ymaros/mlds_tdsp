# Definición de los datos

## Origen de los datos

Los datos provienen del Flickr8k Dataset de Kaggle, que es un conjunto de imágenes que contiene 8,000 imágenes de tamaño variable con anotaciones de texto. Este conjunto de datos se utiliza comúnmente para tareas de visión por computadora y procesamiento de lenguaje natural, como la generación de descripciones de imágenes.

Los datos se obtienen mediante el portal de Kaggle. El enlace directo es: [Flickr8k Dataset](https://www.kaggle.com/datasets/adityajn105/flickr8k).

## Especificación de los scripts para la carga de datos

Scripts utilizados para la carga de datos:

- **Script de adquisición de datos**: Los scripts de adquisición de datos se encuentran en la carpeta ```scripts/data_acquisition```. Estos scripts se encargan de:
  - Descargar los datos desde Kaggle.
  - Descomprimir y organizar las imágenes y los archivos de anotaciones.
- **Script EDA (Exploratory Data Analysis)**: Los scripts de EDA están en la carpeta ```scripts/eda```. En esta carpeta se realizan tareas como:
  - Cargar y visualizar las imágenes y sus descripciones.
  - Estadísticas sobre las anotaciones y las imágenes.
Preparación inicial para la carga de los datos.
- **Script de preprocesamiento**: Los scripts de preprocesamiento se encuentran en la carpeta ```scripts/preprocessing```. En esta sección se realizan las siguientes tareas:
  - Transformaciones de imagen: Redimensionar las imágenes, normalización, y convertirlas en un formato adecuado para alimentar modelos de aprendizaje automático.
  - Limpieza de datos: Filtrar las anotaciones que no sean útiles o eliminar las imágenes sin descripción.
  - Tokenización de las descripciones: Transformar las descripciones en vectores de tokens (palabras o sub-palabras), que se utilizan para modelos de visión y lenguaje como la generación de texto o la clasificación de imágenes.
  - División en conjuntos de datos: Dividir las imágenes y sus descripciones en conjuntos de entrenamiento, validación y prueba, que se usarán en el proceso de modelado.

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

Ubicación de los archivos de origen de los datos: Los archivos de origen de los datos se encuentran en el siguiente directorio:

- Imágenes: ```src/database/flickr8k/Images/```
- Anotaciones: ```src/database/flickr8k/captions.txt```

La carpeta Images contiene las imágenes en formato .jpg, .jpeg, .png, etc. que forman parte del conjunto de datos. El archivo captions.txt contiene las descripciones de las imágenes en formato de texto.

Estructura de los archivos de origen de los datos:

**Imágenes**: La estructura de los archivos en el directorio Images es la siguiente:

```bash
Images/
  ├── 1000268201_693b08cb0e.jpg
  ├── 1001773457_577c3a7d70.jpg
  ├── 1002674143_1b742ab4b8.jpg
  ├── ...
```

Cada archivo de imagen tiene un nombre único, que sirve como identificador de la imagen.

**Captions (descripciones)**: El archivo captions.txt tiene el siguiente formato:

```bash
image_id,caption
1000268201_693b08cb0e.jpg,A man in a blue shirt is playing a guitar.
1001773457_577c3a7d70.jpg,A child is playing with a toy.
1002674143_1b742ab4b8.jpg,A dog running across a field.
...
```

Cada línea del archivo contiene un identificador de imagen y su descripción correspondiente, separados por coma.

Procedimientos de transformación y limpieza de los datos:

- Limpieza de datos:
  - El archivo captions.txt se procesa para eliminar posibles líneas vacías o malformadas.
  - Las descripciones se normalizan (en caso de ser necesario), eliminando caracteres no deseados.
- Transformación de datos:
  - Las descripciones de las imágenes se tokenizan para ser procesadas posteriormente por modelos de procesamiento de lenguaje natural.
  - Las imágenes se redimensionan o se preprocesan para que puedan ser alimentadas en redes neuronales (esto puede incluir normalización o escalado de píxeles).
  - Los identificadores de imagen se asocian con sus descripciones correspondientes para formar un conjunto de datos adecuado para tareas de generación de texto o clasificación.

### Integración con DVC (Data Version Control)

DVC es utilizado para gestionar el ciclo de vida de los datos en el proyecto, permitiendo versionar y realizar un seguimiento de los datos y modelos de manera eficiente. Los scripts y la estructura de carpetas también están organizados para aprovechar DVC en la gestión de los datos.
