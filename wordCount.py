"""
Tarea Parte 3
"""

import time
import sys


def bubble_sort(arr):
    """
    Standar bubble sort
    """
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped is False:
            break

    return arr

def read_data_from_file (path):
    """
    Reads a file
    """
    # Opening file
    with open(path, 'r', encoding="utf-8") as file:
        count = 0

        content = []

        for line in file:
            count += 1
            content.append(line.strip())
        file.close()

    return content

def count_words(words):
    """
    Receives a list of words and counts them, returns a dictionary with key-value pair of word-count
    """
    dictionary = {}
    for word in words:
        indx = f"{word}"
        dictionary[indx] = (dictionary[indx] + 1) if indx in dictionary else 1

    return dictionary

def print_results(dictionary, compute_duration, file_name):
    """
    Prints the results of the computation on a file
    """

    with open("results/WordCountResults.txt", "a", encoding="utf-8") as f:
        print(f"Results of computation of file {file_name}")
        f.write(f"Results of computation of file {file_name}\n")

        for key, value in dictionary.items():
            print(f"{key}\t\t{value}")
            f.write(f"{key}\t\t{value}\n")

        f.write(f"\n\nThe computing time was: {compute_duration}s\n\n\n\n")
        print(f"--- {compute_duration} seconds ---")
        f.close()

def main():
    """
    Main function
    """
    start_time = time.time()

    file_path = sys.argv[1]

    file_content = bubble_sort(read_data_from_file(file_path))

    count_dict = count_words(file_content)

    compute_duration = time.time() - start_time

    print_results(count_dict, compute_duration, file_path)

main()
