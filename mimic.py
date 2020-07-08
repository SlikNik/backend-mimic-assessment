#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""
import random
import sys
import logging
import os

log_dir = os.path.abspath(os.path.join(os.getcwd(), 'log'))
if not os.path.exists(log_dir):
    logging.warning("{} does not exist. Creating it.".format(log_dir))
    os.makedirs(log_dir)
    os.path.join(log_dir, 'test.log')

__author__ = "Nikal Morgan"

logger = logging.getLogger(__name__)

"""
Demo Resources:
setdefault()
def print_top
"""


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    # log "Reading {filename}"
    # log found word
    # log added word
    mimic_dict = {}
    with open(filename, "r") as f:
        mimic_list = f.read().split()
        logger.info("Reading '{}'".format(filename))
        mimic_dict[""] = [mimic_list[0]]
        logger.info("Start Key: '{}'".format(mimic_list[0]))
        while len(mimic_list) > 1:
            mimic_dict.setdefault(mimic_list[0], [mimic_list[1]])
            logger.info("'{}':'{}'".format(mimic_list[0],
                                           mimic_list[1]))
            # mimic_dict[mimic_list[0]] += [mimic_list[1]]
            mimic_dict[mimic_list[0]].append(mimic_list[1])
            logger.info("Added '{}' to '{}' key".format(mimic_list[1],
                                                        mimic_list[0]))
            mimic_list.pop(0)
    # print(mimic_dict)
    return mimic_dict


# create_mimic_dict("imdev.txt")


def print_mimic(mimic_dict, start_word):
    """Given a previously created mimic_dict and start_word,
    prints 200 random words from mimic_dict as follows:
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """
    mimic_output = ''
    current_mimic = start_word
    for i in range(200):
        if current_mimic in mimic_dict:
            next_mimic = random.choice(mimic_dict[current_mimic])
        else:
            logger.warning('No such key: {}. Reseting to ""'
                           .format(current_mimic))
            next_mimic = ''
        mimic_output += current_mimic
        current_mimic = next_mimic
    # print(mimic_output)


# print_mimic(create_mimic_dict("alice.txt"), "Alice's")

# Provided main(), calls mimic_dict() and print_mimic()
def main():
    logging.basicConfig(
        format='%(asctime)s.%(msecs)03d %(name)-12s    '
               '%(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d &%H:%M:%S',
        filename='log/test.log'
    )
    logger.setLevel(logging.INFO)
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
