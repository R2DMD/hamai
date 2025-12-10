#!/bin/bash
# To install dependecies run: sudo apt install sox libsox-fmt-all

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <audio_interface>"
    echo "Example: $0 0,2"
    echo "[Hint] To see available capture devices run: arecord -l" 
	exit 1
fi

stty -F /dev/ttyUSB0 -hupcl

while true; do
	
	for FILE in ./pipeline/tx/*; do
	
	  if [[ -f "$FILE" && $FILE != $0 ]]; then # Check if it's a regular file
		echo "[TX] File found: $FILE. Processing..."
		
		echo ptt_on > /dev/ttyUSB0
		sleep 0.5
		 
		play -t alsa hw:$1 "$FILE" 
		#sox "$FILE" -t alsa 0 &&
		
		echo ptt_off > /dev/ttyUSB0
		
		mv "$FILE" "processed/tx/"
		echo "[TX] File $FILE completed the pipeline"
	  fi
	  
	done
	
	sleep 0.5
done
