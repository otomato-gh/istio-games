kubectl port-forward -n istio-system $(kubectl get pod -n istio-system -l app=servicegraph -o jsonpath={.items[0].metadata.name}) 8088:8088
