#!/bin/bash
# Script version date 2026-01-29

# ./pipeline - Main working dir

# Creating dir for processing pipeline
if [[ ! -d "./pipeline" ]]; then
  mkdir ./pipeline
fi

# Creating dir for recording audio
if [[ ! -d "./pipeline/rx" ]]; then
  mkdir ./pipeline/rx
fi

# Creating inbox dir for transcribing audio recordings
if [[ ! -d "./pipeline/stt" ]]; then
  mkdir ./pipeline/stt
fi

# Creating inbox dir for text propmts
if [[ ! -d "./pipeline/gpt" ]]; then
  mkdir ./pipeline/gpt
fi

# Creating inbox dir for generating audio
if [[ ! -d "./pipeline/tts" ]]; then
  mkdir ./pipeline/tts
fi

# Creating inbox dir for transmiting audio
if [[ ! -d "./pipeline/tx" ]]; then
  mkdir ./pipeline/tx
fi

# ./processed - Archive of files that passed through the pipeline

# Creating dir for storing processed files
if [[ ! -d "./processed" ]]; then
  mkdir ./processed
fi

# Creating dir for processed recording audio
if [[ ! -d "./processed/rx" ]]; then
  mkdir ./processed/rx
fi

# Creating inbox dir for transcribed audio recordings
if [[ ! -d "./processed/stt" ]]; then
  mkdir ./processed/stt
fi

# Creating inbox dir for processsed text propmts
if [[ ! -d "./processed/gpt" ]]; then
  mkdir ./processed/gpt
fi

# Creating inbox dir for generated audio
if [[ ! -d "./processed/tts" ]]; then
  mkdir ./processed/tts
fi

# Creating inbox dir for transmitted audio
if [[ ! -d "./processed/tx" ]]; then
  mkdir ./processed/tx
fi

# ./profiles - Dir for storing profiles

# Creating inbox dir for profiles
if [[ ! -d "./profiles" ]]; then
  mkdir ./profiles
fi


