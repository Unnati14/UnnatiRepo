from shutil import copyfile
import pandas
import re

def prepare_data_to_csv(filename):
    if (filename[-3:] == 'dat'):
        newname = filename.replace('dat','txt')
        # os.filename,newname)
        copyfile(filename,newname)
        filename = newname
    file = open(filename)
    data = file.read()
    # Remove repeated spaces
    data = re.sub(' +', ' ', data)
    data = data.replace("*","") # remove * from data
    data.split('\n')
    data = [line.lstrip().replace(" ",",") for line in data.split('\n') if line.strip() != '']
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
    csv_filename = prepare_data_to_csv("weather.dat")
    data = read_csv_data(csv_filename)
    day = data['Dy']
    maximum_temperature = data['MxT']
    minimum_temperature = data['MnT']
    difference_temperature = maximum_temperature - minimum_temperature
    min_location = difference_temperature.idxmin()
    print("The smallest temperature spread was on", day[min_location])

if __name__ == "__main__":
    main()