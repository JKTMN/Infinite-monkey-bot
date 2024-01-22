import random
from text_processing import text_processing

random_num_list = []
ranom_word_list = []

class random_num():
    
    def random_number_list():
        count = text_processing.count_extract_words()
        print(count)
        i = 0

        while i < count:
            num = random.randrange(1,10)
            random_num_list.append(num)
            i += 1
        return random_num_list
    