# Discord AI Image Classifier Bot

## Description

This project is a Discord bot that uses Artificial Intelligence to classify images sent by users. The bot was developed with Python, Discord.py, TensorFlow, and Keras.

Users can upload an image using a command, and the bot analyzes it with a trained image classification model. After the inference process, the bot responds with the detected object and the confidence level of the prediction.

The project also includes error handling for invalid image formats and low-confidence predictions.

## Features

* Image classification using AI
* Discord bot integration
* TensorFlow/Keras trained model
* Confidence score detection
* Error handling system
* Supports JPG and PNG images

## Technologies Used

* Python
* Discord.py
* TensorFlow
* Keras
* NumPy
* Pillow

## Example Command

```bash
$check
```

Upload an image together with the command and the bot will analyze it automatically.

## Screenshots

Add screenshots here:

```md
![Bot Screenshot](images/screenshot.png)
```

## Installation

```bash
pip install tensorflow keras discord.py pillow numpy requests
```

Run the bot with:

```bash
python main.py
```

## License

This project is licensed under the MIT License.
