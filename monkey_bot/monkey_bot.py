from text_processing import text_processing
from number_generator import random_num
import json

#extract = "Actus Primus Scoena Prima Thunder and Lightning Enter three Witches  When shall we three meet againe In Thunder Lightning or in Raine  When the Hurley burleys done When the Battailes lost and wonne  That will be ere the set of Sunne  Where the place  Vpon the Heath  There to meet with Macbeth  I come Gray Malkin All Padock calls anon faire is foule and foule is faire Houer through the fogge and filthie ayre Exeunt Scena Secunda Alarum within Enter King Malcome Donalbaine Lenox with attendants meeting a bleeding Captaine King What bloody man is that he can report As seemeth by his plight of the Reuolt The newest state"
extract = "your mum"

class monkey_bot():

    def read_file(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                word_list = data.get("test_words", [])
                return word_list
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurrred: {e}")
            
    def set_random_words():
        random_number_list = random_num.get_random_number_list()
        word_list = monkey_bot.read_file("data/test_dict.JSON")

        random_extract = ""
        for x in random_number_list:
            random_extract += word_list[x] + " "

        print(random_extract)
        return random_extract
    
    def compare_extracts(extract):
        while True:
            random_extract = monkey_bot.set_random_words()
            if extract == random_extract:
                return True

    def count_loops(extract):
        loops = 0
        status = monkey_bot.compare_extracts(extract)
        print(f"Number of loops until match: {loops}")


status = monkey_bot.compare_extracts(extract)
print(monkey_bot.count_loops(status))
