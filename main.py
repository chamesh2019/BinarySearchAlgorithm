import random
from time import time
from typing import List


def binarySearch(input_array: List[int], search_item: int, index=0) -> int:
    '''Get the input list and use binary search algorithm to find the index of an integer'''
    
    if len(input_array) == 1:
        if input_array[0] == search_item:
            return index
        else:
            return -1
    
    mid_index = len(input_array)//2
    if input_array[mid_index] > search_item:
        input_array = input_array[:mid_index]
    
    else:
        index += mid_index
        input_array = input_array[mid_index:]
    
    return binarySearch(input_array, search_item, index)
    
def randomize(item):
    ''''using a constrained randomizer so the probability of the generated search integer inside the araay is high'''
    return random.randint(1, 3) + item

if __name__ == '__main__':
    generated_array = [randomize(i) for i in range(100000)]
    generated_array = sorted(set(generated_array))
    search = random.randint(0, generated_array[-1])
    
    start_time = time()
    index = binarySearch(generated_array, search)
    time_used = time() - start_time
    if not index == -1:
        print(f'Item {search} was found at index {index} with a confirmation value of {generated_array[index]} in {time_used} seconds')
    else:
        print(f'Item {search} was not found on array in {time_used} seconds')
        