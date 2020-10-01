
'''----------------------------------------------------------------------import----------------------------------------------------------------------'''

import re
import requests
from bs4 import BeautifulSoup

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

'''----------------------------------------------------------------------exp----------------------------------------------------------------------'''

last_day_and_now, year_info = request()
last_day_info,now_info,year_info = regex(last_day_and_now,year_info)
year_info = year_info_dict(year_info)
