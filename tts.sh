#!/bin/bash
source ../piper-tts/piper/bin/activate

while true; do
	
	for FILE in ./pipeline/tts/*; do
	
	  if [[ -f "$FILE" && $FILE != $0 ]]; then # Check if it's a regular file
		echo "[TTS] File found: $FILE. Processing..."
		filename=$(basename $FILE)
		basename="${filename%.*}"
		python3 -m piper -m ru_RU-dmitri-medium -i $FILE -f pipeline/tx/$basename.wav 
		echo "[TTS] File added: pipeline/tx/$basename.wav"
		mv "$FILE" "processed/tts/$filename"
	  fi
	done
	
	sleep 0.5
done
