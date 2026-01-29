#!/bin/bash
# Script version date 2026-01-29
export HAMAI_PROFILE=banan

source ../piper-tts/piper/bin/activate

while true; do
	DIRPATH="./pipeline/tts/${HAMAI_PROFILE}_*"

	for FILE in $DIRPATH; do
	
	  if [[ -f "$FILE" && $FILE != $0 ]]; then # Check if it's a regular file
		filename=$(basename $FILE)
		basename="${filename%.*}"
		python3 -m piper -m ru_RU-dmitri-medium -i $FILE -f pipeline/tx/$basename.wav 
		echo "[TTS] $FILE => pipeline/tx/$basename.wav"
		mv "$FILE" "processed/tts/$filename"
	  fi
	done
	
	sleep 0.1
done
