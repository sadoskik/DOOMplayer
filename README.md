# DOOMplayer

## Overview
The board uses a set of two 555 timers to generate notes and keep time. A state machine determines the currently playing notes.

## 

## Note Generation
The number of note generating 555 timers is determined by how many "channels" are needed. This refers to the max number of concurrent notes needed during the song. To achieve multiple notes on a single 555 timer, the resistance R_b in Graphic 1 will be changed to different preset values. Graphic 2 shows how specific resistance values can be achieved by closing switches for human keyboards or driving a transistor for automated note generation. The current version only uses a single note generating 555 timer, though future iterations will likely need at least one more to perform the treble clef notes. 
##

## State Machine
The state machine will only capture the initial riff which is repeated four times in the original song anyways. 
##

## Tempo
What's a song without a beat? One of the 555 timers is dedicated to clocking every 32nd of a beat. This is due to the fact that there are no shorter lengths than 1/32th notes in this song. Assuming a tempo of 115 beats per minute, the desired master clock is given by 
1 / [(115 / 60 ) / 32] = 16.69Hz
1 / [(bpm / sec|min) / 32]

This will be its own 555 timer as it will need to be a constant frequency.
##

## Current State
I got caught up in prototyping it rather than modeling it which I don't know too much about. Here I'll do my best to explain what I currently have / the mentality behind it. The noteGenerator schematic contains the actual up-to-date model. It contains two 555 timers like the initial plan outlined, but the resistor values for the tempo are not defined to provide the 16.69Hz desired about. The 555 timer to the left contains enough (more but that was future proofing) notes to play the main meolody. I realized as I was going about creating the state machine that it would quickly become complicated and require compute assistance. I could probably create a very inefficient state machine with a unique state for each 1/32 beat, but that felt wrong and would require a lot of logical ICs that would likely break the bank. There are annotations by the appropriate transistors for the desired note provided the transistor is closed. I found I did not need any amplification because my 9V battery source created a loud enough sound on my prototype, so I do not think I would need to bias it toward the 4.5V centerline. I did not make a BOM, but given I don't even use a microcontroller I believe I could keep it under the $50 limit. I cut the original midi file for the song with Aria. I just cut the channels down to the main melody and removed as many double notes as I could (this would require another note generating 555 timer and signal addition). Looking forward, I would probably include a microcontroller at least for the control of the note generators. I'm sure there is a more elegant way of doing it with the DAC, but I enjoyed using the analog components with the 555 IC to create a similar effect. Maybe there is a happy middle ground using some form of memory but I am unfamiliar with those. Also, this song really shines at the higher note freestyles, so a future iteration of this would definitely work towards that.
