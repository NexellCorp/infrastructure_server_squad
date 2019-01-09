#!/bin/bash

echo "------------------------------------"
echo " squad runserver run"
echo "------------------------------------"
screen -dmS squadRunServer
screen -r squadRunServer -X stuff 'squad --bind 0.0.0.0:5000\n'
sleep 5

echo "------------------------------------"
echo " rabbitmq-server run "
echo "------------------------------------"
screen -dmS rabbitmqServer
screen -r rabbitmqServer -X stuff 'sudo rabbitmq-server\n'
sleep 3

echo "------------------------------------"
echo " squad worker run "
echo "------------------------------------"
screen -dmS squadWorker
screen -r squadWorker -X stuff 'celery -A squad worker\n'
sleep 1

echo "------------------------------------"
echo " squad beat run "
echo "------------------------------------"
screen -dmS squadBeat
screen -r squadBeat -X stuff 'celery -A squad beat\n'
sleep 1

echo "------------------------------------"
echo " squad-admin listen run "
echo "------------------------------------"
screen -dmS squadAdmin
screen -r squadAdmin -X stuff 'squad-admin listen\n'


