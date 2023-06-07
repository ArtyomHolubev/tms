import pandas as pd
from pathlib import Path
from csv import writer

current_path = Path(__file__)
current_dir = current_path.parent
phone = [375294561232, 375294991232, 375294588882, 375294577772, 378822561232]

with open(
        'json_file.json', encoding='utf-8'
) as read_json:
    df = pd.read_json(read_json)

df.to_csv('csv_file.csv', encoding='utf-8', index=False)

with open('csv_file.csv', 'a', newline='') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(phone)
