import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

base_path = os.path.join(os.path.dirname(__file__), '..')

# Load AI jobs dataset
df = pd.read_csv(os.path.join(base_path, 'ai_jobs.csv'))

# Display basic info
# print("Dataset shape:", df.shape)
# print("\nFirst few rows:")
# print(df.head())
# print("\nColumn names and types:")
# print(df.dtypes)

#===== DATA CLEANING =====

# TODO: Check for missing values - Display count of null values per column
print("\nMissing values per column:")
print(df.isnull().sum())

# TODO: Handle missing values - Drop or fill with appropriate values (mean/median/mode/forward fill)

print("\nFilling missing values...")
df['city'] = df['city'].fillna('Unknown')

# Fill experience_level with RANDOM values from available options
experience_options = ['Entry', 'Mid', 'Senior']
df['experience_level'] = df['experience_level'].apply(
    lambda x: np.random.choice(experience_options) if pd.isna(x) else x
)

# Fill company_size with RANDOM values from available options
company_options = ['Small', 'Medium', 'Large']
df['company_size'] = df['company_size'].apply(
    lambda x: np.random.choice(company_options) if pd.isna(x) else x
)

# Convert salary columns to numeric (fixes string values like '56873.0.0')
df['salary_min_usd'] = pd.to_numeric(df['salary_min_usd'], errors='coerce')
df['salary_max_usd'] = pd.to_numeric(df['salary_max_usd'], errors='coerce')

# Now fill with median
df['salary_min_usd'] = df['salary_min_usd'].fillna(df['salary_min_usd'].median())
df['salary_max_usd'] = df['salary_max_usd'].fillna(df['salary_max_usd'].median())

print("\nMissing values after filling:")
print(df.isnull().sum())

count = len(df)
print(f"\nTotal records after filling missing values: {count}")

# TODO: Remove duplicate rows - Check and remove any duplicate entries
print("\nRemoving duplicates...")
df = df.drop_duplicates()
print("Total records after removing duplicates:", len(df))

# TODO: Standardize text columns if issues found above - Convert to lowercase, strip whitespace, fix inconsistencies
# Uncomment below if standardization is needed:
df['city'] = df['city'].str.strip().str.title()
df['job_title'] = df['job_title'].str.strip().str.upper()
df['country'] = df['country'].str.strip().str.title()
# df['company_name'] = df['company_name'].str.strip().str.title()

# # Check if text standardization is needed
# print("\n=== Checking for text inconsistencies ===")

# # Get text columns that actually exist in your dataframe
# possible_text_columns = ['city', 'job_title', 'country', 'company_name', 'location', 'company']
# text_columns = [col for col in possible_text_columns if col in df.columns]

# print(f"\nText columns found: {text_columns}")

# # Check for leading/trailing whitespace
# for col in text_columns:
#     spaces_count = df[col].astype(str).str.strip().ne(df[col].astype(str)).sum()
#     if spaces_count > 0:
#         print(f"'{col}': {spaces_count} values with leading/trailing spaces")

# # Display unique values to check for inconsistencies
# for col in text_columns:
#     print(f"\nUnique {col} (top 20):")
#     print(df[col].value_counts().head(20))

# TODO: Convert data types - Ensure salary is numeric, dates are datetime, categories are proper type

print("\nConverting data types...")
print("Before conversion:")
print(df.dtypes)

df['posted_year'] = pd.to_numeric(df['posted_year'], errors='coerce')
df['country'] = df['country'].astype('category')
df['experience_level'] = df['experience_level'].astype('category')
df['company_size'] = df['company_size'].astype('category')

# df['salary_min_usd'] = pd.to_numeric(df['salary_min_usd'], errors='coerce')
# df['salary_max_usd'] = pd.to_numeric(df['salary_max_usd'], errors='coerce')
print("\nAfter conversion:")
print(df.dtypes)

# TODO: Handle outliers in salary - Detect using IQR or z-scores, remove or cap extreme values
Q1 = df['salary_min_usd'].quantile(0.25)  # 25th percentile
Q3 = df['salary_min_usd'].quantile(0.75)  # 75th percentile
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['salary_min_usd'] < lower_bound) | (df['salary_min_usd'] > upper_bound)]
print(f"\nFound {len(outliers)} outliers")
print(f"Lower bound: ${lower_bound:.2f}")
print(f"Upper bound: ${upper_bound:.2f}")
# TODO: Fix inconsistent job titles - Standardize similar job titles (e.g., "ML Engineer" = "Machine Learning Engineer")
print("\nBefore standardizing job titles:")
print(df['job_title'].value_counts().head(1000))
title_mapping = {
    'ML ENGINEER': 'MACHINE LEARNING ENGINEER',
    'ML ENG': 'MACHINE LEARNING ENGINEER',
    'MACHINE LEARNING ENG': 'MACHINE LEARNING ENGINEER',
}

df['job_title'] = df['job_title'].replace(title_mapping)
print("\nAfter standardizing job titles:")
print(df['job_title'].value_counts().head(1000))
#===== DATA ANALYSIS =====

# TODO: Descriptive statistics - Get mean, median, std, min, max for numerical columns (salary, experience, etc.)

# TODO: Group by job title - Calculate average salary, count of jobs per title

# TODO: Group by country - Analyze job distribution and average salaries by country

# TODO: Correlation analysis - Find correlations between salary, experience, and other numeric variables

# TODO: Top 10 highest paying job titles - Sort and display top jobs by salary

# TODO: Top 10 countries with most AI jobs - Count jobs per country

# TODO: Salary distribution analysis - Analyze salary ranges, quartiles, percentiles

# TODO: Experience level analysis - Group by experience level (Junior/Mid/Senior) if column exists

# TODO: Filter analysis - Create subsets for specific job types, salary ranges, or countries

