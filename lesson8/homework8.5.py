from pathlib import Path
import pandas as pd

current_path = Path(__file__)
current_dir = current_path.parent

df = pd.read_csv(current_dir.joinpath("csv_file.csv"))
data = df.drop('Age', axis=1, inplace=True)
df.index = ['Person 1', 'Person 2', 'Person 3', 'Person 4', 'Person 5']

new = df.T
writer = pd.ExcelWriter('example.xlsx', engine='xlsxwriter')
new.to_excel(writer)
writer._save()
