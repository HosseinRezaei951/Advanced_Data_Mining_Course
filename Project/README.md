# Predicting DeltaG Values Using Random Forest Regression

## Project Overview

This project is centered on predicting DeltaG values using a regression approach. The main goal is to forecast the values in the final column of a given dataset, emphasizing accurate error reporting. The project is implemented in Python and executed on Google Colab, utilizing the Random Forest algorithm for regression tasks.

## Problem Definition

The task involves predicting the continuous values of the last column (DeltaG) in the dataset, making it a regression problem. Two approaches were considered:

1. **Discretization Approach**:
   - Discretizing the DeltaG values into suitable intervals and using classification algorithms for prediction. The error is reported as a continuous value (sum of squared errors).

2. **Direct Regression Approach**:
   - Directly using a regression algorithm to predict the DeltaG values.

### Approach Used

For this project, the Random Forest regression algorithm was chosen due to its flexibility and strong performance in regression tasks. The following outlines the approach used:

1. **Algorithm Selection**:
   - Random Forest was selected for its robustness in handling high-dimensional data and providing accurate predictions without extensive tuning.

2. **Algorithm Overview**:
   - **Random Forest** is an ensemble learning algorithm that constructs multiple decision trees and aggregates their predictions. It is known for its accuracy and capability to handle large datasets with numerous features.

3. **Preprocessing**:
   - The dataset (`DM_data.csv`) was uploaded to Google Drive and read into a pandas DataFrame. Key preprocessing steps included:
     - Removing the first column (a string type), which was not required for calculations.
     - Converting all column data types to `float64` for consistency.
     - Checking for missing values, with none found in the dataset.

4. **Feature and Label Selection**:
   - The data was split into features (all columns except the last one) and labels (the last column, `deltaG`).

5. **Data Splitting**:
   - The dataset was divided into training (70%) and testing (30%) sets using `train_test_split` from `sklearn`.

6. **Model Training**:
   - A Random Forest Regressor was trained on the training set with the following key hyperparameters:
     - `n_estimators = 1000`: Number of trees in the forest.
     - `n_jobs = 10`: Number of processors to use.

7. **Model Evaluation**:
   - The model's performance was evaluated on the test set, with the following metrics:
     - **Mean Absolute Error (MAE)**
     - **Mean Squared Error (MSE)**
     - **Accuracy**: The model achieved an accuracy of 88.35%, indicating a strong predictive performance.

## How to Run the Project

1. **Google Colab Setup**:
   - Upload the `DM_data.csv` dataset to Google Drive.
   - Open the `Final_Project.ipynb` notebook in Google Colab.
   - Run the cells in sequence to execute the code.

2. **Dependencies**:
   - Ensure the following Python libraries are installed:
     - `pandas`
     - `numpy`
     - `sklearn`
     - `matplotlib`
   - These can be installed via pip if necessary.

3. **Data Loading**:
   - Load the dataset from Google Drive into a pandas DataFrame as shown in the notebook.

4. **Model Training and Evaluation**:
   - Follow the steps in the notebook to train the Random Forest Regressor on the training data and evaluate its performance on the test data.

5. **Results**:
   - The notebook outputs performance metrics such as MAE, MSE, and accuracy, providing insights into the model's effectiveness.

## Conclusion

This project successfully demonstrates the use of Random Forest regression to predict DeltaG values. The model's high accuracy and low error metrics underscore the effectiveness of this approach for regression tasks. Further exploration could involve experimenting with different algorithms or fine-tuning the Random Forest hyperparameters to enhance performance.
