kubectl create secret generic istioto --type=tls --from-file=tls.crt=ingress.crt --from-file=tls.key=ingress.key --namespace=kube-system
