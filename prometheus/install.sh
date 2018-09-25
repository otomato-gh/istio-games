#! /bin/bash -f

if [ "$#" -ne 1 ]; then
  echo "Usage: install.sh my_istio_gw_ip"
  exit 1
fi

helm install . --name prom-games --namespace games --set gateway_ip=$1