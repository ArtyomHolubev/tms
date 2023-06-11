import csv
import json
from pathlib import Path
import pandas as pd

current_path = Path(__file__)
current_dir = current_path.parent
phone = [375294561232, 375294991232, 375294588882, 375294577772, 378822561232]


with open(
    current_dir.joinpath("json_file.json"),
    mode="r"
) as r_file:
    data = json.load(r_file)


with open(
        current_dir.joinpath("csv_file.csv"),
        mode='w'
) as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    header = ['ID', 'Name', 'Age']
    writer.writerow(header)

    for k, v in data.items():
        writer.writerow([k, v[0], v[1]])

df = pd.read_csv(current_dir.joinpath("csv_file.csv"), index_col=False)
df["Phone"] = phone
df.to_csv(current_dir.joinpath("csv_file.csv"), index=False)

