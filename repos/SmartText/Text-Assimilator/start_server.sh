#!/bin/bash

if [ -z $LOG_FILE ]; then
    LOG_FILE=tika_server.log
fi
nohup java -jar tika-server-1.12.jar > $LOG_FILE 2>&1 &
cd assimilator && python manage.py runserver 0.0.0.0:8080
