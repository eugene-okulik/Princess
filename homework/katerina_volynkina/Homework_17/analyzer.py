import os
import argparse
from datetime import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
default_logs_path = os.path.join(homework_path, 'eugene_okulik', 'data', 'logs')


def read_file(file_path):
    with open(file_path, encoding='utf-8') as data_file:
        for line in data_file.readlines():
            yield line


def is_new_block(line):
    words = line.split()
    if len(words) == 0:
        return False
    try:
        datetime.strptime(words[0], "%Y-%m-%d")
        return True
    except ValueError:
        return False


parser = argparse.ArgumentParser()
parser.add_argument("path", nargs="?", default=default_logs_path, help="File or folder name")
parser.add_argument("--text", required=True, help="Text for search")
args = parser.parse_args()


files_list = []
if os.path.isfile(args.path):
    files_list.append(args.path)
elif os.path.isdir(args.path):
    for file_name in os.listdir(args.path):
        full_path = os.path.join(args.path, file_name)
        if os.path.isfile(full_path):
            files_list.append(full_path)
else:
    print("Путь не найден!")
    exit()


log_blocks = {}

for file_path in files_list:
    file_name = os.path.basename(file_path)
    current_time = ""
    current_lines = []
    start_line = 1

    for line_num, line in enumerate(read_file(file_path), start=1):
        if is_new_block(line):
            if current_time != "":
                log_blocks[current_time] = {
                    "file": file_name,
                    "start_line": start_line,
                    "lines": current_lines
                }

            words = line.split()
            current_time = words[0] + " " + words[1]
            start_line = line_num
            current_lines = [line]
        else:
            current_lines.append(line)

        if current_time != "":
            log_blocks[current_time] = {
            "file": file_name,
            "start_line": start_line,
            "lines": current_lines
        }

search_word = args.text
found_count = 0

for log_time, block in log_blocks.items():
    for offset, line_text in enumerate(block["lines"]):
        if search_word.lower() in line_text.lower():
            exact_line = block["start_line"] + offset
            words = line_text.split()

            for index, word in enumerate(words):
                if search_word.lower() in word.lower():
                    found_count += 1
                    left_words = words[max(0, index - 5):index]
                    right_words = words[index + 1:index + 6]
                    snippet = " ".join(left_words + [f"[{word}]"] + right_words)

                    print(f"Файл: {block['file']} | Строка: {exact_line}")
                    print(f"Кусок ошибки: {snippet}")
                    print("-" * 50)

print(f"Всего найдено совпадений: {found_count}")
