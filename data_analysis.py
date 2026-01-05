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

# TODO: Descriptive statistics - Get mean, median, std, min, max for numerical columns (salary, etc.)

# Create average salary column
df['salary_avg_usd'] = (df['salary_min_usd'] + df['salary_max_usd']) / 2

# Get all statistics at once
print("\nSalary Statistics (USD):")
print(df[['salary_min_usd', 'salary_max_usd', 'salary_avg_usd']].describe())

print("\nYear Statistics:")
print(df['posted_year'].describe())

print("\nExperience Level Distribution:")
print(df['experience_level'].value_counts())
print("\nPercentages:")
print(df['experience_level'].value_counts(normalize=True) * 100)

# TODO: Group by job title - Calculate average salary, count of jobs per title
grouped_by_title = df.groupby('job_title').agg(
    avg_salary_mean = ('salary_avg_usd', 'mean'),
    job_count = ('job_title', 'count')
)
print("\nTop 10 Job Titles by Average Salary:")
print(grouped_by_title.sort_values(by='avg_salary_mean', ascending=False).head(10))
# TODO: Group by country - Analyze job distribution and average salaries by country
grouped_by_country = df.groupby('country').agg(
    avg_salary_mean = ('salary_avg_usd', 'mean'),
    job_count = ('job_title', 'count')
)
print("\nTop 10 Countries by Average Salary:")
print(grouped_by_country.sort_values(by='avg_salary_mean', ascending=False).head(10))
# TODO: Correlation analysis - Find correlations between salary, experience, and other numeric variables

correlation_value = df['salary_avg_usd'].corr(
    df['experience_level'].map({'Entry':1, 'Mid':2, 'Senior':3})
)
print(f"\nCorrelation between Average Salary and Experience Level: {correlation_value:.4f}")
# TODO: Top 10 highest paying job titles - Sort and display top jobs by salary

highest_paying_jobs = df.groupby('job_title')['salary_max_usd'].mean().sort_values(ascending=False).head(10)
print("\nTop 10 Highest Paying Job Titles:")
print(highest_paying_jobs)
# TODO: Top 10 countries with most AI jobs - Count jobs per country
top_countries = df['country'].value_counts().head(10)
print("\nTop 10 Countries with Most AI Jobs:")
print(top_countries)
# TODO: Salary distribution analysis - Analyze salary quartiles, percentiles
print("\nSalary quartiles (USD):")
Q1 = df['salary_avg_usd'].quantile(0.25)
Q2 = df['salary_avg_usd'].quantile(0.50)
Q3 = df['salary_avg_usd'].quantile(0.75)
print(f"25th Percentile (Q1): {Q1:.2f}")
print(f"50th Percentile (Median, Q2): {Q2:.2f}")
print(f"75th Percentile (Q3): {Q3:.2f}") 

print("\nSalary percentiles (USD):")
salary_percentiles = df['salary_avg_usd'].describe(percentiles=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
print(salary_percentiles)

# TODO: Experience level analysis - Group by experience level (Junior/Mid/Senior) if column exists

exp_level_group = df.groupby('experience_level').agg(
    avg_salary_mean = ('salary_avg_usd', 'mean'),
    job_count = ('job_title', 'count')
)
print("\nExperience Level Analysis:")
print(exp_level_group)
# TODO: Filter analysis - Create subsets for specific job types, salary ranges, or countries
jobs_in_canada = df['country'] == 'Canada'
canada_jobs = df[jobs_in_canada]
print(f"\nTotal AI jobs in Canada: {len(canada_jobs)}")
jobs_distribution_canada = canada_jobs['job_title'].value_counts()
print("\nJob distribution in Canada:")
print(jobs_distribution_canada)
average_salary_canada = canada_jobs['salary_avg_usd'].mean()
print(f"\nAverage salary for AI jobs in Canada: ${average_salary_canada:.2f}")
print(f"\n[SUCCESS] Data analysis complete!")