# ECG Image Classification App 🫀

Welcome to the ECG Image Classification App! This project is a deep learning case study inspired by clinical ECG research. It implements and compares various neural network models, including ANN, CNN, and VGG-19, on ECG image data. The app provides real-time predictions, all deployed using Streamlit.

[![Download Releases](https://img.shields.io/badge/Download%20Releases-Here-brightgreen)](https://github.com/Vaibhavp2129/ECG-Image-Classification-App/releases)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Data Preprocessing](#data-preprocessing)
- [Real-time Predictions](#real-time-predictions)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

Electrocardiograms (ECGs) are vital for diagnosing heart conditions. This app aims to classify ECG images effectively, utilizing deep learning techniques. By comparing different models, we can identify the most efficient approach for ECG image classification.

## Features

- **Multiple Model Implementations**: Compare ANN, CNN, and VGG-19.
- **Real-time Predictions**: Get instant results using Streamlit.
- **User-friendly Interface**: Simple and intuitive design.
- **Image Preprocessing**: Essential steps to enhance model performance.
- **Comprehensive Documentation**: Easy to follow instructions for setup and usage.

## Technologies Used

- **Deep Learning Frameworks**: Keras, TensorFlow
- **Programming Language**: Python 3
- **Streamlit**: For deploying the web app
- **Image Processing**: OpenCV, PIL
- **Data Augmentation**: SMOTE for balancing the dataset
- **Computer Vision**: Techniques for image analysis

## Installation

To get started, clone the repository and install the necessary packages.

1. Clone the repository:

   ```bash
   git clone https://github.com/Vaibhavp2129/ECG-Image-Classification-App.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ECG-Image-Classification-App
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

After installation, you can run the app using the following command:

```bash
streamlit run app.py
```

This will launch the app in your default web browser. Follow the instructions on the interface to upload ECG images and receive predictions.

## Models

### Artificial Neural Network (ANN)

The ANN model is a foundational approach in deep learning. It consists of multiple layers of neurons, which learn from the input data to make predictions.

### Convolutional Neural Network (CNN)

CNNs are particularly effective for image data. They use convolutional layers to automatically extract features from images, which improves classification accuracy.

### VGG-19

VGG-19 is a deep learning model known for its depth and performance. It has 19 layers and is effective for complex image classification tasks.

## Data Preprocessing

Data preprocessing is crucial for enhancing model performance. The following steps are included:

1. **Image Resizing**: Standardize image dimensions.
2. **Normalization**: Scale pixel values to a range of 0-1.
3. **Data Augmentation**: Apply techniques like rotation, flipping, and zooming to increase dataset variability.
4. **Balancing the Dataset**: Use SMOTE to address class imbalances.

## Real-time Predictions

The app provides real-time predictions for uploaded ECG images. Simply upload an image, and the model will analyze it and return the predicted class. This feature is powered by Streamlit, ensuring a seamless user experience.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to create a pull request or open an issue. Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature.
3. Make your changes and commit them.
4. Push to your branch.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

We thank the contributors and researchers in the field of ECG analysis. Your work inspires projects like this one. Special thanks to the developers of the libraries used in this project, which make deep learning accessible and effective.

For further details, you can check the [Releases section](https://github.com/Vaibhavp2129/ECG-Image-Classification-App/releases) for updates and downloads.