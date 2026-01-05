import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

base_path = os.path.dirname(__file__)

# Load cleaned dataset
df = pd.read_csv(os.path.join(base_path, 'ai_jobs_cleaned.csv'))

# Create average salary column
df['salary_avg_usd'] = (df['salary_min_usd'] + df['salary_max_usd']) / 2

print("="*60)
print("AI JOBS DATA VISUALIZATIONS")
print("="*60)
print(f"\nDataset loaded: {len(df)} records\n")

#===== VISUALIZATIONS =====

# TODO: Salary distribution histogram

# TODO: Top 10 job titles bar chart

# TODO: Top 10 countries bar chart

# TODO: Experience level distribution pie chart

# TODO: Salary by experience level box plot

# TODO: Salary by country (top 10) box plot

# TODO: Scatter plot - salary vs year (if applicable)

# TODO: Heatmap - correlation matrix
