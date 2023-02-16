import pandas as pd
import datetime
from datetime import date
from send_demo import send_demo

def send_from_xlsx(filename):
    data = pd.read_excel(filename)
    data = data.sort_values(by="Time")
    times = list(data["Time"])
    tmp = []
    for i in times:
        if i not in tmp:
            tmp.append(i)
    times = tmp
    data.set_index('Time', inplace = True)
    i = 0
    while i < len(times):
        current_time = datetime.datetime.now()
        temp = times[i].split(":")
        hrs = int(temp[0])
        mins = int(temp[1])
        today = date.today()
        date_today = today.strftime("%m/%d/%Y")
        if current_time.hour == hrs and current_time.minute == mins:
            try:
                phone_num = list(data.loc[times[i]]["Phone"])
                user_id = list(data.loc[times[i]]["User ID"])
                start_date = list(data.loc[times[i]]["Start Date"])
                end_date = list(data.loc[times[i]]["End Date"])
                for j in range(len(phone_num)):
                    if date_today >= str(start_date[j]) and date_today <= str(end_date[j]):
                        send_demo(phone_num[j], times[i])
            except:
                phone_num = data.loc[times[i]]["Phone"]
                user_id = data.loc[times[i]]["User ID"]
                start_date = data.loc[times[i]]["Start Date"]
                end_date = data.loc[times[i]]["End Date"]
                if date_today >= str(start_date) and date_today <= str(end_date):
                    send_demo(phone_num, times[i])
            i+=1
    pass