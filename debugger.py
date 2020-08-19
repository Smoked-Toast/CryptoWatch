from bin.CSV_Converter import *

def GetRunVal():
    list = Convert("Kill.csv")
    return list[0][0]

def CheckKillSwitch():
    val = GetRunVal()
    if val == "False":
        return False
    else:
        return True