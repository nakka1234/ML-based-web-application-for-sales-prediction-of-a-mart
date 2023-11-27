# Sales Prediction Web Application

This project is a dynamic web application utilizing Machine Learning for sales prediction, empowering businesses to make data-driven decisions.

## Overview

- **Tools/Tech**: Machine Learning, Python, HTML, CSS, jQuery.
- **Objective**: Develop a web application to predict sales trends for products using Machine Learning techniques.

## Features

- **Predictive Model**: Utilizes a robust Random Forest Algorithm to predict product sales based on influential features.
- **Data Processing**: Implements feature scaling to standardize input data for accurate predictions.
- **Hyperparameter Tuning**: Optimizes model performance via hyperparameter tuning and cross-validation to mitigate overfitting.
- **Web Interface**: Provides an intuitive interface for users to input data and receive predicted sales results.

## Requirements

- Python 3.x
- Flask
- joblib
- numpy

## Usage

1. **Setup:**

    - Install Python 3.x.
    - Install required libraries using pip:
        ```bash
        pip install Flask joblib numpy
        ```

2. **Run the Application:**

    - Execute the Flask application by running the provided script.
    - Access the web application through a browser at the specified port (default: http://localhost:9457).

3. **Using the Application:**

    - Input product details (Item Weight, Item Type, etc.) in the provided fields.
    - Submit the form to receive the predicted sales for the entered product.

## File Structure

- `app.py`: Flask application script handling model prediction and web interactions.
- `model/`: Directory containing ML model files (`sc.sav` for scaler and `grid_search.sav` for the predictive model).

## Acknowledgments

- The application uses Machine Learning techniques for sales prediction.
- Flask framework for building the web application.

Feel free to explore, modify, and extend the application as needed!

