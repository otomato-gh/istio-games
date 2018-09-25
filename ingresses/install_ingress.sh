#! /bin/bash -f
helm install stable/nginx-ingress --name=myingress --set rbac.create=true
