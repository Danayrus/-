##import requests
##a = requests.get("https://cbr.ru/scripts/XML_daily.asp?date_req=31/03/2023")
##print(a.text)
import pandas as pd
#url = 'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=31/03/2023&date_req2=01/04/2023&VAL_NM_RQ=R01235'
day = input("Введите день")
month = input("Введите месяц (числом)")
year = input("Введите год")
a = day+'/'+month+'/'+year
url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='+a
print(pd.read_xml(url,encoding='cp1251'))

