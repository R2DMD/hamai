#!/bin/bash
# Script version date 2026-01-29
# To install dependecies run: sudo apt install sox libsox-fmt-all

export HAMAI_PROFILE=banan

export AUDIODRIVER=alsa
export AUDIODEV=hw:0,0

#if [ "$#" -lt 1 ]; then
#	echo "Usage: $0 <audio_interface>"
#   echo "Example: $0 0,2"
#   echo "[Hint] To see available capture devices run: arecord -l" 
#	exit 1
#fi

# Set ID here. Recommended format: QTH_FREQ. This ID is included in the filename for all generated files
#readonly Rxid="${HAMAI_PROFILE}"

# HW device
#readonly DEVICE="$1"
#readonly HW="hw${DEVICE//,}"

# Startup messages
#echo "[$Rxid] Listening audio interface $DEVICE"

# Main loop
while true; do
	timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
	filename="${HAMAI_PROFILE}_${timestamp}.wav"
	#filename="${Rxid}_${HW}_${timestamp}.wav"
	#rec -t alsa hw:$1 -c 1 pipeline/rx/$filename silence 1 0.1 3% 1 0.5 3%
	rec -c 1 pipeline/rx/$filename silence 1 0.1 3% 1 0.5 3%
	mv pipeline/rx/$filename pipeline/stt/$filename	
	echo "[RX] File added to pipeline: $filename"
done
