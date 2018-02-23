#!/usr/bin/env python3


"""
Filename: print_json.py
Author: Nate Browne
Short script used to legibly print out .json files in a readable format using
the pprint module.
"""

import pprint
import json
from sys import exit, argv

"""
Prints out the given filename using the pretty printer to make indentation more
legible.

Exceptions Thrown: OSError: Thrown if an OSError or DecodeError are caught in
                            attempting to open and parse the given filename.
Params: filename: name of the file to be printed
Return: None.
"""
def print_the_file(filename):

    pp = pprint.PrettyPrinter(indent=1)

    try:

        with open(filename, 'r') as inputfile:

                parsed = json.load(inputfile)
                pp.pprint(parsed)

    except(OSError, json.decoder.JSONDecodeError):

        print('File invalid (either doesn\'t exist or can\'t be read).')

        # Raise error for colling function to handle
        raise OSError

"""
Parses command line arguments, cleans up the filename to verify that it is
indeed a .json file, then calls print_the_file to handle the printing as well as
any errors thrown

Params: None.
Return: None.
"""
def main():

    # Check command line argument number for correctness. Should only be 1
    if len(argv) != 2:

        print('\nExpected a filename as the only argument.')
        exit(1)

    # Start try block to handle errors if thrown
    try:

        filename = argv[1]

        # Make sure file actually is a .json file

        if '.json' not in filename:

            filename += '.json'

        # Call function to use the PrettyPrinter to print the json readably
        print_the_file(filename)

        # Print a double newline
        print('\n')

    except(OSError):

        print('Problem with I/O for file. Exiting...')
        exit(1)


# Standard boilerplate to run the main function
if __name__ == '__main__':
    main()
