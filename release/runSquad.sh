#!/bin/bash

echo "------------------------------------"
echo " squad runserver "
echo "------------------------------------"
squad --bind 0.0.0.0:5000 &> /dev/null &

echo "------------------------------------"
echo " rabbitmq-server run "
echo "------------------------------------"
sudo rabbitmq-server &> /dev/null &

echo "------------------------------------"
echo " squad worker run "
echo "------------------------------------"
celery -A squad worker &> /dev/null &

echo "------------------------------------"
echo " squad beat run "
echo "------------------------------------"
celery -A squad beat &> /dev/null &

echo "------------------------------------"
echo " squad-admin listen run "
echo "------------------------------------"
squad-admin listen &> /dev/null &

