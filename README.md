# Kubernetes Training

To build Docker image from Dockerfile:

`docker build -t flask-app . `

To run container from image

`docker run -it --name flask-app-container flask-app`

To run local image inside a Pod (must be run every shell session):

`eval $(minikube -p minikube docker-env)`

Run a shell inside a Pod:

`kubectl exec --stdin --tty k8-training-pod-alpine-app -- /bin/bash`
`kubectl exec k8-training-pod -c flask-app-pod -ti -- bash`

Access Pod via Service NodePort

'''
Exposes the Service on each Node's IP at a static port (the NodePort). A ClusterIP Service, to which the NodePort Service routes, is automatically created. You'll be able to contact the NodePort Service, from outside the cluster, by requesting <NodeIP>:<NodePort>.
'''

`minikube ip` 
`kubectl describe svc`

Utilizar IP minikube + NodePort
