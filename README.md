# Kubernetes Training

To build Docker image from Dockerfile:

`docker build -t flask-app . `

To run container from image

`docker run -it --name flask-app-container flask-app`

To run local image inside a Pod (must be run every shell session):

`eval $(minikube -p minikube docker-env)`

Run a shell inside a Pod:

`kubectl exec --stdin --tty k8-training-pod-alpine-app -- /bin/bash`
