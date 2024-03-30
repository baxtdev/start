from datetime import time,date,datetime
 
_today = date.today()
_today_ = datetime.now().time()
_time = time()

 
print("Seconds since epoch =", _today,"\n",_today_,"\n",_time)


deadline = datetime.strptime("22/05/2017", "%d/%m/%Y")
print(deadline)     # 2017-05-22 00:00:00
 
deadline = datetime.strptime("22/05/2017 12:30", "%d/%m/%Y %H:%M")
print(deadline)     # 2017-05-22 12:30:00
 
deadline = datetime.strptime("05-22-2017 12:30", "%m-%d-%Y %H:%M")
print(deadline)     # 2017-05-22 12:30:00