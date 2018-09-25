kubectl create secret generic istiotst --type=tls --from-file=tls.crt=ingress.crt --from-file=tls.key=ingress.key --namespace=kube-system
