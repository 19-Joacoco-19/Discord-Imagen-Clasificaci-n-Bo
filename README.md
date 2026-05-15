# Bot de Discord con Clasificación de Imágenes usando IA

## Descripción

Este proyecto consiste en un bot de Discord desarrollado con Python que utiliza Inteligencia Artificial para clasificar imágenes enviadas por los usuarios.

El bot usa un modelo entrenado con TensorFlow y Keras para analizar imágenes y detectar objetos automáticamente. Después del proceso de inferencia, el bot responde mostrando el objeto detectado y el nivel de confianza de la predicción.

Además, el proyecto incluye manejo de errores para formatos de imagen no válidos y predicciones con baja confianza.

## Características

* Clasificación de imágenes mediante IA
* Integración con Discord
* Modelo entrenado con TensorFlow/Keras
* Detección de nivel de confianza
* Manejo de errores
* Compatibilidad con imágenes JPG y PNG

## Tecnologías utilizadas

* Python
* Discord.py
* TensorFlow
* Keras
* NumPy
* Pillow
* Requests

## Comando de ejemplo

```bash
$check
```

El usuario debe enviar una imagen junto al comando para que el bot la analice automáticamente.

## Capturas de pantalla

Agrega aquí imágenes del funcionamiento del bot:

```md
![Captura](https://raw.githubusercontent.com/19-Joacoco-19/Discord-Imagen-Clasificaci-n-Bo/main/screenshot.png)
```

## Instalación

Instalar dependencias:

```bash
pip install tensorflow keras discord.py pillow numpy requests
```

Ejecutar el bot:

```bash
python main.py
```

## Licencia

Este proyecto está bajo la licencia MIT.
