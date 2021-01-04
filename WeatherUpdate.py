import schedule 
import time 
import smtplib
import requests
from bs4 import BeautifulSoup
import re
#function that webscraps the value of temprature from the website
def findtemp():

    URL='https://www.accuweather.com/en/in/bengaluru/204108/current-weather/204108'

    headers={
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }

    page= requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    
    title=soup.find('li', {"class": re.compile("^([A-Z]*[a-z]* fday1 *)")})
    title2=title.find('span', {'class': 'large-temp'})
    title3=title.find('span', {'class': 'cond'})
    title4=title2.text.strip()
    title5=title3.text.strip()
    finalstring=(title4+title5)
   
    sendmyemail(finalstring)
#function to send email 
def sendmyemail(finalstring):
   
    print(finalstring)
    mymsg=(finalstring).encode('utf-8').strip()
   
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
   
    server.ehlo()
 
    server.login('senders email id','password')
    subject='your daily temperature update'
    body='Todays temperature:'
   
    msg2=(finalstring).encode('utf-8').strip()
    server.sendmail(
        'senders email id',
        'receivers email id',
        msg2
        )

    print('email sent')
    server.quit()   

              

  
# Task scheduling to send email everyday at 7 am
 

schedule.every().day.at("07:00").do(findtemp) 
 
# keeps on running all time. 
while True: 
  
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    time.sleep(1) 