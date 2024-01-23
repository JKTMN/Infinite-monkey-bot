import random
from text_processing import text_processing

random_num_list = []

class random_num():
    
    def get_random_number_list():
        count = text_processing.count_extract_words()
        print(count)
        i = 0

        while i <= count:
            num = random.randrange(1, count)
            random_num_list.append(num)
            i += 1
        print(random_num_list)
        return random_num_list  
