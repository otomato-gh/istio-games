#! /bin/bash -f
kubectl apply -f aleph-dep.yml  -f front-dep.yml -f beth-dep.yml -n games
