#!/bin/bash
# Script version date 2026-01-29
# To install dependecies run: sudo apt install sox libsox-fmt-all

export HAMAI_PROFILE=banan

export AUDIODRIVER=alsa
export AUDIODEV=hw:0,0

stty -F /dev/ttyUSB0 -hupcl

while true; do
	DIRPATH="./pipeline/tx/${HAMAI_PROFILE}_*"

	for FILE in $DIRPATH; do
	
	  if [[ -f "$FILE" && $FILE != $0 ]]; then # Check if it's a regular file
		echo "[TX] File found: $FILE. Processing..."
		
		echo ptt_on > /dev/ttyUSB0
		sleep 1
		
		play "$FILE" &&
		#play -t alsa hw:$1 "$FILE" 
		#sox "$FILE" -t alsa 0 &&
		
		echo ptt_off > /dev/ttyUSB0
		
		mv "$FILE" "processed/tx/"
		echo "[TX] File $FILE completed the pipeline"
	  fi
	  
	done
	
	sleep 0.1
done
