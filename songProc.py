from mido import MidiFile

mid = MidiFile("AtDoomsGateCut.mid")
last = mid.tracks[1][0]
for msg in mid.tracks[1][1:]:
    if last.type == msg.type:
        print(last)
        print(msg)
        print()
    last = msg