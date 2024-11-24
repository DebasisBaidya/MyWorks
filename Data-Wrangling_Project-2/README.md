# Project 2: Data Preprocessing & Exploratory Analysis

## Step-by-Step Process

### Step 1: Importing of Libraries
Began by importing the necessary Python libraries:
- **Pandas** for data manipulation.
- **NumPy** for numerical operations.
- **Matplotlib** and **Seaborn** for data visualization.
- **Scikit-learn** for machine learning preprocessing tools.

### Step 2: Loading of Datasets
Loaded the datasets from CSV files using Pandas. Previewed the data by displaying:
- The first few rows (head).
- The last few rows (tail).
- The shape, column names, and data types, describe.

### Step 3: Analyzing Datasets
Examined the structure of each dataset:
- Checked for null values and unique value counts.
- Computed basic descriptive statistics (mean, median, mode) for numerical columns.

### Step 4: Handling Missing Values
Utilized Scikit-learn's `SimpleImputer` to fill in missing values:
- For numerical columns, used the mean.
- For categorical columns, used the mode.

### Step 5: Data Type Identification
Determined and set appropriate data types for each column to ensure proper analysis.

### Step 6: Dropping Unwanted Columns
Removed any unnecessary columns that do not contribute to the analysis.

### Step 7: Merging of Datasets
Combined the cleaned datasets into a single merged dataset. Ensured alignment based on shared features or key variables.

### Step 8: Skewness and Outlier Analysis
- Assessed the skewness of numerical columns to understand data distribution.
- Identified and handled outliers using the interquartile range (IQR) method.

### Step 9: Correlation Visualization
Generated a correlation matrix to visualize relationships between different variables in the final dataset.

## Conclusion
This step-by-step guide provides an overview of the data preprocessing and exploratory analysis conducted in this project.
