import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

base_path = os.path.dirname(__file__)

# Load cleaned dataset
df = pd.read_csv(os.path.join(base_path, 'ai_jobs_cleaned.csv'))

# print("="*60)
# print("AI JOBS DATA ANALYSIS")
# print("="*60)
# print(f"\nDataset shape: {df.shape}")
# print(f"Total records: {len(df)}")

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

#===== VISUALIZATIONS =====

# TODO: Create visualizations for your analysis here
