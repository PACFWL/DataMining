
# Step A - 1

import pandas as pd

df = pd.read_csv('Fruit Sales Data.csv')

df.head()

# Step A - 2

df.dtypes

# Step A - 3

weight_in_kg_column = df['Weight in Kg']

weight_in_kg_column

# Step A - 4

max_value = df['Weight in Kg'].max()

max_value

# Step A - 5

filtered_data = df[df['Fruit Name'] == 'Strawberry']

filtered_data

# Step B - 1

import pandas as pd

fruits = pd.DataFrame({
    'x': [0],
    'Apple': [30],
    'Banana': [20]
})

fruits

# Step C - 1 

sales_fruits = pd.DataFrame({
    'x': ['Sales 2022', 'Sales 2023'],
    'Apple': [1000, 5000],
    'Banana': [700, 2000]
})

sales_fruits
