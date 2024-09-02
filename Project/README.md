# Predicting DeltaG Values Using Random Forest Regression

## Project Overview

This project focuses on predicting the values of the last column in a given dataset using a regression approach. The primary objective is to forecast DeltaG values, emphasizing the importance of proper error reporting methods. The project was developed using Python and executed on Google Colab, leveraging the Random Forest algorithm for regression.

## Problem Definition

The task involves predicting the values of the final column in the dataset. The challenge lies in accurately predicting DeltaG values rather than discrete labels, making it a regression problem rather than a classification one. Two approaches were considered for this problem:

1. **Discretization Approach**:
   - The target DeltaG values can be discretized into suitable intervals, and classification algorithms can be employed for prediction. Despite using classification, the error is still reported as a DeltaG value (sum of squared errors).

2. **Direct Regression Approach**:
   - Use a regression algorithm directly to predict DeltaG values.

### Approach Used

For this project, the Random Forest regression algorithm was chosen due to its versatility and ease of use. Random Forest can be employed for both classification and regression tasks. The following steps outline the approach used:

1. **Algorithm Selection**:
   - Random Forest was selected for its ability to handle high-dimensional data and its robustness in providing accurate predictions without extensive tuning.

2. **Algorithm Overview**:
   - **Random Forest** is a powerful machine learning algorithm that builds multiple decision trees during training and outputs the average prediction of the individual trees. The algorithm is known for its high accuracy and ability to handle large datasets with many features.

3. **Preprocessing**:
   - The dataset was first uploaded to Google Drive and then read into a pandas DataFrame. Initial preprocessing included:
     - Removing the first column (string type), as it was not necessary for calculations.
     - Converting the data types of all columns to `float64` to ensure consistency in calculations.
     - Checking for and handling any missing values (although none were found in this dataset).

4. **Feature and Label Selection**:
   - The data was split into features (all columns except the last one) and labels (the last column, `deltaG`).

5. **Data Splitting**:
   - The data was split into training and testing sets with a ratio of 70% for training and 30% for testing using the `train_test_split` function from `sklearn`.

6. **Model Training**:
   - A Random Forest Regressor model was trained using the training set. Key hyperparameters included:
     - `n_estimators = 1000`: The number of trees in the forest.
     - `n_jobs = 10`: The number of processors to use.

7. **Model Evaluation**:
   - The model was evaluated on the test set, and the following metrics were reported:
     - **Mean Absolute Error (MAE)**
     - **Mean Squared Error (MSE)**
     - **Accuracy**: The model achieved an accuracy of 88.35%, indicating a high level of performance.

## How to Run the Project

1. **Google Colab Setup**:
   - Upload the dataset to Google Drive.
   - Open the `Final_Project.ipynb` notebook in Google Colab.
   - Run the notebook cells sequentially to execute the code.

2. **Dependencies**:
   - The project requires the following Python libraries:
     - `pandas`
     - `numpy`
     - `sklearn`
     - `matplotlib`
   - These can be installed using pip if not already available in the environment.

3. **Data Loading**:
   - Load the dataset from Google Drive into a pandas DataFrame.

4. **Model Training and Evaluation**:
   - Follow the steps outlined in the notebook to train the Random Forest Regressor on the training data and evaluate its performance on the test data.

5. **Results**:
   - The notebook will output the performance metrics, including MAE, MSE, and accuracy, providing insights into the model's predictive capabilities.

## Conclusion

This project demonstrates the application of the Random Forest regression algorithm to predict DeltaG values in a dataset. The model's performance, with a high accuracy and low error metrics, shows the effectiveness of this approach in handling regression tasks. For further exploration, one could experiment with different algorithms or tune the hyperparameters of the Random Forest model to optimize performance.
