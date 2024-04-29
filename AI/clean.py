import pandas as pd
from bs4 import BeautifulSoup
import re

# Load the CSV file
df = pd.read_csv('.venv/archive/steam.csv', delimiter=',')  # Assuming comma-separated data, adjust delimiter if necessary

# Apply strip and lowercase operations on each column
for column in df.columns:
    if df[column].dtype == 'object':  # Check if the column contains textual data
        df[column] = df[column].str.strip()  # Remove leading and trailing whitespace
        df[column] = df[column].str.lower()  # Convert text to lowercase

# Additional cleaning steps
# Remove HTML tags from specific columns
for column in df.columns:
    df[column] = df[column].apply(lambda x: BeautifulSoup(x, 'html.parser').get_text() if isinstance(x, str) else x)

# Remove special characters from specific columns
for column in ['name', 'developer', 'publisher']:
    df[column] = df[column].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x) if isinstance(x, str) else x)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Drop rows with missing values if needed
# df.dropna(inplace=True)

# Convert release_date column to datetime format
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Extract year from the release_date and create a new column
df['release_year'] = df['release_date'].dt.year

# Save the cleaned DataFrame to a new CSV file
cleaned_file_path = 'steam_cleaned.csv'
df.to_csv(cleaned_file_path, index=False)

print("DataFrame after additional cleaning steps:\n", df.head())
print("Cleaned data saved to:", cleaned_file_path)


