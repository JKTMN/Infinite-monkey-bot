import json

from number_gen2 import random_indexes

test_words_file_path = "monkey_bot2/data2/test_dict2.JSON"
prev_extract_file_path = "monkey_bot2/data2/prev_extracts.JSON"

class monkey_bot2:

    def read_file(test_words_file_path):
        try:
            with open(test_words_file_path, 'r') as file:
                data = json.load(file)
                return data.get("test_words", [])
        except FileNotFoundError:
            print(f"File not found: {test_words_file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_random_words():
        word_list = monkey_bot2.read_file(test_words_file_path)
        num_list = random_indexes.get_random_indexes()
        random_extract = ""

        for x in num_list:
            random_extract += word_list[x] + " "

        monkey_bot2.is_duplicate(random_extract)

    def is_duplicate(prev_extract_file_path, random_extract):
        try:
            with open(prev_extract_file_path, 'r') as json_file:
                previous_extracts = json.load(json_file)
                
                for value in previous_extracts.values():
                    if isinstance(value, str) and random_extract in value:
                        monkey_bot2.get_random_words()
                monkey_bot2.compare_extracts(random_extract)
        except FileNotFoundError:
            print(f"File not found: {prev_extract_file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def store_extract(prev_extract_file_path, random_extract):
        try:
            try:
                with open(test_words_file_path, 'r') as json_file:
                    existing_extracts = json.load(json_file)
            except FileNotFoundError:
                existing_extracts["previous_extracts"].append(random_extract)

                with open(test_words_file_path, 'w') as json_file:
                    json.dump(existing_extracts, json_file, indent=2)
        except Exception as e:
            print(f"Error: {e}")

    def compare_extracts(extract, random_extract):
        if extract == random_extract:
            return True
        else:
            monkey_bot2.store_extract(random_extract)
            monkey_bot2.get_random_words()
    
    def count_loops():
        loops = 0
        while monkey_bot2.compare_extracts != True:
            loops += 1
        
        print("match found after {loops} iterations")
        return loops

monkey_bot2.get_random_words()