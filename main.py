import MainModule as Bot
import re

listApp = ['google','Google','chrome','Chrome','word','Word','winword','Winword','powerpoint','PowerPoint']
listFunction = ['giờ','ngày','tháng','năm']
listFunction2 = ['âm lượng','volumne']

Request = "âm lượng 90"
for lstapp in listApp:
    if lstapp in Request:
        Bot.open_application_multi(Request)
for lstfunction in listFunction:
    if lstfunction in Request:
        Bot.get_time(Request)
for lstfunction2 in listFunction2:
    if lstfunction2 in Request:
        match = re.search(r'\d+', Request)
        volume_str = match.group()
        volume = int(volume_str)
        Bot.controlVolumn(volume)   
    


