import re
from pathlib import Path

def convert_translations(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    output_lines = []

    for line in lines:
        # Check if the line is a comment containing a title key
        match = re.match(r'/\* Class = "(\w*)"; title = "(.*)"; ObjectID = "([^"]+)"; \*/', line)
        if match:
            # Extract the ObjectID and the English title
            class_name = match.group(1)
            english_title = match.group(2)
            object_id = match.group(3)
            # Format the new line
            formatted_line = f'"{object_id}.title" = "{english_title}";\n'

            output_lines.append(f"/* No comment by Translator*/\n{formatted_line}\n")
        else:
            # Copy the line as is if it doesn't match the pattern
            continue

    with open(output_file, encoding='utf-8', mode='w') as file:
        file.writelines(output_lines)

# ディレクトリ内のすべてのstringsファイルを変換
strings_directory = Path('zh-Hans')
strings_files = strings_directory.glob('*.strings')

for file_path in strings_files:
    output_file_path = Path('en') / file_path.name
    convert_translations(file_path, output_file_path)