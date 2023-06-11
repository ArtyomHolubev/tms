import json
from pathlib import Path

current_path = Path(__file__)
current_dir = current_path.parent

dict_js = {
    111111: ('Vasyliy', 38), 222222: ('Ekaterina', 24),
    333333: ('Antoniy', 12), 444444: ('Polina', 84),
    555555: ('Alexandriy', 45)
}

with open(
    current_dir.joinpath("json_file.json"),
    mode="w"
) as w_file:
    json.dump(dict_js, w_file, indent=4)
