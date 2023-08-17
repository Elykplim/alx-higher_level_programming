#!/usr/bin/python3
def uniq_add(new_list=[]):
    unique_items = set(new_list)
    result_sum = 0

    for item in unique_items:
        result_sum += item

    return result_sum
