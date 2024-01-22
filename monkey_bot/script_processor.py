import json
import string
import re

def remove_line_numbers(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

    # Use regular expression to remove line numbers
    lines_without_numbers = [re.sub(r"^\s*\d+", "", line) for line in lines]

    with open(output_file, 'w', encoding='utf-8') as output_file:
        output_file.writelines(lines_without_numbers)

remove_line_numbers('macbeth_w_line_numbers.txt', 'macbeth_wo_line_numbers.txt')

def process_macbeth_script(macbeth_text, output_file="macbeth_dict.JSON"):

    words = [word.strip(string.punctuation).lower() for word in macbeth_text.split()]

    unique_words = list(set(words))

    result_dict = {"macbeth_words": unique_words}

    with open(output_file, "w") as json_file:
        json.dump(result_dict, json_file, indent=2)


with open('macbeth_wo_line_numbers.txt', 'r', encoding='utf-8') as file:
    macbeth_text = file.read()

process_macbeth_script(macbeth_text)
