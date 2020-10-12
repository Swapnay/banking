#!/usr/bin/env bash

echo "Waiting for MySQL..."

#until nc -z -v -w30 $CFG_MYSQL_HOST 3306
#do
  echo "Waiting for database connection..."
  # wait for 5 seconds before check again
 # sleep 5
#done

while ! nc -z mysql_test 3306; do
  sleep 0.5
done

#while !  wget mysql:3306; do
# sleep 0.5
#done

echo "MySQL started"
pwd
echo "doing ls"
ls
cd /app
echo "doing ls"
 pwd
 ls

python -m dbinit
python -m bank
