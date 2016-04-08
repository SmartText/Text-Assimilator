#!/bin/bash

if [ -z $LOG_FILE ]; then
    LOG_FILE=tika_server.log
fi
nohup java -jar tika-server-1.12.jar > $LOG_FILE 2>&1 &
