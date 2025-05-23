from datetime import datetime
import shelve
import os
from decimal import Decimal, ROUND_DOWN
import json

# print(dir(datetime))
# print(datetime.today())
# print(datetime.now())


#what time is it?
# postpone task: # create match case

def run_CheckA(previous_timeStamp_Data, today_timeStamp_Data, final_outcome=False):
    def arbFunc_False(previous_timeStamp_Data, today_timeStamp_Data):
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
    def arbFunc_True(previous_timeStamp_Data, today_timeStamp_Data):
        #check two-time-stamps:
        # print(p := previous_timeStamp_Data) #un-commented: 3-9 12:34
        p = previous_timeStamp_Data
        # print(n := today_timeStamp_Data) #un-commented: 3-9 12:34
        n = today_timeStamp_Data
        # print(today.date())
        # print(today.time())
        # print(datetime.fromtimestamp(p))
        # print(datetime.fromtimestamp(n))
        pre_c = n-p
        c = Decimal.from_float(pre_c)
        precision = Decimal('0.01')
        c = c.quantize(precision, rounding=ROUND_DOWN)
        # print(c) #un-commented: 3-9 12:34
        denominator = Decimal.from_float(60.000)
        denominator = denominator.quantize(precision, rounding=ROUND_DOWN)
        # print(denominator) #un-commented: 3-9 12:34
        # print(c/denominator) #un-commented: 3-9 12:34
        # print(str(int((c/60)//60)) + "h", str(((c/60)%60)//1) + "m", str((((c/60)%60)%1)*60) + "s")
        # print(str(int((c/denominator)//denominator)) + "h", (((c/denominator)%denominator)),"m")
        precision = Decimal('0')
        seconds_calc = ((((c/60)%60)%1)*60)
        seconds_calc = seconds_calc.quantize(precision, rounding=ROUND_DOWN)
        # print(seconds_calc) #un-commented: 3-9 12:34
        print(str(int((c/60)//60)) + "h", str(((c/60)%60)//1) + "m", str(seconds_calc) + "s")
    if not final_outcome:
        arbFunc_False(previous_timeStamp_Data, today_timeStamp_Data)
    else:
        arbFunc_True(previous_timeStamp_Data, today_timeStamp_Data)



def definitionA(fileName_arg, run_CheckA__Switch = False, final_outcome = False):
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
            timeStamp_Data['timeStamp_Data'] = today.timestamp()
    else:
        with shelve.open(fileName) as timeStamp_Data:
            previous_timeStamp_Data = timeStamp_Data['timeStamp_Data']
    if run_CheckA__Switch:
        if previous_timeStamp_Data:
            run_CheckA(previous_timeStamp_Data, today_timeStamp_Data)
    print("")
def definitionB(fileName_arg, run_CheckA__Switch = False, final_outcome=False, close__Switch = False):
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
    # print(f"filename: {fileName_arg}")
    today = datetime.today()
    today_timeStamp_Data = today.timestamp() 
    fileName = fileName_arg
    objectFilePath = os.path.exists(fileName)
    if not objectFilePath:
        with shelve.open(fileName) as timeStamp_Data:
            timeStamp_Data['today'] = today
            timeStamp_Data['timeStamp_Data'] = today.timestamp()
    else:
        with shelve.open(fileName) as timeStamp_Data:
            previous_timeStamp_Data = timeStamp_Data['timeStamp_Data']
    if run_CheckA__Switch:
        if previous_timeStamp_Data:
            run_CheckA(previous_timeStamp_Data, today_timeStamp_Data, final_outcome)
    if close__Switch:
        with shelve.open(fileName) as openedFile:
            openedFile['time--delta'] = today_timeStamp_Data - previous_timeStamp_Data
            openedFile['close--time'] = today_timeStamp_Data
    print("")

def printNameFunc(fileName, printName):
    if printName:
        print(fileName)

def open_Data(fileName, printName=False):
    printNameFunc(fileName, printName)
    with shelve.open(fileName) as openFile:
        time__delta = openFile['time--delta']
        closing__time = openFile['close--time']
    return time__delta, closing__time

def open_Data_timeStamp(fileName, printName=False):
    printNameFunc(fileName, printName)
    with shelve.open(fileName) as openFile:
        timeStamp_Data = openFile['timeStamp_Data']
    return timeStamp_Data

#i need to migrate-data within shelve files.

def open_shelve_migrate(fileName):
    with shelve.open(fileName) as openFile:
        openFile['timeStamp_Data'] = openFile['time_StampData']
        print('file migrated')

#
# After migration, I need to remove old data: 'time_StampData
#

def open_shelf_generic(varA, varB, fileName, test=False):
    with shelve.open(fileName) as openFile:
        openFile[varA] = varB
        open_variable = openFile[varA]
    if test:
        print("openFile:,", open_variable)
#
#

def genericFunc():
    ...

def placeholder_data():
    return {
        "timesquare": 1, "newYork": 0, "california": 3, "sanFrancisco": 4,
        "losAngeles": 2, "sanDiego": 5, "washington": 6, "seattle": 7
    }

def jotDownTime_Now(fileName="testShelveFile_defaultFile__deleteLater_Anytime", data=None, add_on_Complete=False):
    print("fileName:", fileName)
    # redundant-use:
    today = datetime.today()
    timestamp = today.timestamp() 
    #
    with shelve.open(fileName) as openFile:
        allKeys = list(openFile.keys())
        # print-keys:
        print("allKeys:, ", allKeys)
        #
        if 'Checkpoint--counter' not in allKeys:
            openFile['Checkpoint--counter'] = 0
            currentCount = openFile['Checkpoint--counter']
        else: 
            currentCount = openFile['Checkpoint--counter']
            if add_on_Complete:
                currentCount += 1
        if currentCount < 10:
            openFile[f'checkpoint-0{currentCount}']= timestamp
        else:
            openFile[f'checkpoint-{currentCount}']= timestamp
        if add_on_Complete:
            currentCount +=1
            if currentCount < 10:
                openFile[f'checkpoint-0{currentCount}']= timestamp
            else:
                openFile[f'checkpoint-{currentCount}']= timestamp
        openFile['Checkpoint--counter'] = currentCount

    with shelve.open(fileName) as openFile:
        # second--print:
        allKeys = list(openFile.keys())
        # print-keys:
        print("allKeys:, ", allKeys)
        #
    
    # to-do:
    # 
    # check if json file exists, if not, create one.
    # otherwise, an error occurs

    ###
    #continue
    ###
    arbritra_Dict = {}
    with shelve.open(fileName) as openFile:
        for ea in allKeys:
            arbritra_Dict[ea] = str(openFile[ea])
    arbritra_keys = arbritra_Dict.keys()

    with open(f"{fileName}.json", "w") as jsonFile:
        processData = {}
        processData['cities-and_states'] = data
        for e in arbritra_keys:
            processData[e] = arbritra_Dict[e]
        json.dump(processData, jsonFile, indent=2)
    
    # print-entry for today, timeStamp_data, and checkpoint-00
    entries = arbritra_keys
    arbritra_List = []
    for i in entries:
        if not i == 'today':
            printThis = datetime.fromtimestamp(float(processData[i]))
        else:
            printThis = processData[i]
        arbritra_String = (i+":").ljust(22), str(processData[i]).rjust(34), str(printThis).rjust(30)
        arbritra_List.append(arbritra_String)
    arbritra_List.sort()
    for i in arbritra_List:
        print(i)
    




if __name__ == '__main__':
    definitionA("time_StampData", run_CheckA__Switch=True)
    # do not uncomment:
    # definitionB("2nd_break", run_CheckA__Switch = True, close__Switch = True)
    # do not uncomment:
    # definitionB("walking_timer_1", run_CheckA__Switch = True, close__Switch = True)
    # do not uncomment:
    # definitionB("arb_timer", run_CheckA__Switch=True, close__Switch=True)
    #
    time__delta, closing__time = open_Data("2nd_break", printName = True)
    print(time__delta)
    print(n := closing__time, "\n")
    timeStamp_Data = open_Data_timeStamp("2nd_break", printName=True)
    print(t := timeStamp_Data)
    print(n-t)
    #
    # One-Time use:
    # open_shelf_generic('time--delta', closing__time - timeStamp_Data, "2nd_break")
    #

    #
    # Moment-of-Truth:
    print("")
    run_CheckA(t, n)
    
    #
    #
    time__delta, closing__time = open_Data("walking_timer_1", printName = True)
    print(time__delta)
    print(n := closing__time, "\n")
    timeStamp_Data = open_Data_timeStamp("walking_timer_1", printName=True)
    print(t := timeStamp_Data)
    print(n-t)
    print("")
    run_CheckA(t, n)

    print("")
    # save-name: laziTimer_beforeSleep_3_8  # timer didn't save
    #
    # do not uncomment
    # definitionB("runSleepTimer", run_CheckA__Switch=True, close__Switch=True)

    #
    #
    time__delta, closing__time = open_Data("runSleepTimer", printName = True)
    print(time__delta)
    print(n := closing__time, "\n")
    timeStamp_Data = open_Data_timeStamp("runSleepTimer", printName=True)
    print(t := timeStamp_Data)
    print(n-t)
    print("")
    run_CheckA(t, n)

    #
    #
    print("")
    definitionB("dailyClock_3_9", run_CheckA__Switch=True, close__Switch=False)
    definitionB("./notWorking/notWorkingTimer01", run_CheckA__Switch=True, final_outcome=True, close__Switch=False)
    # time__delta, closing__time = open_Data("./notWorking/notWorkingTimer01", printName = True)
    # print(time__delta)
    # print(n := closing__time, "\n")
    timeStamp_Data = open_Data_timeStamp("./notWorking/notWorkingTimer01", printName=True)
    print(t := timeStamp_Data)

    # only-uncomment if true
    # print("")
    # jotDownTime_Now(
    #     "./notWorking/copy_notWorkingTimer01",
    #     placeholder_data(),
    #     add_on_Complete = False)

    definitionB("./washingMachine/washingMachineBreakTimer01", run_CheckA__Switch=True, final_outcome=True, close__Switch=False)
    print("")
    jotDownTime_Now(
        "./washingMachine/washingMachineBreakTimer01",
        placeholder_data(),
        add_on_Complete = False)

    definitionB("./3-09/timerRightBeforeSleep", run_CheckA__Switch=True, final_outcome=True, close__Switch=False)
    jotDownTime_Now(
        "./3-09/timerRightBeforeSleep",
        placeholder_data(),
        add_on_Complete = False)

    definitionB("./3-10/wokeUp-Today", run_CheckA__Switch=True, final_outcome=True, close__Switch=False)
    jotDownTime_Now(
        "./3-10/wokeUp-Today",
        placeholder_data(),
        add_on_Complete = False)

    definitionB("./3-10/2ndTimer-ContemplatingOfCleaningMyRoom", run_CheckA__Switch=True, final_outcome=True, close__Switch=False)
    jotDownTime_Now(
        "./3-10/2ndTimer-ContemplatingOfCleaningMyRoom",
        placeholder_data(),
        add_on_Complete = False)

    definitionB("./3-10/Go-ToMyRoom", run_CheckA__Switch=True, final_outcome=True, close__Switch=False)
    jotDownTime_Now(
        "./3-10/Go-ToMyRoom",
        placeholder_data(),
        add_on_Complete = False)

    definitionB("./3-15/Take-a-break", run_CheckA__Switch=True, final_outcome=True, close__Switch=False)
    jotDownTime_Now(
        "./3-15/Take-a-break",
        placeholder_data(),
        add_on_Complete = False)


    #
    # I was able to successfully migrate: time_StampData, 2nd_break, arb_timer
    # and break_timer, newly-migrated: walking_timer_1
    #
    #
    # Migrate-successful: 21:45
    #
    # I made an error with shelve data  # timeStamp_Data or 
    # time_StampData   #crisis-averted


