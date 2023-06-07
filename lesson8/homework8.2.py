from pathlib import Path

str1, str2, str3, str4 = input('Строка 1: '), input('Строка 2: '), input('Строка 3: '), input('Строка 4 ')
current_path = Path(__file__)
current_dir = current_path.parent

with open(
    current_dir.joinpath("hm8.2.txt"),
    mode="w",
    encoding="utf-8"
) as write_file:
    write_file.write(str1 + '\n')
    write_file.write(str2 + '\n')

with open(
    current_dir.joinpath("hm8.2.txt"),
    mode="a",
    encoding="utf-8"
) as write_file:
    write_file.write(str3 + '\n')
    write_file.write(str4 + '\n')
