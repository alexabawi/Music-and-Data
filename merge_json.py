#/usr/bin/env python3

"""
Filename: merge_json.py
Author: Nate Browne
Last Edited: 28 February 2018
Takes two .json files and merges their contents into one .json file.
"""

import json
from sys import argv, exit

"""
Takes passed in .json files and merges them into one file

Exceptions Thrown: OSError: Thrown if an OSError or DecodeError are caught in
                            attempting to open and parse the given filename.
Params: file1 - first json file to merge
        file2 - second json file to merge
        destfile - destination file to write to
Return: None.
"""
def merge_json(file1, file2, destfile):

    data = []

    try:

        with open(destfile, 'w') as outputfile:

            with open(file1, 'r') as inputfile:

                filedata = json.load(inputfile)

                data.append(filedata)

            with open(file2, 'r') as inputfile:

                filedata = json.load(inputfile)

                data.append(inputfile)

            json.dump(data, outputfile)
    except(OSError, json.decoder.JSONDecodeError):

        print('File invalid (either doesn\'t exist or can\'t be read).')

        # Raise error for calling function to handle
        raise OSError



"""
Parses command line argument and handles errors, then delegates to other
function to merge the files

Params: None.
Return: None.
"""
def main():


    # Check command line argument number for correctness. Should only be 3
    if len(argv) != 4:

        print('USAGE: ./%s <file1> <file2> <destinationfile>' % argv[0])
        exit(1)

    try:

        # Parse arguments
        file1 = argv[1]
        file2 = argv[2]
        destination = argv[3]

        # Make sure file1 passed in ends with .json
        if '.json' not in file1:

            file1 += '.json'

        # Make sure file2 passed in ends with .json
        if '.json' not in file2:

            file2 += '.json'

        # Make sure file1 passed in ends with .json
        if '.json' not in destination:

            destination += '.json'

        # Merge the files
        merge_json(file1, file2, destination)

        # Print a double newline
        print('\n')

    except(OSError):

        print('Problem with I/O for file. Exiting...')
        exit(1)



# Standard boilerplate to run the main function
if __name__ == '__main__':
    main()
