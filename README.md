# Project Overview

This project is an application to predict image class (cat or dog) using a fine-tuned VGG16 model. The model is served over the web via Python Flask.

# Features

*   Image classification for cats and dogs.
*   Web interface for uploading images and viewing predictions.
*   Flask backend serving the Keras model.

# How it Works

The project follows these general steps:

1.  **Data Input:** The frontend (`static/index.html`) allows users to upload an image.
2.  **Image Transmission:** The selected image is base64 encoded and sent to the `/predict` endpoint of the Flask application (`predict.py`).
3.  **Backend Processing:** The Flask application decodes the image, preprocesses it (resizes to 224x224, converts to RGB, and converts to a numpy array).
4.  **Model Inference:** The preprocessed image is fed to the loaded Keras model (`VGG16_cats_and_dogs.h5`).
5.  **Output Generation:** The model predicts the probability of the image being a dog or a cat. The predictions are returned as a JSON response to the frontend and displayed.

# Setup and Installation

To get the project running locally, follow these steps:

1.  **Navigate to Project Directory:**
    Ensure you are in the root directory of the project (where files like `predict.py` are located).
    If you've just cloned the repository, navigate into it:
    ```bash
    # Example: cd your-project-directory-name
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Python Dependencies:**
    The required Python libraries are listed in `requirements.txt`. Install them using pip:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Obtain the H5 Model File:**
    **IMPORTANT:** This project requires a pre-trained H5 model file named `VGG16_cats_and_dogs.h5`. This file is **not included** in the repository, typically due to its size.
    *   You need to obtain this file yourself. It might be available from a separate download link provided by the project maintainers, or you might need to train it using a separate script (if provided).
    *   Once obtained, place the `VGG16_cats_and_dogs.h5` file in the **root directory** of the project (the same directory where `predict.py` is located).

# Running the Project

Once the setup and installation are complete, including placing the `VGG16_cats_and_dogs.h5` file in the root directory:

1.  **Run the Flask Application:**
    Open your terminal, navigate to the project's root directory, and execute:
    ```bash
    python predict.py
    ```
    This will typically start a development server (e.g., on `http://localhost:5000` or `http://127.0.0.1:5000`).

2.  **Access the Web Interface:**
    Open your web browser and navigate to the `static/index.html` file directly. Alternatively, if the Flask app is configured to serve static files from the root, you might be able to access it via `http://localhost:5000`.

# Usage

1.  Launch the application as described in "Running the Project". Ensure the Flask server (`predict.py`) is running.
2.  Open `static/index.html` in your web browser.
3.  Click the "Choose File" button to select an image (e.g., a `.jpg` or `.png` file of a cat or a dog).
4.  The selected image will be displayed on the page.
5.  Click the "Predict" button.
6.  The predicted probabilities for "Dog" and "Cat" will be displayed below the button (e.g., "Dog: 0.98, Cat: 0.02").

# Potential Bugs/Troubleshooting

*   **`ModuleNotFoundError`:** Ensure you have activated your virtual environment (`source venv/bin/activate`) and successfully installed all dependencies using `pip install -r requirements.txt`.
*   **`FileNotFoundError: VGG16_cats_and_dogs.h5`:** This is a critical error. Confirm that the `VGG16_cats_and_dogs.h5` file is present in the root directory of the project, alongside `predict.py`. If not, you must obtain it and place it there.
*   **Issues with `pip install`:** If you encounter errors during dependency installation, check for version conflicts or missing system libraries. Sometimes, specific versions in `requirements.txt` might need adjustments based on your OS or Python version.
*   **Flask Server Not Running:** If the webpage loads but predictions fail, ensure the `python predict.py` command is still running in your terminal and hasn't crashed.
*   **JavaScript Errors:** Open your browser's developer console (usually by pressing F12). Look for errors in the "Console" tab. This can happen if the backend at `http://localhost:5000/predict` is not reachable or returns an unexpected response format.
*   **Image Format/Corruption:** Ensure the image you are trying to upload is a valid, uncorrupted image file (e.g., JPG, PNG).

If you encounter other issues, please check the project's issue tracker (if available) or consider opening a new issue with detailed information, including error messages and steps to reproduce.

# Contributing (Optional)

We welcome contributions to improve this project! If you'd like to contribute, please follow these general guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix (`git checkout -b feature/your-feature-name` or `bugfix/your-bug-fix`).
3.  Make your changes and commit them with clear and descriptive messages.
4.  Ensure your code adheres to the project's coding style (if any).
5.  Write or update tests for your changes.
6.  Push your changes to your forked repository.
7.  Create a pull request to the main project repository.

---
This project is currently not licensed.
