# GPT4ALL and ollama Voice-Assistant

This is an active repo making code to run multiple different LLMs in Embedded Devices such as Raspberry pi, Jetson. Currently testing Faster Whisper to optimize and speed up the model. Also trying to add some kind of check, so that the code doesnt keep recording. 

## Setup

MacOS install portaudio 
Install rquirements.txt using PIP

## To Do

* Faster Whisper (works in python 3.10, not on 3.12, Error during pip install AV* which is a prerequisite) 
* Use int8 instead of float32 for performance 
* Docker Support 
* Multiple model calling with different names

Function to remake: 
1. Voice to Text 
2. Text to Speech (using whisper base model)
3. Listen for key word call (using whisper tiny model)
4. Pass Text ollama 
5. Pass text GPT4All 
6. Print ollama and GPT4All texts 

**Test on Raspberry pi**
**Test on Jetson Nano** 

