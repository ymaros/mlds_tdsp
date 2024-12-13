# Diccionario de datos

La base de datos utilizada en este proyecto, contiene información sobre las imágenes y sus respectivas descripciones. Los datos provienen del conjunto de datos Flickr8k.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| -------- | ----------- | ------------ | ---------------------- | --------------- |
| ```image_id``` | Identificador único de la imagen | String | ID único por imagen (ej. "1000268201_693b08cb0e.jpg") | ```src/database/flickr8k/Images/``` |
| ```caption``` | Descripción textual de la imagen | String | Texto libre, con oraciones descriptivas | ```src/database/flickr8k/captions.txt``` |

---

```image_id```: Identificador único de la imagen, utilizado tanto para las imágenes físicas (archivos .jpg) como para asociar las descripciones y características extraídas de cada imagen.

```caption```: Descripción textual que explica lo que ocurre en la imagen. La descripción ha sido preprocesada para facilitar la tarea de análisis y modelado.
