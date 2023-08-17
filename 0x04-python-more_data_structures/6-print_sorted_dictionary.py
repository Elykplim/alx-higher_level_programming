#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys_ordered = list(a_dictionary.keys())
    keys_ordered.sort()
    for key in keys_ordered:
        print("{}: {}".format(key, a_dictionary.get(key)))

