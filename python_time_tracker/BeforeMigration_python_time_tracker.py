from datetime import datetime
import shelve
import os
from decimal import Decimal, ROUND_DOWN

# print(dir(datetime))
# print(datetime.today())
# print(datetime.now())


#what time is it?
# postpone task: # create match case

def run_CheckA(previous_timeStamp_Data, today_timeStamp_Data):
    #check two-time-stamps:
    print(p := previous_timeStamp_Data)
    print(n := today_timeStamp_Data)
    # print(today.date())
    # print(today.time())
    # print(datetime.fromtimestamp(p))
    # print(datetime.fromtimestamp(n))
    pre_c = n-p
    c = Decimal.from_float(pre_c)
    precision = Decimal('0.01')
    c = c.quantize(precision, rounding=ROUND_DOWN)
    print(c)
    denominator = Decimal.from_float(60.000)
    denominator = denominator.quantize(precision, rounding=ROUND_DOWN)
    print(denominator)
    print(c/denominator)
    # print(str(int((c/60)//60)) + "h", str(((c/60)%60)//1) + "m", str((((c/60)%60)%1)*60) + "s")
    # print(str(int((c/denominator)//denominator)) + "h", (((c/denominator)%denominator)),"m")
    precision = Decimal('0')
    seconds_calc = ((((c/60)%60)%1)*60)
    seconds_calc = seconds_calc.quantize(precision, rounding=ROUND_DOWN)
    print(seconds_calc)
    print(str(int((c/60)//60)) + "h", str(((c/60)%60)//1) + "m", str(seconds_calc) + "s")



def definitionA(fileName_arg, run_CheckA__Switch = False):
    #initial-variables:
    previous_timeStamp_Data = None
    #
    print(f"filename: {fileName_arg}")
    today = datetime.today()
    today_timeStamp_Data = today.timestamp() 
    fileName = fileName_arg
    objectFilePath = os.path.exists(fileName)
    if not objectFilePath:
        with shelve.open(fileName) as timeStamp_Data:
            timeStamp_Data['today'] = today
            timeStamp_Data['time_StampData'] = today.timestamp()
    else:
        with shelve.open(fileName) as timeStamp_Data:
            previous_timeStamp_Data = timeStamp_Data['time_StampData']
    if run_CheckA__Switch:
        if previous_timeStamp_Data:
            run_CheckA(previous_timeStamp_Data, today_timeStamp_Data)
    print("")
def definitionB(fileName_arg, run_CheckA__Switch = False, close__Switch = False):
    #initial-variables:
    previous_timeStamp_Data = None
    #
    if close__Switch:
        try:
            with shelve.open(fileName) as openedFile:
                if openedFile['time--delta']:
                    print("file-exists---do-not-continue")
                # I need to create a switch that turns stuff off.
            # I need to create a switch that does not
            # run the function when this variable exists.
            # "" openedFile['time--delta'] ""
        except UnboundLocalError:
            print("UnboundLocalError")
    print(f"filename: {fileName_arg}")
    today = datetime.today()
    today_timeStamp_Data = today.timestamp() 
    fileName = fileName_arg
    objectFilePath = os.path.exists(fileName)
    if not objectFilePath:
        with shelve.open(fileName) as timeStamp_Data:
            timeStamp_Data['today'] = today
            timeStamp_Data['time_StampData'] = today.timestamp()
    else:
        with shelve.open(fileName) as timeStamp_Data:
            previous_timeStamp_Data = timeStamp_Data['time_StampData']
    if run_CheckA__Switch:
        if previous_timeStamp_Data:
            run_CheckA(previous_timeStamp_Data, today_timeStamp_Data)
    if close__Switch:
        with shelve.open(fileName) as openedFile:
            openedFile['time--delta'] = previous_timeStamp_Data - today_timeStamp_Data
            openedFile['close--time'] = today_timeStamp_Data
    print("")

def printNameFunc(fileName, printName):
    if printName:
        print(fileName)

def open_Data(fileName, printName = False):
    printNameFunc(fileName, printName)
    if printName:
        print(fileName)
    with shelve.open(fileName) as openFile:
        time__delta = openFile['time--delta']
        closing__time = openFile['close--time']
    return time__delta, closing__time

def open_Data_timeStamp(fileName, printName = False):
    printNameFunc(fileName, printName)
    with shelve.open(fileName) as openFile:
        timeStamp_Data = openFile['time_StampData']
    return timeStamp_Data

#i need to migrate-data within shelve files.

def open_shelve_migrate(fileName):
    with shelve.open(fileName) as openFile:
        openFile['timeStamp_Data'] = openFile['time_StampData']
        print('file migrated')

#
# After migration, I need to remove old data: 'time_StampData
#

if __name__ == '__main__':
    # pause-only once
    # definitionA("time_StampData", run_CheckA__Switch = True)
    #
    # do not uncomment:
    # definitionB("2nd_break", run_CheckA__Switch = True, close__Switch = True)
    # do not uncomment:
    # definitionB("walking_timer_1", run_CheckA__Switch = True, close__Switch = True)
    # pause only once
    # definitionB("arb_timer", run_CheckA__Switch = True)
    # time__delta, closing__time = open_Data("2nd_break", printName = True)
    # print(time__delta)
    # print(n := closing__time, "\n")
    # timeStamp_Data = open_Data_timeStamp("2nd_break", printName=True)
    # print(t := timeStamp_Data)
    # print(n-t)
    #
    #
    # I was able to successfully migrate: time_StampData, 2nd_break, arb_timer
    # and break_timer
    #
    # open_shelve_migrate('time_StampData')
    # open_shelve_migrate('2nd_break')
    # open_shelve_migrate('arb_timer')
    # open_shelve_migrate('break_timer')
    #
    #File migrated. 
    #
    # I made an error with shelve data  # timeStamp_Data or 
    # time_StampData   #crisis-averted


