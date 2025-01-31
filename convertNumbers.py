"""
Tarea Parte 2
"""

import time
import sys
import re
import logging

def negative_binary (binary, add_padding = True):
    """
    Handles the conversion of a positive binary to a negative one
    """
    binary = f"{(len(binary) % 4) * "0"}{binary}"
    inverse = ''
    for bit in binary:
        if bit == '0':
            inverse = f"{inverse}1"
        else:
            inverse = f"{inverse}0"

    added = False
    carry = 0
    result = []

    # Traverse both strings from the end
    for i in range(len(inverse) - 1, -1, -1):
        bit_aux = int(inverse[i])
        bit_sum = bit_aux + carry

        if added is False:
            bit_sum += 1
            added = True

        bit = bit_sum % 2
        carry = bit_sum // 2

        result.append(str(bit))

    if carry > 0:
        result.append('1')

    result = ''.join(result[::-1])

    if len(result) < 10 and add_padding:
        result = f"{(10 - len(result)) * "1"}{result}"
    else:
        result = f"{(len(result) % 4) * "1"}{result}"
    return result

def process_binary(number):
    """
    Converts number to binary, abstracted function
    """
    bit = f"{number % 2}"
    if number >= 1:
        return f"{process_binary(int(number/2))}{bit}"
    return f"{number if number == 0 else ""}"

def convert_to_binary (number, add_padding = True):
    """
    Handles the convertion to binary for both positive and negative numbers
    """
    number = int(number)
    is_negative = number < 0
    if is_negative:
        number = number * -1
    binary = process_binary(number)

    binary = binary[1:] if binary[0] == '0' and number != 0 else binary

    if is_negative:
        binary = negative_binary(binary, add_padding)
    return binary

def process_to_hex (number):
    """
    Converts a decimal number to a hexadecimal
    """
    hexa = ""
    if number % 16 < 10:
        hexa = f"{number % 16}"
    else:
        match number % 16:
            case 10:
                hexa = "A"
            case 11:
                hexa = "B"
            case 12:
                hexa = "C"
            case 13:
                hexa = "D"
            case 14:
                hexa = "E"
            case 15:
                hexa = "F"

    if number >= 15:
        return f"{convert_to_hexadecimal(int(number/16))}{hexa}"
    return f"{hexa}"

def binary_to_hex(binary, add_padding = True):
    """
    Transforms a binary to hexadecimal, it has to divide the binary to chunks of 4 bits
    """
    chunks = 4
    binary = binary[::-1]
    binaries_to_convert = [binary[i:i+chunks] for i in range(0, len(binary), chunks)]
    binaries_to_convert = binaries_to_convert[::-1]
    binaries_to_convert = list(map(lambda item: item[::-1], binaries_to_convert))

    hexa = ''
    for i in range(len(binaries_to_convert) - 1, -1, -1):
        item = binaries_to_convert[i]
        acum = 0
        for j in range(len(item) - 1, -1, -1):
            inv_indx = len(item) - j - 1
            if item[j] == '1':
                acum += (2 ** inv_indx)
        hexa = f"{process_to_hex(acum)}{hexa}"

    if len(hexa) < 10 and add_padding:
        hexa = f"{(10 - len(hexa)) * "F"}{hexa}"
    return hexa

def convert_to_hexadecimal (number):
    """
    Converts a decimal number to hexadecimal. Handles positive and negative numbers
    """
    number = int(number)
    is_negative = number < 0

    if is_negative:
        binary = convert_to_binary(number, False)
        return binary_to_hex(binary)
    return process_to_hex(number)

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
            else:
                logging.exception("The number on file was invalid")
        file.close()

    return content

def print_results(numbers, binary, hexa, compute_duration, file_name):
    """
    Prints the results of the computation on a file
    """
    if not (len(numbers) == len(binary) and len(numbers) == len(hexa)):
        raise ValueError("List don't match on the quantity")

    with open("results/ConvertionResults.txt", "a", encoding="utf-8") as f:
        print(f"Results of computation of file {file_name}")
        f.write(f"Results of computation of file {file_name}\n")
        print("NUMBER\t\tBIN\t\tHEX")
        f.write("NUMBER\t\tBIN\t\tHEX\n")
        for i in range(len(numbers) -1):
            print(f"{numbers[i]}\t\t{binary[i]}\t\t{hexa[i]}")
            f.write(f"{numbers[i]}\t\t{binary[i]}\t\t{hexa[i]}\n")

        f.write(f"\n\nThe computing time was: {compute_duration}s\n\n\n\n")
        f.close()

def main():
    """
    Main function
    """
    start_time = time.time()

    file_path = sys.argv[1]

    numbers = list(map(int, read_data_from_file(file_path)))

    binary = list(map(convert_to_binary, numbers))
    hexa = list(map(convert_to_hexadecimal, numbers))

    compute_duration = time.time() - start_time
    print(f"--- {compute_duration} seconds ---")

    print_results(numbers, binary, hexa, compute_duration, file_path)

main()
