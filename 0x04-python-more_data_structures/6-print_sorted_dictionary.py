#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return
    
    sorted_keys = sorted(a_dictionary.keys())
    
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))

