from datetime import datetime
import shelve
import os

# print(dir(datetime))
# print(datetime.today())
# print(datetime.now())


#what time is it?

today = datetime.today()
today_time_StampData = today.timestamp()
fileName = "time_StampData"
objectFilePath = os.path.exists(fileName)
if not objectFilePath:
    with shelve.open(fileName) as time_StampData:
        time_StampData['today'] = today
        time_StampData['time_StampData'] = today.timestamp()
else:
    with shelve.open(fileName) as time_StampData:
        previous_time_StampData = time_StampData['time_StampData']
#check two-time-stamps:
print(p := previous_time_StampData)
print(n := today_time_StampData)
print(today.date())
print(today.time())
print(p)
print(n)

