PROJECT_NAME = enigma

SHELL := /bin/bash

AFLAGS		= -t none
LFLAGS		= -t none
RMFLAGS		= -f
 
CC		= cc65
CA		= ca65
CL		= cl65
RM		= rm

all: clean $(PROJECT_NAME).bin

$(PROJECT_NAME).o: $(PROJECT_NAME).a65
	$(CA) $(AFLAGS) -o $(PROJECT_NAME).o $(PROJECT_NAME).a65
$(PROJECT_NAME).bin: $(PROJECT_NAME).o
	$(CL) $(LFLAGS) -C aim65.cfg -o $(PROJECT_NAME).bin $(PROJECT_NAME).o

clean:
	$(RM) $(RMFLAGS) *.o *.bin

papertape: all
	srec_cat enigma.bin -Binary -offset 512 -Output enigma.bin.ser -MOS_Technologies 
