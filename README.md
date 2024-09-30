# OCR and Document Search Web Application

This is a web-based prototype application that performs Optical Character Recognition (OCR) on uploaded images containing text in both Hindi and English. The application allows users to search for specific keywords within the extracted text.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Deployment](#deployment)
6. [Example Outputs](#example-outputs)
7. [License](#license)

## Introduction

The OCR and Document Search Web Application uses Tesseract OCR to extract text from images and provides a keyword search functionality. The application is designed to be user-friendly and accessible.

## Features

- Upload an image file (JPEG, PNG, etc.) for OCR processing.
- Extract text from the uploaded image in both Hindi and English.
- Enter keywords to search within the extracted text.
- Highlight matching sections in the extracted text.
- Deployable on Hugging Face Spaces.

## Installation

To run this application locally, you will need to set up a Python environment and install the necessary libraries. Follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   
2. Create a virtual environment (optional):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`


3. Install the required libraries:
      ```bash
      pip install -r requirements.txt


4. Install Tesseract OCR and language packs:
    For installation instructions, visit the Tesseract OCR GitHub page.
   
## Usage
1. Run the application:
    ```bash
    python main.py

2. Open your web browser and navigate to the URL provided in the terminal.

3. Upload an image containing Hindi or English text.

4. Click "Submit" to process the image and extract text.

5. Enter a keyword to search within the extracted text and view the results.

## Deployment
The web application is deployed on Hugging Face Spaces. You can access it via the following link: Live Web Application

## Example Outputs
Extracted Text: The application will display the extracted text in a text box.
Search Functionality: You can test the search functionality by entering keywords and viewing highlighted results.
