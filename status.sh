#!/bin/bash

p="python3"
pid="$(ps -fe | grep python3 | grep bot.py | awk '{print$9}')"

echo $pid
if [[ "$pid" ==  "main.py" ]]; then
echo "process running"
else
echo "process not running"
cd ~
cd /path/to/bot
python3 main.py

fi

