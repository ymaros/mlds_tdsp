# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Image Captioning Model with InceptionV3 and LSTM
- **Plataforma de despliegue:** REST API con FastAPI
- **Requisitos técnicos:**
  - Python 3.12
  - Dependencias principales:

    ```plaintext
    fastapi==0.104.1
    uvicorn==0.24.0
    tensorflow==2.14.0
    Pillow==10.1.0
    python-multipart==0.0.6
    numpy==1.24.3
    ```

  - Hardware mínimo:
    - CPU: 4 cores
    - RAM: 8GB
    - Almacenamiento: 2GB para modelos y dependencias
  - Hardware recomendado:
    - CPU: 8 cores
    - RAM: 16GB
    - GPU: Compatible con CUDA (opcional)
    - Almacenamiento: 5GB

- **Requisitos de seguridad:**
  - CORS (Cross-Origin Resource Sharing) configurado
  - Validación de tipos de archivo (solo imágenes)
  - Limpieza automática de archivos temporales
  - Manejo seguro de carga de archivos
  - Rate limiting recomendado en producción
  - Monitoreo de salud del servicio

- **Diagrama de arquitectura:**

```plaintext
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Cliente   │─────│  FastAPI     │─────│ Procesador  │
│   (HTTP)    │     │  Endpoint    │     │ de Imágenes │
└─────────────┘     └──────────────┘     └─────────────┘
                           │                     │
                    ┌──────┴──────┐       ┌─────┴─────┐
                    │  Modelos    │       │ InceptionV3│
                    │  Cargados   │       │  Feature   │
                    │             │       │ Extraction │
                    └─────────────┘       └───────────┘
                    ┌─────────────┐
                    │  Tokenizer  │
                    │    PKL      │
                    └─────────────┘
```

## Código de despliegue

- **Archivo principal:**
  - ```app.py```: Servidor FastAPI y lógica principal
  - ```model_loader.py```: Carga de modelos y clases auxiliares

- **Rutas de acceso a los archivos:**

```plaintext
mlds_tdsp/
├── src/
│   ├── models/
│   │   ├── caption_model.keras
│   │   ├── tokenizer.pkl
│   │   └── weights/
│   │       └── caption_model.weights.h5
│   └── database/
│       └── flickr8k/
│           └── Images/
└── scripts/
    └── evaluation/
        ├── model_loader.py
        └── app.py
```

- **Variables de entorno:**

```plaintext
MODEL_PATH=../../src/models/caption_model.keras
WEIGHTS_PATH=../../src/models/weights/caption_model.weights.h5
TOKENIZER_PATH=../../src/models/tokenizer.pkl
PORT=8000
HOST=0.0.0.0
```

## Documentación del despliegue

- **Instrucciones de instalación:**

1. Clonar el repositorio:

```bash
git clone <repository_url>
cd mlds_tdsp
```

2. Crear y activar entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# o
.venv\Scripts\activate     # Windows
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

- **Instrucciones de configuración:**

1. Verificar estructura de directorios y archivos necesarios:

- Modelo: src/models/caption_model.keras
- Pesos: src/models/weights/caption_model.weights.h5
- Tokenizador: src/models/tokenizer.pkl

2. Iniciar el servidor:

```bash
cd scripts/evaluation
python app.py
```

- **Instrucciones de uso:**

1. Usando curl

```bash
# Generar caption para una imagen
curl -X POST -F "file=@path/to/your/image.jpg" http://localhost:8000/generate-caption/

# Verificar estado del servicio
curl http://localhost:8000/health
```

2. Usando Python

```python
import requests

# Generar caption para una imagen
url = "http://localhost:8000/generate-caption/"
files = {"file": open("path/to/your/image.jpg", "rb")}
response = requests.post(url, files=files)
print(response.json())

# Verificar estado del servicio
health_response = requests.get("http://localhost:8000/health")
print(health_response.json())
```

3. Usando la interfaz web

   1. Acceder a la documentación interactiva:
      - Swagger UI: http://localhost:8000/docs
      - ReDoc: http://localhost:8000/redoc
   2. Probar el endpoint desde la interfaz Swagger:
      - Ir a http://localhost:8000/docs
      - Clic en POST /generate-caption/
      - Clic en "Try it out"
      - Subir una imagen
      - Ejecutar y ver resultados

- **Instrucciones de mantenimiento:**

1. Monitoreo:

   - Verificar regularmente el endpoint de salud
   - Monitorear uso de memoria y CPU
   - Revisar logs del servidor

2. Actualizaciones:

   - Realizar backups antes de actualizar
   - Actualizar dependencias periódicamente
   - Mantener versiones compatibles de TensorFlow y FastAPI

3. Troubleshooting común:

   - Si el modelo no carga: Verificar rutas y permisos de archivos
   - Si hay errores de memoria: Ajustar batch_size o liberar memoria
   - Si hay timeout: Ajustar configuración de uvicorn

4. Escalamiento:

   - Considerar usar contenedores Docker
   - Implementar balanceo de carga para múltiples instancias
   - Configurar caché para resultados frecuentes

5. Seguridad:

   - Mantener dependencias actualizadas
   - Implementar rate limiting
   - Monitorear intentos de acceso no autorizados
   - Realizar copias de seguridad periódicas
