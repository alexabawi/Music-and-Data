#/usr/bin/env python3

"""
Sample program to attempt to save data from billboard charts as a json file
"""

import json
import billboard as bd

"""
Grabs the user data from the billboard charts to create the dictionary
"""
def grab_data():

    chart_data = {}

    # Grab current chart
    current_chart = bd.ChartData('hot-100')

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
Turns the passed in dictionary into a .json file for analysis
"""
def create_json(dict_to_use):

    with open('sample_data.json', 'w') as outputfile:

        json.dump(dict_to_use, outputfile)


def main():

    print('Grabbing data...\n')
    data = grab_data()


    print('Creating json file..\n')

    create_json(data)

    print('\nComplete!\n')

# Standard boilerplate to run main
if __name__ == '__main__':
    main()
