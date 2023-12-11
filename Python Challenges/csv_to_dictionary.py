import pandas as pd

# opening the CSV file and reading the contents
data = pd.read_csv('instagram_followers_data.csv')

# converting to a dictionary
data_dict = data.to_dict(orient='records')

df = pd.DataFrame(data_dict)

# Using regex to remove the target string from 'your_column'
df['country'] = df['country'].str.replace('\xa0', '', regex=True)

# converting the cleaned data back to a dictionary
cleaned_data = df.to_dict(orient='records')

print(cleaned_data)
