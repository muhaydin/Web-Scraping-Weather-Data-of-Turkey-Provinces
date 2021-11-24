# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:50:00 2021

@author: muhammet.aydin
"""

from  selenium import webdriver
import pandas as pd
import os
import time
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
    tah_sıc_max1=driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(1) > td.ng-binding:nth-child(4)").text
    time.sleep(0.35)
    tah_sıc_max2=driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(2) > td.ng-binding:nth-child(4)").text
    time.sleep(0.35)
    tah_sıc_max3=driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(3) > td.ng-binding:nth-child(4)").text
    time.sleep(0.35)
    tah_sıc_max4=driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(4) > td.ng-binding:nth-child(4)").text
    time.sleep(0.35)
    tah_sıc_max5=driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(5) > td.ng-binding:nth-child(4)").text
    time.sleep(0.35)
    tah_sıc_max= [tah_sıc_max1,tah_sıc_max2,tah_sıc_max3,tah_sıc_max4, tah_sıc_max5]
    time.sleep(0.35)

    tah_sıc_min1=driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(1) > td.ng-binding:nth-child(3)").text
    time.sleep(0.35)
    tah_sıc_min2=driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(2) > td.ng-binding:nth-child(3)").text
    time.sleep(0.35)
    tah_sıc_min3=driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(3) > td.ng-binding:nth-child(3)").text
    time.sleep(0.35)
    tah_sıc_min4=driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(4) > td.ng-binding:nth-child(3)").text
    time.sleep(0.35)
    tah_sıc_min5=driver.find_element_by_css_selector("#_4_5gunluk > table > tbody > tr:nth-child(5) > td.ng-binding:nth-child(3)").text
    time.sleep(0.35)
    tah_sıc_min=[tah_sıc_min1,tah_sıc_min2,tah_sıc_min3,tah_sıc_min4, tah_sıc_min5]
    
    data = {'Sıcaklık_max':tah_sıc_max, 'Sıcaklık_min':tah_sıc_min}
    df_list[x]=pd.DataFrame(data)

[il(x) for x in range(0,len(url))]
driver.close()


df_list2 = pd.concat(df_list, axis=1)
iller2=sorted(iller*2)
mins = '_min'
maxs = '_max'
iller_colname=[0]*len(iller2)
for i in range(0,len(iller2)):
    if i%2==0:
        iller_colname[i]=iller2[i]+maxs
    else:
        iller_colname[i]=iller2[i]+mins        
df_list3 = df_list2.set_axis(iller_colname, axis=1)
df_list3.index=tah_tar
df_list3.to_csv('Sıcaklık_mgm.csv', encoding='utf-8-sig')  
