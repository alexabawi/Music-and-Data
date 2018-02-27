#/usr/bin/env python3

"""
Filename: save_chart_as_json.py
Author: Nate Browne
Last Edited: 23 February 2018
Program used to grab data from billboard charts and append it into a .json file
for use in the python notebooks for COGS 108 Winter 2018. the name of the json
file must be passed in as a command line argument.
"""

import json
import billboard as bd
from sys import exit, argv
from pathlib import Path
from os import remove

"""
Grabs the user data from the billboard charts to create and return a dictionary
where the key value is the rank and the data associated with the key is a list
of the other song attributes (title, artist peak position, last position,
number of weeks)

Params: current_chart: the chart for which a dict is supposed to be created
Return: A dict of the chart data with rank for key and song attributes in a list
for values
"""
def grab_data(current_chart):

    chart_data = {}

    # Loop through the chart populating the dict
    for ind in range(len(current_chart)):

        # Populate the list
        attrib = []
        attrib.append(current_chart[ind].title)
        attrib.append(current_chart[ind].artist)
        attrib.append(current_chart[ind].peakPos)
        attrib.append(current_chart[ind].lastPos)
        attrib.append(current_chart[ind].weeks)

        # Append the list into the dict for the rank as the key val
        chart_data[current_chart[ind].rank] = attrib

    return chart_data


"""
Appends the passed in dictionary into a .json file for analysis

Params: list_to_use: A dictionary of the chart to append to the json file for
                     ease of use
        file_to_use: A string of the name of the file to serialize the json data
                     onto
Return: None.
"""
def create_json(list_to_use, file_to_use):

    with open(file_to_use, 'a') as outputfile:

        json.dump(list_to_use, outputfile)


"""
Parses command line argument and handles errors, then delegates to other two
functions to download all data.

Params: None.
Return: None.
"""
def main():

    # Create a counter of how many charts downloaded for keeping track
    counter = 1

    # Check command line argument number for correctness. Should only be 1
    if len(argv) != 2:

        print('Expected a file name as the only argument.')
        exit(1)


    # Parse the command line argument as the name of the file to save data to
    file_to_use = argv[1]

    # Make sure string passed in ends with .json
    if '.json' not in file_to_use:

        file_to_use += '.json'

    # Create a path to the file so that we can remove incomplete data if
    # interrupted
    next_filename = './' + file_to_use
    my_file = Path(next_filename)

    # Grab current chart
    current_chart = bd.ChartData('hot-100', date='2018-02-24')

    # Create a empty list of dicts of charts
    data = []

    try:

        # Set up our loop to download all the data at once
        while current_chart.previousDate:

            print('Grabbing chart data %d as a dict...\n' % counter)

            # Grab the data and save it into a dict
            next_chart = grab_data(current_chart)

            # append that dict to the list of dicts
            data.append(next_chart)

            # Update current chart to get next set of data
            current_chart = bd.ChartData('hot-100', current_chart.previousDate)
            counter += 1

        # Dump that new list of dicts into the file given
        print('Appending to .json file...\n')
        create_json(data, file_to_use)

        print('Complete!\n')

    except (EOFError, KeyboardInterrupt):

        print('\nInterrupted. Removing incomplete data file and exiting...\n')

        # Delete the file before exiting
        if my_file.exists():

            remove(my_file)

        exit(1)


# Standard boilerplate to run main
if __name__ == '__main__':
    main()
