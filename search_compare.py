import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order"""
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, time.time() - start

def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found, time.time() - start

def binary_search_iterative(a_list, item):
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found, time.time() - start

def binary_search_recursive(a_list, item, start_time=None):
    if start_time is None:
        start_time = time.time()
    if len(a_list) == 0:
        return False, time.time() - start_time
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True, time.time() - start_time
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item, start_time)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item, start_time)

def benchmark_search():
    sizes = [500, 1000, 5000]
    target = 99999999
    
    for size in sizes:
        seq_time = ord_seq_time = bin_iter_time = bin_rec_time = 0
        
        for _ in range(100):
            data = get_me_random_list(size)
            data.sort()
            
            _, time_taken = sequential_search(data, target)
            seq_time += time_taken
            
            _, time_taken = ordered_sequential_search(data, target)
            ord_seq_time += time_taken
            
            _, time_taken = binary_search_iterative(data, target)
            bin_iter_time += time_taken
            
            _, time_taken = binary_search_recursive(data, target)
            bin_rec_time += time_taken
            
        print(f"Sequential Search took {seq_time / 100:10.7f} seconds on average for size {size}")
        print(f"Ordered Sequential Search took {ord_seq_time / 100:10.7f} seconds on average for size {size}")
        print(f"Binary Search Iterative took {bin_iter_time / 100:10.7f} seconds on average for size {size}")
        print(f"Binary Search Recursive took {bin_rec_time / 100:10.7f} seconds on average for size {size}")

if __name__ == "__main__":
    benchmark_search()
