# Diccionario de datos

## Base de datos 1

Esta base de datos contiene información sobre las imágenes y sus respectivas descripciones. Los datos provienen del conjunto de datos Flickr8k.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| -------- | ----------- | ------------ | ---------------------- | --------------- |
| ```image_id``` | Identificador único de la imagen | String | ID único por imagen (ej. "1000268201_693b08cb0e.jpg") | ```src/database/flickr8k/Images/``` |
| ```caption``` | Descripción textual de la imagen | String | Texto libre, con oraciones descriptivas | ```src/database/flickr8k/captions.txt``` |

- ```image_id```: Identificador único de la imagen, utilizado tanto para las imágenes físicas (archivos .jpg) como para asociar las descripciones y características extraídas de cada imagen.
- ```caption```: Descripción textual que explica lo que ocurre en la imagen. La descripción ha sido preprocesada para facilitar la tarea de análisis y modelado.

## Base de datos 2

Esta base de datos contiene las descripciones de las imágenes que han sido preprocesadas (tokenización, eliminación de caracteres no deseados, etc.). Los datos provienen de la limpieza del archivo captions.txt.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| -------- | ----------- | ------------ | ---------------------- | --------------- |
| ```image_id``` | Identificador único de la imagen | String | ID único por imagen (ej. "1000268201_693b08cb0e.jpg") | ```src/database/flickr8k/Images/``` |
| ```caption``` | Descripción limpia y procesada de la imagen | String | Texto libre, procesado (sin caracteres no deseados, en minúsculas) | ```src/database/flickr8k/captions_preprocessed.txt``` |

- ```image_id```: Identificador único de la imagen, usado como clave para asociar las descripciones limpias con las imágenes correspondientes.
- ```caption```: Descripción procesada de la imagen. Las descripciones son procesadas para eliminar palabras irrelevantes, normalizar (convertir a minúsculas) y tokenizar las palabras, lo que facilita el análisis en modelos de aprendizaje automático.
