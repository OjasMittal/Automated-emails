import  yagmail
import pandas
from main import Newsfeed
import datetime
import time
while True:
    if datetime.datetime.now().hour== 9 and datetime.datetime.now().minute==15:
        df=pandas.read_excel('people.xlsx')
        for index,row in df.iterrows():
            news_feed=Newsfeed(interest=row['interest'],
                               from_date=(datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                               to_date=datetime.datetime.now().strftime('%Y-%m-%d'))
            email=yagmail.SMTP(user="automail.ojas.python@gmail.com",password="ojaspython123")
            email.send(to=row['email'],
                       subject=f"your {row['interest']} news for today",
                       contents=f"Hi {row['name']}\n Check out todays news on {row['interest']} \n Do not reply back to this email \n\n {news_feed.get()}\nOjas")

    time.sleep(60)
