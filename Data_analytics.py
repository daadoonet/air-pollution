
#just for test
#it must use in main.py
from readcsv import *



'''----------------------------------------------------------------------import----------------------------------------------------------------------'''

import matplotlib.pyplot as plt

'''----------------------------------------------------------------------plot----------------------------------------------------------------------'''
def plot(data_list,title):
    plt.figure()
    plt.title(title)

    plt.plot( data_list[0], data_list[1] )

    plt.xlabel('Date')
    plt.ylabel('Pollution')
    plt.show()

plot(last7_data_list,'last 7 days')
plot(last30_data_list,'last 30 days')


