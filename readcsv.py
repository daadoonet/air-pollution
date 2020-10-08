'''----------------------------------------------------------------------import----------------------------------------------------------------------'''

import csv
import pandas as pd

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

aqi_data_dict = read_from_csv('aqi_data.csv')
aqi_data_list = pd.read_csv('aqi_data.csv')
last7_data_list = pd.read_csv('aqi_data.csv',skiprows=len(aqi_data_list)-6)
last30_data_list = pd.read_csv('aqi_data.csv',skiprows=len(aqi_data_list)-29)

