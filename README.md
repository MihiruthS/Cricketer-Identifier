# Cricketer Identifier Model

This repository contains a Cricketer Identifier model that can identify a cricketer from a given picture. The model is designed to recognize five legendary cricketers: Kumar Sangakkara, Mahela Jayawardene, Sanath Jayasuriya, MS Dhoni, and Virat Kohli. 

## Overview

The Cricketer Identifier model uses OpenCV for image processing, Python FlaskNet for the web server, and Haar Cascade for face detection. The project includes all necessary files for model training, user interface, and server setup.

![image](https://github.com/MihiruthS/Cricketer-Identifier/assets/166645514/ef99dca7-d221-4118-9ae3-7845e51a11a0)

## Features

- Identify cricketers from an image
- Recognize five specific cricketers:
  - Kumar Sangakkara
  - Mahela Jayawardene
  - Sanath Jayasuriya
  - MS Dhoni
  - Virat Kohli

## Project Structure

The repository is organized as follows:

- `model/`: Contains scripts and data for training the identification model.
- `ui/`: Contains the user interface code for uploading and displaying images.
- `server/`: Contains the server code to handle requests and run the model.

## Dependencies

To run this project, you need to have the following installed:

- Python 3.x
- OpenCV
- Flask
- Haarcascade files

You can install the necessary Python packages using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository to your local machine.
2. Navigate to the `server` directory.
3. Run the Flask server:

```bash
python server.py
```
4. Open your web browser and go to http://127.0.0.1:5000.
5. Upload an image of one of the five cricketers to identify them.

## References

This project is inspired by and built with the help of tutorials from the [Codebasics YouTube channel](https://www.youtube.com/@codebasics).

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## Acknowledgements

Special thanks to the Codebasics YouTube channel for their comprehensive tutorials on building machine learning models and web applications.

## Watch a Demo

https://github.com/MihiruthS/Cricketer-Identifier/assets/166645514/b13d0a68-ad82-4715-b442-a6d8d0671f67


