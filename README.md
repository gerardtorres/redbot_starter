# About
Custom Python script used for launching redbot from scheduled task. Also updates custom command with ip from server(settings.json).

## Features
- Checks windows for redbot process before starting bot
- Updates json dictionary object with IP of local server
- After updated the bot, performs a graceful shutdown, then starts bot from the virtual python env
- Intended to be launched via included bat file via scheduled task

## Caution
Very limited testing with the first commits. I will solve issues as I go. 
