#!/bin/bash
# Script version date 2026-01-29
export HAMAI_PROFILE=banan
export HAMAI_LLM_NAME=gemma3

# Start ollama model if not running
if ollama ps | grep -q $HAMAI_LLM_NAME; then
	echo "Model '$HAMAI_LLM_NAME' is already running!"
else
	echo "Starting '$HAMAI_LLM_NAME' Ollama model..."
	ollama run $HAMAI_LLM_NAME &
	sleep 10
fi

python3 lib/gpt.py
