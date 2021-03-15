# Wrangling Data with Pandas
import pandas as pd
import csv

# open csv file
with open('file.csv', 'w', encoding='utf-8') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for line in csv_reader:
        print(', '.join(line)) # prints out csv data

data_set = pd.read_csv('file.csv')
df1 = pd.DataFrame(data_set)
df1.head()
df1.describe() # check the distribution of data and ensure the properties are expected or reasonable.

# Data shuffling
# see: Why should the data be shuffled for machine learning tasks
# shuffling the data frame (part of preprocessing for ML data)
csv_data = df1.sample(frac=1).reset_index(drop = True)

# accessing columns
cols_2_4 = csv_data.columns[2:4]

csv_data.columns()

# accessing rows