# output the midi
from mido import Message, MidiFile, MidiTrack, MetaMessage
import csv
import os

filepathin = r'.\IN_mid'
pathout = r'.\OUT_mid'
pathdir=os.listdir(filepathin)

def outmidi(file):
    # build a midi file and set the header  
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    
    track.append(MetaMessage('key_signature', key='C'))
    track.append(MetaMessage('instrument_name', name="Steel Drums")) 
    track.append(MetaMessage('channel_prefix', channel = 10))
    track.append(Message('program_change', program=0, time=0))
    array = [] # all the data in csv
    with open(filepathin+"\\\\"+file, 'r') as inp:
        for row in csv.reader(inp):
            row[0] = int(row[0])
            row[1] = int(row[1])
            array.append(row)
    
    rest = [] #all the tempo
    note = [] # all the note 
   
    for ro in array :
        if ro[1] < 128 :
            note.append(ro)
            i = ro[0]+100 # tick + 100
            j = ro[1]+100 # pitch + 100 means note off
            note.append([i, j])
        else :
            rest.append(ro)
            
    for row in rest:
        note.append(row)
    seq = sorted(note,key=(lambda x:x[0])) #all the data after sort

    time0 = 0
    for row in seq:
        tim = row[0] - time0
        time0 = row[0]
        if row[1] > 128 and row[1] < 228: # note off
            track.append(Message('note_off', note=row[1]-100, velocity=64, time=tim))
        elif row[1] < 128 : #note on
            track.append(Message('note_on', note=row[1], velocity=64, time=tim))
        elif row[1] >10000 : # tempo
            track.append(MetaMessage('set_tempo', tempo = row[1], time=tim))
        else :
            down = row[1]%100
            up = int((row[1] - down)/300)
            track.append(MetaMessage('time_signature', numerator=up, denominator=down))
        
    mid.save(pathout+'\\\\'+file + '.mid')

for s in pathdir:
    outmidi(s)





