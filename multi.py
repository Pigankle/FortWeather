#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:23:48 2019

@author: chinkapin
"""
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt

recType = ""
statID = ""
readingType = ""
metUnits = ""
year = ""
month= ""
timeInterval= ""
filler = 99
readingCt = ""
obsDayOfMonth = ""
obsHour= ""
obsSign= ""
obsValue= ""
obsQC1 =""
obsQC2="" 
storeReading = True

tableC_Clouds=  {'0C':'Cirrus','0K':'Cumulus','ST':'Stratus','CC':'Cirro-cumulus','CS':'Cirro-stratus','KS':'Cumulo-stratus','KN':'Cumulo-nimbus','0N':'Nimbus','NS':'Nimbo-stratus','3':'clouds','1':'clear','HZ':'haze','HF':'highfog','SM':'smoky','SD':'scudd','99':'Missing','0R':'Rain','0T':'thunderstorm','0S':'Snow','0D':'drizzle/mist','0E':'Sleet','0G':'Glaze','0H':'Hail','0I':'Ice','0M':'mixed - rain and snow','0W':'squalls/showers/sprinkles','0F':'Fog','0X':'Dew','0Z':'Frost',}
tableE_precipType =  {'R':'Rain','T':'thunderstorm','S':'Snow','D':'drizzle/mist','E':'Sleet','G':'Glaze','H':'Hail','I':'Ice','M':'mixed - rain and snow','W':'squalls/showers/sprinkles','F':'Fog','X':'Dew','Z':'Frost','9':'Missing'}
tableD_WeatherType=  {'01':'Clear','02':'Partly Cloudy','03':'Clouds','04':'Rain','05':'Snow','06':'Smoke/haze','07':'Fog','08':'Drizzle(mist)','09':'Sleet','10':'Glaze','11':'Thunder','12':'Hail','13':'Duststorm','14':'Blowing snow','15':'Highwind','16':'Tornado','17':'Fair','18':'Squalls','19':'Frost','20':'Mixed rain andsnow','21':'Dew','99':'Illegible',}
statDict = {"04763099" :"Sacramento","04774099":"SanDiego","45297699":"FortSteilacoom" , "45877399": "FortVancouver","45297799":"FortWallaWalla"}



startYear  = 1861
startMonth = 12
endYear = 1862
endMonth = 2
outFileName = str(startMonth)+str(startYear)+"--"+str(endMonth)+str(endYear)+"-multi.csv"

readinglist=[]
rowList = []
for file in os.listdir():
    if file.endswith(".dat"):
        

    #with open('AllDatFiles.dat') as f:
        with open(file) as f:
            stationName = file[:-9]
            for thisRow in f:
                statID = thisRow[3:11]        #print line      
                
        #for thisRow in sampleText:
                readingType = thisRow[11:15]

                #Only Store the Values we care about
                if (readingType in ['PRCP','TAHR']):
                    storeReading = True
                else:
                    storeReading = False

                if storeReading==True:
                    metUnits = thisRow[15:17]
                    year = thisRow[17:21]           
                    month= thisRow[21:23]
    
                    readingCt = int(thisRow[27:30])
                    
                    if ((int(year)==startYear and int(month)>= startMonth) or ( int(year)==endYear and int(month)<=endMonth )) :# and int(year) > 1860 :
                      
                        dict2 = {"recType":recType, "statID": statID, "stationName" : stationName ,"readingType": readingType , "metUnits": metUnits, "year": year,  "month": month,  "timeInterval": timeInterval,  "readingCt": readingCt,  "fullRow":thisRow}
                        rowList.append(dict2)
                        
                        for obs in range(0,readingCt) :
                            dict1 = {}
                            offset = 30 + (obs)*12
                            obsHour       = thisRow[offset+ 2 : offset+4]
                            obsDayOfMonth = thisRow[offset    : offset+2]
                                            
    
                            obsValue      = thisRow[offset+ 4 : offset+10]
    
    #CONVERSION BASED ON UNITS AND TYPE
                            if metUnits == "HI" :
                                # Convert hundredths of an inch to inches
                                obsValue = float(obsValue)
                                obsValue = obsValue/100.0  
                                outUnits = "inches"
                            elif metUnits == "IT" :
                                #Convert in mercury into Bar
                                obsValue = float(obsValue)
                                obsValue = obsValue/29.53
                                outUnits = "bar"
                            elif metUnits == "HF" :
                                #convert hundredths of a degree fahrenheit into whole degrees
                                obsValue = float(obsValue)
                                obsValue = obsValue /100.0
                                outUnits = "F"
                            elif metUnits == "DG" :
                                #Whole degrees  - no change
                                obsValue = float(obsValue)
                                outUnits = "deg"
                                pass
                            elif metUnits == "TN" :
                                # change 0-10 scale to 0-1 scale
                                obsValue = float(obsValue)
                                obsValue = obsValue / 10.0
                                outUnits = "[-]"
                            elif metUnits == "MH" :
                                #Do not change mph
                                obsValue = float(obsValue)
                                outUnits = "mph"
                                pass
                            elif metUnits == "TP" :
                                # Change tenths of a percent to percent
                                obsValue = float(obsValue)
                                obsValue = obsValue / 10.0
                                outUnits = "%"
                            elif metUnits == "NA" :
                                # NA - no units
                                if readingType == "CLTL" :
                                    #Cloud Cover Type - Table C
                                    obsValue = tableC_Clouds[obsValue[-2:]]
                                elif readingType == "CLTU" :
                                    #Cloud Cover Type - Table C
                                    obsValue = tableC_Clouds[obsValue[-2:]]                                
                                elif readingType == "DYSW" :
                                    #Weather type - Table D
                                    obsValue = tableD_WeatherType[obsValue[-2:]]
                                elif readingType == "PTYP" :
                                    #Precip Type - Table E
                                    obsValue = tableE_precipType[obsValue[-1]]                                
                                elif readingType == "STWX" :
                                    #State of the Weather - Table D
                                    obsValue = tableD_WeatherType[obsValue[-2:]]                        
                                elif readingType == "TPBG" :
                                    #TimePrecipBegins
                                    pass
                                elif readingType == "TPEN" :
                                    #TimePrecipEnds
                                    pass
                                pass
                            
                      #      print(obsValue)
                            morNoNi = ""
                            summaryTag = ""
                            if float(obsDayOfMonth) == 32:
                                summaryTag = "_sum"
                            if float(obsDayOfMonth) == 33:
                                summaryTag = "_avg"    
                            if int(obsHour) < 25:
                                morNoNi = "_"+obsHour
                            if float(obsDayOfMonth) <=31:
                                if float(obsHour) <99 :
                                    dt = datetime.fromisoformat(year +"-"+ month +"-"+ obsDayOfMonth +" "+ obsHour +":00:00" )
                                else:
                                    dt = datetime.fromisoformat(year +"-"+ month +"-"+ obsDayOfMonth)
                                    
                                    
                            
                            readingType = thisRow[11:15]+morNoNi+summaryTag
    
                            
                            obsQC1        = thisRow[offset+10 : offset+11]
                            obsQC2        = thisRow[offset+11 : offset+12] 
                            numObs = ""
                            textObs = ""
                            if not (metUnits == "NA"):
                                numObs = obsValue
    #                            print(obsValue)
                            else :
                                textObs = obsValue
                            if obsQC1 == "M":
                                textObs = "Missing"
                                numObs =""
                                obsValue = "-"
                            dict1 = { "stationName" : stationName ,"readingType": readingType , "metUnits": outUnits, "year": float(year)+1000,  "month": month,    "obsDayOfMonth": obsDayOfMonth, "obsHour": obsHour,  "obsValue": obsValue,"numObs": numObs,  "obsQC1": obsQC1,  "obsQC2": obsQC2, "dt":dt, "YY-MM": year+"-"+month, "YY-MM-DD": year+"-"+month+"-"+obsDayOfMonth, "textObs":textObs, "thisRow":thisRow}
                            
        
                            readinglist.append(dict1)
                        
                        
                        if 'str' in thisRow:
                          break

df=pd.DataFrame(columns=['stationName','readingType' ,'metUnits' , 'year' , 'month'   , 'obsDayOfMonth' , 'obsHour'  , 'obsValue' , 'numObs', 'obsQC1' , 'obsQC2',"dt", "YY-MM", "YY-MM-DD", "textObs"  ])#     , "thisRow"])

df = pd.DataFrame(readinglist)    
readingListColumnsTitles = [  "stationName" , "readingType" , "metUnits","year",  "month",  "obsDayOfMonth", "obsHour",  "obsValue", "numObs", "obsQC1",  "obsQC2","dt", "YY-MM", "YY-MM-DD", "textObs"   ]#    , "thisRow"]
df = df.reindex(columns=readingListColumnsTitles)


df.to_csv("output"+outFileName, sep=',')

df.set_index('dt', inplace = True)
plt.figure()

plotPRCP = df[df['readingType'].str.contains('PRCP')]
plotPRCP = plotPRCP[plotPRCP['stationName'].str.contains('cisco')]
plotPRCP = plotPRCP[pd.to_numeric(plotPRCP.obsDayOfMonth ) < 32]
axPRCP = plotPRCP.plot.bar(  y = 'numObs')#,marker = "o")

plt.figure()

plotTAHR = df[df['readingType'].isin(['TAHR_07','TAHR_14','TAHR_21']) ].interpolate()
plotTAHR = plotTAHR[plotTAHR['stationName'].str.contains('cisco')]
plotTAHR = plotTAHR[~plotTAHR['obsQC1'].str.contains("M")]
plotTAHR.interpolate().plot(  y = 'numObs',linestyle = "-") 

plotTAHR.interpolate().plot(  y = 'numObs',linestyle = "-", ax = axPRCP) 
