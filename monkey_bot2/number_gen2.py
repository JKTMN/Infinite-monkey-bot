import random

from text_processing2 import text_processing2

class random_indexes():

    def get_random_indexes():
        count = text_processing2.count_words()
        return random.sample(range(count), 6)
    
print(random_indexes.get_random_indexes())