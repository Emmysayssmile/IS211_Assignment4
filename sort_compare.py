import argparse
import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order"""
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    return time.time() - start

def shell_sort(a_list):
    start = time.time()
    sublistcount = len(a_list) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(a_list, startposition, sublistcount)
        sublistcount = sublistcount // 2
    return time.time() - start

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value

def python_sort(a_list):
    start = time.time()
    sorted_list = sorted(a_list)
    return time.time() - start

def benchmark_sort():
    list_sizes = [500, 1000, 5000]
    for size in list_sizes:
        ins_time = shell_time = py_time = 0
        for _ in range(100):
            data = get_me_random_list(size)
            
            copy1, copy2, copy3 = data[:], data[:], data[:]
            py_time += python_sort(copy1)
            ins_time += insertion_sort(copy2)
            shell_time += shell_sort(copy3)
            
        print(f"Python sort took {py_time / 100:10.7f} seconds on average for size {size}")
        print(f"Insertion sort took {ins_time / 100:10.7f} seconds on average for size {size}")
        print(f"Shell sort took {shell_time / 100:10.7f} seconds on average for size {size}")

if __name__ == "__main__":
    benchmark_sort()

