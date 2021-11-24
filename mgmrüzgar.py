# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:51:46 2021

@author: muhammet.aydin
"""

import time
import os
from  selenium import webdriver
import pandas as pd
driver_path = os.getcwd() + "\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

link='https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il='


iller= ["Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", 
               "Artvin", "Aydın", "Balıkesir", "Bartın", "Batman", "Bayburt", "Bilecik", "Bingöl", "Bitlis", "Bolu", 
               "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Düzce", "Edirne", "Elazığ", 
               "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkâri", "Hatay", "Iğdır", 
               "Isparta", "İstanbul", "İzmir", "Kahramanmaraş", "Karabük", "Karaman", "Kars", "Kastamonu", "Kayseri", 
               "Kilis", "Kırıkkale", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", 
               "Mardin", "Mersin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", 
               "Şanlıurfa", "Siirt", "Sinop", "Sivas", "Şırnak", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van", 
               "Yalova", "Yozgat", "Zonguldak"]

url = [link + str(i) for i in iller]    

driver.get(url[0])
tah_tar1=driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(1) > td.ng-binding:nth-child(1)").text
tah_tar2=driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(2) > td.ng-binding:nth-child(1)").text
tah_tar3=driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(3) > td.ng-binding:nth-child(1)").text
tah_tar4=driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(4) > td.ng-binding:nth-child(1)").text
tah_tar5=driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(5) > td.ng-binding:nth-child(1)").text
tah_tar=[tah_tar1,tah_tar2,tah_tar3,tah_tar4, tah_tar5]

df_list= [0]*len(url)
def il(x):
    
    driver.get(url[x])
    time.sleep(0.35)
    tah_ruz1= driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(1) > td.ng-binding:nth-child(8)").text
    time.sleep(0.35)
    tah_ruz2= driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(2) > td.ng-binding:nth-child(8)").text
    time.sleep(0.25)                                              
    tah_ruz3= driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(3) > td.ng-binding:nth-child(8)").text
    time.sleep(0.25)                                             
    tah_ruz4= driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(4) > td.ng-binding:nth-child(8)").text
    time.sleep(0.25)                                            
    tah_ruz5= driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(5) > td.ng-binding:nth-child(8)").text
    time.sleep(0.25)                                             
    tah_ruz=[tah_ruz1,tah_ruz2,tah_ruz3,tah_ruz4, tah_ruz5]
    time.sleep(0.25)

    data = {'Ruzgar':tah_ruz}
    df_list[x]=pd.DataFrame(data)

[il(x) for x in range(0,len(url))]
driver.close()


df_list2 = pd.concat(df_list, axis=1)
df_list2.columns=iller
df_list2.index=tah_tar
df_list2.to_csv('Rüzgar_mgm.csv', encoding='utf-8-sig')  

