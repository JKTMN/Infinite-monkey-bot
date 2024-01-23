import json
import string
import re

def remove_numbers_and_punctuation(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

    pattern = r"^\s*\d+|\b\d+\b|[{}]".format(re.escape(string.punctuation))
    lines_without_numbers_and_punctuation = [re.sub(pattern, "", line) for line in lines]

    with open(output_file, 'w', encoding='utf-8') as output_file:
        output_file.writelines(lines_without_numbers_and_punctuation)

remove_numbers_and_punctuation('data/macbeth_w_line_numbers_and_punctuation.txt', 'data/macbeth_wo_line_numbers_and_punctuation..txt')

def process_macbeth_script(macbeth_text, output_file="macbeth_dict.JSON"):

    words = [word.strip(string.punctuation).lower() for word in macbeth_text.split()]

    unique_words = list(set(words))

    result_dict = {"macbeth_words": unique_words}

    with open(output_file, "w") as json_file:
        json.dump(result_dict, json_file, indent=2)


with open('data/macbeth_wo_line_numbers_and_punctuation.txt', 'r', encoding='utf-8') as file:
    macbeth_text = file.read()

process_macbeth_script(macbeth_text)
