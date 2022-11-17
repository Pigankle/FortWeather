#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:23:48 2019

@author: chinkapin
"""
import os
import pandas as pd

recType = ""
statID = ""
metElType = ""
metUnits = ""
year = ""
month = ""
timeInterval = ""
filler = 99
readingCt = ""
obsDayOfMonth = ""
obsHour = ""
obsSign = ""
obsValue = ""
obsQC1 = ""
obsQC2 = ""
data_dir = 'Data/'  # enter relative path to data directory, including "/" as necessary
# %%  Lookup Dictonaries
cloud_Dct = {'00': 'Missing', '0C': 'Cirrus', '0K': 'Cumulus', 'ST': 'Stratus',
             'CC': 'Cirro-cumulus', 'CS': 'Cirro-stratus', 'KS': 'Cumulo-stratus',
             'KN': 'Cumulo-nimbus', '0N': 'Nimbus', 'NS': 'Nimbo-stratus', '3': 'clouds',
             '1': 'clear', 'HZ': 'haze', 'HF': 'highfog', 'SM': 'smoky', 'SD': 'scudd',
             '99': 'Missing', '0R': 'Rain', '0T': 'thunderstorm', '0S': 'Snow',
             '0D': 'drizzle/mist', '0E': 'Sleet', '0G': 'Glaze', '0H': 'Hail', '0I': 'Ice',
             '0M': 'mixed - rain and snow', '0W': 'squalls/showers/sprinkles', '0F': 'Fog',
             '0X': 'Dew', '0Z': 'Frost'}
PTYP_Dct = {'R': 'Rain', 'T': 'thunderstorm', 'S': 'Snow', 'D': 'drizzle/mist', 'E': 'Sleet',
            'G': 'Glaze', 'H': 'Hail', 'I': 'Ice', 'M': 'mixed - rain and snow',
            'W': 'squalls/showers/sprinkles', 'F': 'Fog', 'X': 'Dew', 'Z': 'Frost', '9': 'Missing'}
DYSW_STWX_Dct = {'01': 'Clear', '02': 'Partly Cloudy', '03': 'Clouds', '04': 'Rain', '05': 'Snow',
                 '06': 'Smoke/haze', '07': 'Fog', '08': 'Drizzle(mist)', '09': 'Sleet',
                 '10': 'Glaze', '11': 'Thunder', '12': 'Hail', '13': 'Duststorm',
                 '14': 'Blowing snow', '15': 'Highwind', '16': 'Tornado', '17': 'Fair',
                 '18': 'Squalls', '19': 'Frost',  '20': 'Mixed rain andsnow',
                 '21': 'Dew', '99': 'Illegible'}
units_Dict = {'HF': 'Hundredths of degrees Fahrenheit', ' I': 'Inches', 'TI': 'Tenths of an inch',
              'HI': 'Hundredths of inches', 'IT': 'Thousandths of inches of mercury',
              'MH': 'Miles per hour', ' M': 'Whole miles', 'NA': 'No units', 'DG': 'whole degrees',
              'TN': 'Scale of 0 to 10', 'WN': 'Scale of 0 to 12', 'PC': 'Whole percent',
              'TP': 'Tenths of a percent', 'TG': 'Tenths of feet'}
station_Dct = {"04763099": "Sacramento",    "04774099": "SanDiego",   "45297699": "FortSteilacoom",
               "45877399": "FortVancouver", "45297799": "FortWallaWalla"}

# %%

readinglist = []
rowList = []
for file in os.listdir(data_dir):
    if file.endswith(".dat"):

        # with open('AllDatFiles.dat') as f:
        with open(data_dir+file) as f:
            for thisRow in f:
                # print line
                # for thisRow in sampleText:
                #    recType = thisRow[0:3]
                #    statID = thisRow[3:11]
                statName = file[:-9]
                metElType = thisRow[11:15]

# Only Store the Values we care about
                # (metElType in ['DYSW', 'STWX', "PTYP","CLTL","CLTU"]):
                if True:

                    metUnits = thisRow[15:17]
                    year = thisRow[17:21]

                    month = thisRow[21:23]
                    timeInterval = thisRow[23:25]
                    filler99 = thisRow[25:27]
                    readingCt = int(thisRow[27:30])
                    AECode = thisRow[30+(readingCt)*12: 30+(readingCt)*12+8]
                    afterSlash = thisRow[30 +
                                         (readingCt)*12+9: 30+(readingCt)*12+16]

                    # ((int(year)==1861 and int(month)<9) or
                    # (int(year)==1862 and int(month)<7)) :# and int(year) > 1860 :
                    if True:

                        #                    dict2 = { "statID": statID, "statName" : statName ,"metElType": metElType , "metUnits": metUnits, "year": year,  "month": month,  "timeInterval": timeInterval,  "readingCt": readingCt,  "fullRow":thisRow}
                        dict2 = {"statName": statName, "metElType": metElType,
                                 "metUnits": metUnits, "year": year,  "month": month, }
                        rowList.append(dict2)

                        for obs in range(0, readingCt):
                            dict1 = {}
                            offset = 30 + (obs)*12
                            obsDayOfMonth = thisRow[offset: offset+2]
                            obsHour = thisRow[offset + 2: offset+4]
                            obsValue = thisRow[offset + 4: offset+10]

                            if metElType == "PTYP":
                                obsValue = PTYP_Dct[obsValue[-1]]

                            if metElType in ['DYSW', 'STWX']:
                                obsValue = DYSW_STWX_Dct[obsValue[-2:]]

                            if metElType in ["CLTL", "CLTU"]:
                                obsValue = cloud_Dct[obsValue[-2:]]

                            obsQC1 = thisRow[offset+10: offset+11]
                            obsQC2 = thisRow[offset+11: offset+12]

#                        if obsHour == 7:
#                            #
#                        if obsHour == 14:
#                            #
#                        if obsHour == 21:
#                            #
#                        if obsHour == 99:
#                            #

                            dict1 = {"statName": statName, "metElType": metElType,
                                     "metUnits": metUnits, "year": year,  "month": month,
                                     "timeInterval": timeInterval,
                                     "readingCt": readingCt,  "obsDayOfMonth": obsDayOfMonth,
                                     "obsHour": obsHour,  "obsValue": obsValue,  "obsQC1": obsQC1,
                                     "obsQC2": obsQC2}

                        readinglist.append(dict1)

                        if 'str' in thisRow:
                            break

df = pd.DataFrame(columns=['statID', 'statName', 'metElType', 'metUnits', 'year', 'month',
                           'timeInterval', 'filler99readingCt', 'obsDayOfMonth', 'obsHour',
                           'obsSign', 'obsValue', 'obsQC1', 'obsQC2', 'AECode', 'afterSlash',
                           'fullRow'])

df = pd.DataFrame(readinglist)
readingListColumnsTitles = ["statID", "statName", "metElType", "metUnits",   "timeInterval",
                            "readingCt", "year", "month",  "obsDayOfMonth", "obsHour",  "obsValue",
                            "obsQC1",  "obsQC2", "AECode", "afterSlash", "fullRow"]
df = df.reindex(columns=readingListColumnsTitles)
df.to_csv("ParsedDataWide-FDPW.csv", sep=',')

df_rows = pd.DataFrame(columns=['statID', 'statName', 'metElType', 'metUnits', 'year', 'month',
                                'timeInterval', 'filler99readingCt', 'FullRow'])
df_rows = pd.DataFrame(rowList)
rowListColumnsTitles = ["statID", "statName", "metElType", "metUnits", "timeInterval",
                        "readingCt", "year",  "month",  "fullRow"]
df_rows = df_rows.reindex(columns=rowListColumnsTitles)
df_rows.to_csv("TargetRowsWide-FDPW.csv", sep=',')
