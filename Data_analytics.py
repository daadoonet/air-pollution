
#just for test
#it must use in main.py
#from readcsv import *



'''----------------------------------------------------------------------import----------------------------------------------------------------------'''

import matplotlib.pyplot as plt

'''----------------------------------------------------------------------plot----------------------------------------------------------------------'''
def plot(data_list,title):
    plt.figure()
    plt.title(title)

    plt.plot( data_list['Date'], data_list['Pollution'] )

    plt.xlabel('Date')
    plt.ylabel('Pollution')
    return plt.show()

#plot(aqi_data_list.tail(7),'last 7 days')
#plot(aqi_data_list.tail(30),'last 30 days')
