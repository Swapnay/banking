#!/usr/bin/env bash

echo "Waiting for MySQL..."
echo "Waiting for database connection..."
  # wait for 5 seconds before check again
 # sleep 5
while ! nc -z mysql_test 3306; do
  sleep 0.5
done
echo "MySQL started"
cd /app

python -m dbinit
tail -f /dev/null

