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
