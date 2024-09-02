# Market Basket Analysis and MDX Query Language

## Overview
This assignment focuses on analyzing market basket data using WEKA software to extract frequent itemsets and generate association rules. Additionally, an optional task explores MDX query language, commonly used in OLAP databases. The main tasks involve data preprocessing, performing analysis in WEKA, and interpreting the results.

## Project Structure
The project includes the following directories and files:

### Directories
- **data/**: Contains the original dataset used for analysis.
  - `market_basket_dataset.csv`: The dataset containing 1000 transactions with 40 items.
- **results/**: Contains the output of preprocessing and WEKA analysis.
  - `new_data.csv`: The transformed dataset, ready for analysis in WEKA.
  - `Apriori(0.3).txt`: Output from WEKA using the Apriori algorithm with a confidence-based evaluation.
  - `Apriori(0.3)_liftBase.txt`: Output from WEKA using the Apriori algorithm with a lift-based evaluation.
  
### Main Script
- **main.py**: Python script that preprocesses the dataset to make it compatible with WEKA.

## Task Breakdown

### Question 1: Market Basket Analysis with WEKA

#### 1.1 Problem Definition
The task involves analyzing the `market_basket_dataset.csv` dataset using WEKA to extract frequent itemsets with a minimum support of 0.3. The problem is divided into several steps:

1. **Data Preprocessing**: 
   - The original dataset needs to be transformed into a format suitable for WEKA. This is done by creating binary columns for each of the 40 items, indicating whether each item is present in a transaction.

2. **Frequent Itemset Extraction**:
   - Use WEKA's Apriori algorithm to extract frequent itemsets with a minimum support of 0.3.

3. **Evaluation of Frequent Itemsets**:
   - Analyze and explain the evaluation metrics for the extracted frequent itemsets.

4. **Association Rule Mining**:
   - Generate association rules from the frequent itemsets and evaluate these rules.

#### 1.2 Implementation Details
The `main.py` script performs the following steps:

- **Data Loading**: The script reads the `market_basket_dataset.csv` file using the `pandas` library.
- **Data Transformation**:
  - For each item (from 1 to 40), the script checks each transaction to determine if the item is present. It then creates a new column for each item, where each cell is marked as "Yes" if the item is present and "No" if it is absent.
  - The original `transactions` column is dropped, and the resulting dataset is saved as `new_data.csv` in the `results/` directory.

#### 1.3 Using WEKA for Analysis

1. **Load the Data**:
   - Open WEKA and load `new_data.csv` in

the Explorer interface.

2. **Set Up the Apriori Algorithm**:
   - In the Associate tab, select the Apriori algorithm.
   - Configure the algorithm as follows:
     - **Minimum Support**: Set to 0.3.
     - **Metric Type**: Choose `confidence` for the first analysis (`Apriori(0.3).txt`) and `lift` for the second analysis (`Apriori(0.3)_liftBase.txt`).
     - **Minimum Confidence**: Set to 0.9 for the confidence-based analysis.
     - **Minimum Lift**: Set to 1.1 for the lift-based analysis.

3. **Run the Analysis**:
   - Execute the Apriori algorithm and examine the output. The results will include frequent itemsets and association rules.
   - Save the output as `Apriori(0.3).txt` for confidence-based analysis and `Apriori(0.3)_liftBase.txt` for lift-based analysis.

4. **Evaluation**:
   - The rules are evaluated based on their confidence and lift values. Confidence indicates the likelihood that the consequent occurs given the antecedent, while lift measures the strength of a rule over the baseline probability of the consequent.

#### 1.4 Example Results

From the `Apriori(0.3).txt` file:

- **Frequent Itemsets**:
  - Example: `{item26=No, item28=No} : support = 0.85`

- **Association Rules**:
  - Example Rule: `{item26=No, item28=No} => {item23=No} (confidence: 0.99, lift: 1.00)`

From the `Apriori(0.3)_liftBase.txt` file:

- **Frequent Itemsets**:
  - Example: `{item11=No, item22=No, item39=No} : support = 0.74`

- **Association Rules**:
  - Example Rule: `{item11=No, item22=No, item39=No} => {item23=No} (confidence: 0.84, lift: 1.13)`

These results highlight the most significant associations within the dataset, allowing for a deeper understanding of the relationships between items in the transactions.

### Question 2: Optional - Understanding MDX

#### 2.1 Problem Definition
The optional task involves defining MDX (Multidimensional Expressions) and providing an example query to illustrate its application.

#### 2.2 Explanation
MDX is a query language for OLAP databases, similar to SQL but specifically designed to interact with multidimensional data structures known as OLAP cubes. MDX supports various data types, including scalars, dimensions, hierarchies, and tuples.

#### 2.3 Example Query
An MDX query example might look like this:

```mdx
SELECT 
  {[Measures].[Store Sales]} ON COLUMNS, 
  {[Time].[2002], [Time].[2003]} ON ROWS 
FROM [Sales]
WHERE ([Store].[USA].[CA])
```

This query retrieves sales data for stores in California during the years 2002 and 2003.

## How to Use

1. **Run the Script**:
   - Execute `main.py` to preprocess the dataset.
   - The transformed data will be saved in the `results/` directory.

2. **Load Data into WEKA**:
   - Open WEKA and load the `new_data.csv` file.
   - Use the Apriori algorithm with the specified settings to perform the analysis.

3. **Evaluate and Interpret Results**:
   - Analyze the output for frequent itemsets and association rules.
   - Save and document your findings for future reference.

4. **Optional Task**:
   - Study the MDX query language and practice writing queries using an OLAP database.

## Conclusion
This assignment demonstrates the application of data mining techniques, specifically market basket analysis, using WEKA. Additionally, it provides an introduction to the MDX query language, a powerful tool for multidimensional data analysis. For further details and results, refer to the files in the `results/` directory.
