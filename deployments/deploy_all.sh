#! /bin/bash -f
kubectl create ns games
kubectl label ns games istio-injection=enabled
kubectl apply -f aleph-dep.yml  -f front-dep.yml -f beth-dep.yml -f loader-dep.yml -n games
