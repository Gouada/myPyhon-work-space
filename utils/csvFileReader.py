
import csv

def readCSV(filename):


    """ open file for reading """
    try:
        #rd = open(file_path, "r")

        with open(filename, "r") as csvFile:
            """ read first line """
            rd = csv.reader(csvFile)
            next(rd)
            rw = []
            for lt in rd:
                #lt = next(rd)
                rw.append(lt)
            return rw
    except FileNotFoundError as error:
        print(error.__str__())




