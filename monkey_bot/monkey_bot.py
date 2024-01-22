from text_processing import text_processing
from number_generator import random_num
import json

random_words_list = []

class monkey_bot():

    def read_file(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                word_list = data.get("macbeth_words", [])
                return word_list
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurrred: {e}")
            
    def set_random_words():
        random_number_list = random_num.random_number_list()
        word_list = monkey_bot.read_file("data/macbeth_dict.JSON")
        for x in random_number_list:
            i = x
            if i < len(word_list):
                random_words_list.append(word_list[i])

        return random_words_list
    
random_words_list = monkey_bot.set_random_words()
print(random_words_list)
