#! /bin/bash -f
URL=$@
while true
do 
  printf '%s\n' {1..10} | xargs -I % -P 10 curl -w "\n" ${URL};
  echo "..."
  sleep 1
done
