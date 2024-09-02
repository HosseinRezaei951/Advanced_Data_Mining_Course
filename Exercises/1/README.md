# Sampling, Visualization, and Discretization

## Overview

This assignment focuses on key data mining tasks such as determining the number of features in a dataset, sampling a portion of the data, validating the sampling method, and discretizing the data for further analysis. These tasks are implemented in Python, with visualizations provided to support and validate the analysis.

## Project Structure

The project includes the following directories and key files:

### Directories

- **data/**: Contains the dataset used for analysis.
  - `data.csv`: The main dataset utilized in the assignment.

- **results/**: Contains the output of the analysis, including visualizations and the discretized dataset.
  - Various `.jpeg` files comparing original vs. sampled and original vs. discretized data for different features.
  - `data_disc.csv`: The discretized dataset saved after processing.

### Main Script

- **main.py**: The primary Python script that performs the following tasks:
  1. Determining the number of features.
  2. Sampling 80% of the data.
  3. Validating the sampling method through visualizations.
  4. Discretizing the data and saving the results.

## Task Details

### Feature Count (Q1)

The script identifies the number of features in the dataset by reading the CSV file and counting the columns. The total number of features (excluding the target variable) is displayed in the console.

### Data Sampling (Q2)

The script randomly samples 80% of the data without replacement, ensuring that the sample is representative of the entire dataset. The sampled data is sorted and printed to the console for review.

### Sampling Validation (Q3)

To validate the sampling method, the script generates boxplots and histograms with KDE (Kernel Density Estimation) for the last nine features in the dataset. These visualizations compare the original data distribution to the sampled data, ensuring that the sample is statistically similar to the original data.

For example, the following images show the comparison between the original and sampled data for the `ALOGP` and `MOLWEIGHT` features:

- **ALOGP (Original Vs Sample)**:
  
  ![alt text](https://github.com/HosseinRezaei951/Advanced_Data_Mining_Course/blob/main/Exercises/1/results/ALOGP%20(Original%20Vs%20Sample).jpeg)

- **MOLWEIGHT (Original Vs Sample)**:
  
  ![alt text](https://github.com/HosseinRezaei951/Advanced_Data_Mining_Course/blob/main/Exercises/1/results/MOLWEIGHT%20(Original%20Vs%20Sample).jpeg)

### Data Discretization (Q4 & Q5)

The script normalizes the sampled data, scales it, and discretizes it into bins. The discretized data is then visualized through plots comparing the original and discretized versions of the last nine features. Finally, the discretized data is saved as `data_disc.csv` in the results directory.

Below are examples of the visualizations comparing the original and discretized data for the `AROMATIC_RINGS` and `deltaG` features:

- **AROMATIC_RINGS (Original Vs Discretized)**:

  ![alt text](https://github.com/HosseinRezaei951/Advanced_Data_Mining_Course/blob/main/Exercises/1/results/AROMATIC_RINGS%20(Original%20Vs%20Discretized).jpeg)

- **deltaG (Original Vs Discretized)**:

  ![alt text](https://github.com/HosseinRezaei951/Advanced_Data_Mining_Course/blob/main/Exercises/1/results/deltaG%20(Original%20Vs%20Discretized).jpeg)

## How to Use

1. **Run the Script**:
   - Execute `main.py` to perform all tasks, from feature counting to data discretization.
   - The script will generate and save visualizations in the `results/` directory.

2. **View Results**:
   - Check the `results/` directory for `.jpeg` files comparing original, sampled, and discretized data.
   - The discretized dataset can be found in `results/data_disc.csv`.

This assignment provides practical experience with essential data mining techniques, including sampling, validation, and discretization, using Python. The visualizations offer valuable insights into the effectiveness of these methods in preparing data for subsequent analysis.