#!/bin/bash

# Start seleniumserver in the background and take its PID:
/opt/bin/entry_point.sh & SELENIUM_PID=$!

# Function for checking forever if /tmp/shared/exited file exists
check_for_exit () {
  while true; do 
    if [[ -f "/tmp/shared/exited" ]]; then 
       kill $SELENIUM_PID; 
    fi

    sleep 1;
  done
}

check_for_exit &

wait $SELENIUM_PID
exit 0
