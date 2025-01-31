"""
Tarea Parte 1
"""

from dataclasses import dataclass
import time
import sys
from typing import List
import re

@dataclass
class StatisticsDTO:
    """
    Statistics class because the linter said so
    """
    mean: float
    median: float
    mode: float
    std_dev: float
    variance: float


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

def get_mode(numbers: List[float]):
    """
    Receives a list of numbers and returns the mode of the list
    """
    dictionary = {}

    for item in numbers:
        indx = f"{item}"
        dictionary[indx] = (dictionary[indx] + 1) if indx in dictionary else 1

    biggest_item = { 'count': 0, 'number': '0' }
    for key, value in dictionary.items():
        if biggest_item['count'] <= value:
            biggest_item = { 'count': value, 'number': key }

    return biggest_item['number']

def get_median (numbers) -> float:
    """
    Receives a list of numbers and returns the median of the list
    """
    sorted_nums = bubble_sort(numbers)

    if len(sorted_nums) % 2 == 0:
        indx = int(len(sorted_nums)/ 2) - 1
        return (sorted_nums[indx] + sorted_nums[indx + 1]) / 2

    indx = int((len(sorted_nums) + 1)/ 2) - 1
    return  sorted_nums[indx]

def get_mean (numbers):
    """
    Receives a list of numbers and returns the mean of the list
    """
    acum = 0
    for num in numbers:
        acum = acum + num

    return acum / len(numbers)

def get_standar_deviation (numbers):
    """
    Receives a list of numbers and returns the standar deviation of the list
    """
    mean = get_mean(numbers)

    acum = 0
    for num in numbers:
        acum = acum + (num - mean) ** 2

    return (acum / (len(numbers))) ** 0.5

def get_variance (numbers):
    """
    Receives a list of numbers and returns the variance of the list
    """
    mean = get_mean(numbers)

    acum = 0
    for num in numbers:
        acum = acum + (num - mean) ** 2

    return (acum / (len(numbers) - 1))

def read_data_from_file (path):
    """
    Reads a file
    """
    # Opening file
    with open(path, 'r', encoding="utf-8") as file:
        count = 0
        pattern = re.compile("^[+-]?([0-9]*[.])?[0-9]+$")
        content = []

        for line in file:
            count += 1
            line_content = line.strip()

            if pattern.match(line_content):
                content.append(line.strip())
        file.close()

    return content

def print_results(*, statistics, compute_duration, file_name):
    """
    Prints the results of the computation on a file
    """
    print(f"The mean is: {statistics.mean}")
    print(f"The median is: {statistics.median}")
    print(f"The mode is: {statistics.mode}")
    print(f"The  standard deviation is: {statistics.std_dev}")
    print(f"The variance is: {compute_duration}")

    print(f"The computing time was: {statistics.variance}")

    with open("results/StatisticsResults.txt", "a", encoding="utf-8") as f:
        print(f"Results of computation of file {file_name}")
        f.write(f"Results of computation of file {file_name}\n")

        f.write(f"The mean is: {statistics.mean}\n\
                The median is: {statistics.median}\n\
                The mode is: {statistics.mode}\n\
                The  standard deviation is: {statistics.std_dev}\n\
                The variance is: {statistics.variance}\n\n\
                The computing time was: {compute_duration}s")
        f.write(f"\n\nThe computing time was: {compute_duration}s\n\n\n\n")
        f.close()

def main():
    """
    Main function
    """
    start_time = time.time()

    file_path = sys.argv[1]

    numbers = list(map(float, read_data_from_file(file_path)))
    print(len(numbers))

    mean = get_mean(numbers)
    median = get_median(numbers)
    mode = get_mode(numbers)
    std_dev = get_standar_deviation(numbers)
    variance = get_variance(numbers)
    compute_duration = time.time() - start_time
    print(f"--- {compute_duration} seconds ---")

    stats = StatisticsDTO(mean=mean,
        median=median,
        mode=mode,
        std_dev=std_dev,
        variance=variance)

    print_results(statistics=stats,
        compute_duration=compute_duration,
        file_name=file_path)

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
