#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: Dec 2019
# This program uses a 2D array

import random


def average_of_numbers(a_2D_list, rows, columns):
    # this function finds average of all the elements in  a 2D array

    total = 0
    for row_value in a_2D_list:
        for single_element in row_value:
            total += single_element

    total = total/(rows*columns)

    return total


def main():
    # this function uses a 2D array

    a_2d_list = []
    # input
    rows_string = input("How many row would you like: ")
    columns_string = input("How many columns would you like: ")

    try:
        rows = int(rows_string)
        columns = int(columns_string)

        for loop_counter_rows in range(0, rows):
            temp_column = []
            for loop_counter_columns in range(0, columns):
                a_random_number = random.randint(0, 50)
                temp_column.append(a_random_number)
                print("{0} ".format(a_random_number), end="")
            a_2d_list.append(temp_column)
            print("")

        average = average_of_numbers(a_2d_list, rows, columns)
        print("The sum of all the numbers is: {0} ".format(average))

    except(ValueError):
        print("invalid numbers")


if __name__ == "__main__":
    main()
