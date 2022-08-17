# Rockwell AIM-65 Enigma Machine Simulator

This is an Enigma machine simulator for the Rockwell AIM-65 computer. It builds using the CA65 assembler that comes with CC65.

This version is essentially a proof of concept. The plugboard simulation wasn't working how I'd like so I've removed it for now.

I only have a basic set of rotors implemented. More can be computed using the `compute_rotors.py` script and added to the machine by hand.

## Todo

- Better plugboard simulation
- More rotors
- A menu for configuring the rotors, plugboard, and initial state
- Pre-compiled paper tape images for easy loading over serial
- A better readme
