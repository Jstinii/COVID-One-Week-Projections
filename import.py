"""
Author: Justin Ngo
Date: 7/13/20
Description: Script to gather 1 week projections for deaths of specified area given terminal prompts
CSV files from Reich's Labs COVID Forecast Lab git repository for
https://github.com/reichlab/covid19-forecast-hub/tree/master/data-processed
"""
import csv

def import_func():
    print("Input the Forecast CSV name[.csv]")
    file=input()
    #2020-07-06-CovidAnalytics-DELPHI.csv
    print("When is the date the forecast was made? [YYYY-MM-DD]")
    date = input()
    #date = '2020-07-06'
    print("What is the state's FIPS numeric code [00]")
    state = input()
    with open('Reported_Data\\' + file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        write_file = open('Reported_Data\\projections.csv', 'w')
        new_data = []
        for row in csv_reader:
            if row[0] == '':
                print('No data was found')
                return
            if row[0] == date and row[1] == '1 wk ahead cum death' and row[3] == state and row[4] == 'point':

                csv_writer = csv.writer(write_file)

                new_data.append((row[6]))

                csv_writer.writerow(new_data)

                print('1 week forecast saved in projections.csv in Reported Data folder')

import_func()


