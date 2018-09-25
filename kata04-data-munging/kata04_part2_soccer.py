# -*- coding: utf-8 -*-
import csv
import numpy as np
import pandas
import re
import os
from shutil import copyfile

def prepare_data_to_csv(filename):
    if (filename[-3:] == 'dat'):
        newname = filename.replace('dat','txt')
        # os.filename,newname)
        copyfile(filename,newname)
        filename = newname

    file = open(filename)
    data = file.read()
    data = data.replace(". ",".")
    data = data.replace("-","")
    data = re.sub(' +', ' ', data)
    data = data.replace("*", "")
    # data = data.replace(" ",",")
    data.split('\n')
    data = [line.lstrip().replace(" ", ",") for line in data.split('\n') if line.strip() != '']
    csv_filename = filename.replace('txt','csv')
    csv_file = open(csv_filename, "w")
    for d in data:
        csv_file.write(d + "\n")
    csv_file.close()
    return csv_filename

def read_csv_data(csv_filename):
    data = pandas.read_csv(csv_filename)
    return data

def main():
    csv_filename = prepare_data_to_csv("football.dat")
    data = read_csv_data(csv_filename)
    team_name = data['Team']
    win_for = data['F']
    win_against = data['A']
    win_difference = abs(win_for - win_against)
    min_index = win_difference.idxmin()
    print ("The team", team_name[min_index], "has the smallest difference in ‘for’ and ‘against’ goals.")

if __name__ == "__main__":
    main()
