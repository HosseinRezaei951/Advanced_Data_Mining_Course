# Advanced Data Mining Course

Welcome to the Advanced Data Mining Course repository. This collection includes a series of exercises and a final project focused on various data mining techniques. The materials in this course will guide you through essential methods such as data preprocessing, association rule learning, regression, and model evaluation. The course is structured to provide hands-on experience with Python scripts and datasets, facilitating practical learning and application of data mining concepts.

## Directory Structure

### Exercises

The `Exercises` directory is divided into subdirectories, each focusing on different data mining tasks.

#### Exercise 1: Data Discretization and Visualization

This exercise involves discretizing continuous data and visualizing the effects of discretization on various features:

- **Data Directory**:
  - Contains the dataset used for the exercise.

- **Results Directory**:
  - Includes images comparing the original and discretized data, as well as the original and sampled data for features like ALOGP, deltaG, HBA, and more.
  - The discretized dataset (`data_disc.csv`) is also stored here.

- **Scripts**:
  - **main.py**: Script to perform the discretization and generate visualizations.

#### Exercise 2: Association Rule Learning with Apriori

This exercise focuses on implementing the Apriori algorithm to discover association rules from a market basket dataset:

- **Data Directory**:
  - Contains the market basket dataset used for association rule mining.

- **Results Directory**:
  - Contains text files with the results of the Apriori algorithm, including rule sets generated with different support thresholds and lift criteria.
  - A modified version of the dataset (`new_data.csv`) is also included.

- **Scripts**:
  - **main.py**: Script to execute the Apriori algorithm and generate association rules.

### Project: DeltaG Value Prediction with Random Forest

The project applies the Random Forest regression algorithm to predict DeltaG values for a given dataset:

- **Final_Project.ipynb**: Jupyter notebook that walks through the steps of data preprocessing, model training, and evaluation using Random Forest regression.
- **README.md**: Provides an overview of the project, explaining the approach and summarizing the results.

## How to Use

### Running the Scripts and Notebooks

1. **Exercise 1 (Data Discretization and Visualization)**:
   - Navigate to the `1` subdirectory under `Exercises` and run `main.py` to discretize the data and generate visual comparisons.

2. **Exercise 2 (Association Rule Learning with Apriori)**:
   - Navigate to the `2` subdirectory under `Exercises` and execute `main.py` to perform association rule mining on the market basket data.

3. **Final Project (DeltaG Value Prediction with Random Forest)**:
   - Open and run `Final_Project.ipynb` in Jupyter Notebook or Google Colab to follow the regression analysis workflow.

## Conclusion

This course provides a comprehensive introduction to essential data mining techniques, including data discretization, association rule learning, and regression analysis. Through practical exercises and a final project, you will gain hands-on experience and a deeper understanding of data mining concepts. Feel free to explore and modify the scripts to enhance your learning and apply these techniques to different datasets.
