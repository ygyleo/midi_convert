# -*- coding: utf-8 -*-
#midi to csv
import py_midicsv as pm
import csv
import os
import sys

filepathin = r'.\IN_csv'
csvpath = r'.\OUT_csv'
pathdir=os.listdir(filepathin)

def convert(file) :
    #Load the MIDI file and parse it into CSV format
    csv_string = pm.midi_to_csv(filepathin+"\\\\"+file)
    
    # load the data in csv
    str1 = ''.join(csv_string)
    array = []
    array1 = []
    array2 = [] # all the info in midi
    csv_array = [] # final array
    array = str1.split('\n')
    for item in array:
        array1 = item.split(', ') 
        array2.append(array1)
    #print(array2)
    for row in array2:
        row[1] = int(row[1])
        if row[2] == 'Time_signature': # time and time signature
            row[3] = int(row[3])
            row[4] = int(row[4])
            csv_array.append([row[1], row[3]*300+pow(2,row[4])])
        elif row[2] == 'Tempo' : # time and tempo
            row[3] = int(row[3])
            csv_array.append([row[1], row[3]])
        elif row[2] == 'Note_on_c' :
            row[4] = int(row[4])
            csv_array.append([row[1], row[4]])
    #print(csv_array)
    with open(csvpath+"\\\\"+file+'.csv', 'w', newline="") as out:
        for row in csv_array :
            writer = csv.writer(out)
            writer.writerow(row)
        
for s in pathdir:
    convert(s)

