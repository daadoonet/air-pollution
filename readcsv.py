'''----------------------------------------------------------------------import----------------------------------------------------------------------'''


import csv

'''----------------------------------------------------------------------read-from-csv----------------------------------------------------------------------'''


def read_from_csv(filename):

    aqidatadict = dict()
    with open(filename, "r") as inputfile:
        reader = csv.reader(inputfile)
        for raw in reader :
            #print (raw)
            aqidatadict[raw[0]] = raw[1]
        #print (aqidatadict)
    return aqidatadict

'''----------------------------------------------------------------------exp----------------------------------------------------------------------'''

aqi_data = read_from_csv('aqi_data.csv')