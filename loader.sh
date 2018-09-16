#! /bin/bash -x
URL=$1
while true
  do printf '%s\n' {1..10} | xargs -I % -P 10 curl ${URL};
  sleep 5 
done
