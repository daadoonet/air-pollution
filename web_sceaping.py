
'''----------------------------------------------------------------------import----------------------------------------------------------------------'''

import re
import requests
from bs4 import BeautifulSoup
import csv

'''----------------------------------------------------------------------request----------------------------------------------------------------------'''

def request():

    url = 'http://airnow.tehran.ir'



    try:
        json = requests.get(url)
        soup = BeautifulSoup(json.text, 'html.parser')
        last_day_and_now = soup.find_all('span',attrs={"class":"info-box-number aqival"})
    except:
        print('sorry I can not connect to airnow.tehran.ir' )



    try:
        json = requests.get(url)
        soup = BeautifulSoup(json.text, 'html.parser')
        year_info = (soup.find_all('div',attrs={"id":"ContentPlaceHolder1_CountDay"}))
    except:
        print('sorry I can not connect to airnow.tehran.ir' )
    


    return last_day_and_now, year_info

'''----------------------------------------------------------------------regex----------------------------------------------------------------------'''

def regex(html1,html2):

    last_day_info = int(re.findall(r">(\d*)<", str(html1[0]))[0])
    now_info = int(re.findall(r">(\d*)<", str(html1[1]))[0])
    year_info = (re.findall(r"days=(\d*)", str(html2)))
    return last_day_info,now_info,year_info

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

'''----------------------------------------------------------------------year-info-dict----------------------------------------------------------------------'''

def year_info_dict(year_info):
    dictionary = dict()
    dictionary['clean'] = year_info[0]
    dictionary['acceptable'] = year_info[1]
    dictionary['Unhealthy for sensitive groups'] = year_info[2]
    dictionary['Unhealthy'] = year_info[3]
    dictionary['Very unhealthy'] = year_info[4]
    dictionary['Dangerous'] = year_info[5]

    return(dictionary)

'''----------------------------------------------------------------------TEST----------------------------------------------------------------------'''

last_day_and_now, year_info = request()
#    print(year_info)
#    print('html is: ' , last_day_and_now)
last_day_info,now_info,year_info = regex(last_day_and_now,year_info)
#    print('last_day_info is: ' , last_day_info)
#    print('now_info is: ' , now_info)
aqi_data = read_from_csv('aqi_data.csv')
year_info = year_info_dict(year_info)
#    print(year_info)
