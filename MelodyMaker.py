# GENERATE A RANDOM 6-NOTE MELODY WITHIN THE KEY OF C SHARP MINOR
# By Laughton Chandler, 2019-2021

import os
import random
from midiutil import MIDIFile
from datetime import datetime

#csharpm
keyCsm = [13, 15, 16, 18, 20, 21, 23, 25, 27, 28, 30, 32, 33, 35, 37, 39, 40, 42, 44, 45, 47, 49, 51, 52, 54, 56, 57, 59, 61, 63, 64, 66, 68, 69, 71, 73, 75, 76, 78, 80, 81, 83, 85, 87, 88, 90, 92, 93, 95, 97, 99, 100, 102, 104, 105, 107]


# GET FIRST NOTE OF MELODY
Note1 = keyCsm[28] # Tonic Key normally
Note1Literal = 28
print(Note1)

# GET SECOND NOTE OF MELODY
rnd1 = random.randint(1, 5) # number of notes within key to jump
UporDown = random.sample([1, -1],  1) # direction of jump - third number indicates how many numbers to output
UporDownInt = int(UporDown[0]) #Turn UporDown into an Integer:
Pre2 = int(rnd1) * int(UporDownInt)
Note2Literal = Note1Literal + Pre2
Note2 = keyCsm[Note2Literal] # Takes the number in the sequence of the original key and adds or subtracts on a positional basis, then returns that value
print(Note2)

# GET THIRD NOTE OF MELODY
rnd1 = random.randint(1, 5) # number of notes within key to jump
UporDown = random.sample([1, -1],  1) # direction of jump - third number indicates how many numbers to output
UporDownInt = int(UporDown[0]) #Turn UporDown into an Integer:
Pre3 = int(rnd1) * int(UporDownInt)
Note3Literal = Note2Literal + Pre3
Note3 = keyCsm[Note3Literal] # Takes the number in the sequence of the original key and adds or subtracts on a positional basis, then returns that value
print(Note3)

# GET FOURTH NOTE OF MELODY
rnd1 = random.randint(1, 5) # number of notes within key to jump
UporDown = random.sample([1, -1],  1) # direction of jump - third number indicates how many numbers to output
UporDownInt = int(UporDown[0]) #Turn UporDown into an Integer:
Pre4 = int(rnd1) * int(UporDownInt)
Note4Literal = Note3Literal + Pre4
Note4 = keyCsm[Note4Literal] # Takes the number in the sequence of the original key and adds or subtracts on a positional basis, then returns that value
print(Note4)

# GET FIFTH NOTE OF MELODY
rnd1 = random.randint(1, 5) # number of notes within key to jump
UporDown = random.sample([1, -1],  1) # direction of jump - third number indicates how many numbers to output
UporDownInt = int(UporDown[0]) #Turn UporDown into an Integer:
Pre5 = int(rnd1) * int(UporDownInt)
Note5Literal = Note4Literal + Pre5
Note5 = keyCsm[Note5Literal] # Takes the number in the sequence of the original key and adds or subtracts on a positional basis, then returns that value
print(Note5)

# GET SIXTH NOTE OF MELODY
rnd1 = random.randint(1, 5) # number of notes within key to jump
UporDown = random.sample([1, -1],  1) # direction of jump - third number indicates how many numbers to output
UporDownInt = int(UporDown[0]) #Turn UporDown into an Integer:
Pre6 = int(rnd1) * int(UporDownInt)
Note6Literal = Note5Literal + Pre6
Note6 = keyCsm[Note6Literal] # Takes the number in the sequence of the original key and adds or subtracts on a positional basis, then returns that value
print(Note6)


# CREATE VOLUMES OF NOTES
Volume1 = random.randint(55, 90)
Volume2 = random.randint(55, 90)
Volume3 = random.randint(55, 90)
Volume4 = random.randint(55, 90)
Volume5 = random.randint(55, 90)
Volume6 = random.randint(55, 90)

# CREATE DURATIONS OF NOTES
Duration1 = random.randint(1, 3)
Duration2 = random.randint(1, 3)
Duration3 = random.randint(1, 3)
Duration4 = random.randint(1, 3)
Duration5 = random.randint(1, 3)
Duration6 = random.randint(1, 3)

# DESIGNATE START TIMES OF NOTES
Time1 = 1
Time2 = Time1 + random.randint(1, 2)
Time3 = Time2 + random.randint(1, 3)
Time4 = Time3 + random.randint(1, 3)
Time5 = Time4 + random.randint(1, 3)
Time6 = Time5 + random.randint(1, 2)


# CREATES A MIDI FILE
# Defines midi file
MyMIDI = MIDIFile(1)


#ADDS NOTE 1
track    = 0   # Track numbers are zero-origined
channel  = 0   # MIDI channel number
pitch    = Note1  # MIDI note number
time     = Time1   # In beats - the time-marker in the file - same time for chord
duration = Duration1   # In beats
volume   = Volume1 # 0-127, 127 being full volume
annotation = None
MyMIDI.addNote(track,channel,pitch,time,duration,volume,annotation)

#ADDS NOTE 2
track    = 0   # Track numbers are zero-origined
channel  = 0   # MIDI channel number
pitch    = Note2  # MIDI note number
time     = Time2   # In beats - the time-marker in the file - same time for chord
duration = Duration2   # In beats
volume   = Volume2 # 0-127, 127 being full volume
annotation = None
MyMIDI.addNote(track,channel,pitch,time,duration,volume,annotation)

#ADDS NOTE 3
track    = 0   # Track numbers are zero-origined
channel  = 0   # MIDI channel number
pitch    = Note3  # MIDI note number
time     = Time3   # In beats - the time-marker in the file - same time for chord
duration = Duration3 # In beats
volume   = Volume3 # 0-127, 127 being full volume
annotation = None
MyMIDI.addNote(track,channel,pitch,time,duration,volume,annotation)

#ADDS NOTE 4
track    = 0   # Track numbers are zero-origined
channel  = 0   # MIDI channel number
pitch    = Note4  # MIDI note number
time     = Time4  # In beats - the time-marker in the file - same time for chord
duration = Duration4   # In beats
volume   = Volume4 # 0-127, 127 being full volume
annotation = None
MyMIDI.addNote(track,channel,pitch,time,duration,volume,annotation)

#ADDS NOTE 5
track    = 0   # Track numbers are zero-origined
channel  = 0   # MIDI channel number
pitch    = Note5  # MIDI note number
time     = Time5  # In beats - the time-marker in the file - same time for chord
duration = Duration5   # In beats
volume   = Volume4 # 0-127, 127 being full volume
annotation = None
MyMIDI.addNote(track,channel,pitch,time,duration,volume,annotation)

#ADDS NOTE 6
track    = 0   # Track numbers are zero-origined
channel  = 0   # MIDI channel number
pitch    = Note6  # MIDI note number
time     = Time6 # In beats - the time-marker in the file - same time for chord
duration = Duration6   # In beats
volume   = Volume6 # 0-127, 127 being full volume
annotation = None
MyMIDI.addNote(track,channel,pitch,time,duration,volume,annotation)


filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")
filename2 = filename1 + '.mid'
with open(filename2, 'wb') as output_file:
    MyMIDI.writeFile(output_file)

print("Midi file saved to disk!")
#os.startfile("filename2")


