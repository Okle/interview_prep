#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    a = input()

    b = input()


    def char_count(my_string):

        char_count_htbl = {}

        for item in my_string:
            if item in char_count_htbl.keys():
                char_count_htbl[item] += 1
            else:
                char_count_htbl[item] = 1

        return char_count_htbl


    def make_anagram_remove_count(first_str, second_str):

        remove_num = 0

        first_count = char_count(first_str)
        second_count = char_count(second_str)

        for key, value in first_count.items():
            if key in second_count.keys():
                remove_num = remove_num + abs(value - second_count[key])
                second_count[key] = 0
            else:
                remove_num = remove_num + value

        for key, value in second_count.items():
            if value != 0:
                remove_num = remove_num + value

        return remove_num


    def number_needed(a, b):
        total = 0
        for letter in "abcdefghijklmnopqrstuvwxyz":
            total += abs(a.count(letter) - b.count(letter))
        return total


    def number_needed_1(a, b):
        H = {}
        count = 0
        for i in range(len(a)):
            if not H.get(a[i]):
                H[a[i]] = 1
            else:
                H[a[i]] += 1

        for i in range(len(b)):
            if H.get(b[i]):
                H[b[i]] -= 1
            else:
                count += 1
        for v in H.values():
            count += v
        return count

    print(make_anagram_remove_count(a, b))





