#! /bin/bash -f
kubectl apply -f aleph-dep.yml  -f front-dep.yml -f beth-dep.yml -f aleph-dep1.yml -n games
