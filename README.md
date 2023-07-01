# deploy_1st_app_on_k8s
Create a hello world API with Python using FastAPI, bundle it up as a container image, and then deploy it to a Kubernetes cluster on Civo Cloud

create a python env
$ python3 -m venv ./venv
activate virtual env
source ./venv/bin/activate

install packages
$ pip install fastapi uvicorn 
create requirements file
install via requirements.txt
$ pip install -r requirements.txt 

add Dockerfile one level up

build docker image
$ docker build -t k8s-fastapi .

run container
port forward from localhost 8000  to 80 inside the container
$ docker run -p 8000:80 k8s-fastapi

get the container into a registry, from where we'll be able to use it.
create new repo from https://hub.docker.com/
build the new image to be pushed
$ docker build -t kokouvishna/first_k8s:0.0.1 .
push the new image to the repo
$ docker push kokouvishna/first_k8s:0.0.1

create a cluster on civo cloud to deploy the image
create deployment, service files
download the civo kubeconfig into the root folder

$ export KUBECONFIG=/home/master/Documents/deploy_1st_app_on_k8s/civo-first_k8s-kubeconfig
$ kubectl get nodes
all nodes in civo should appear
X-X_X-node-pool-X-X   Ready    <none>   22h   v1.23.6+k3s1
...
under deploy_1st_app_on_k8s/kubernetes run
$ kubectl apply -f .

port forward from the local system to the k8s cluster
$ kubectl port-forward <pod-name> 8080:80
Forwarding from 127.0.0.1:8080 -> 80
Forwarding from [::1]:8080 -> 80
When you try again to access the page via http://127.0.0.1:8080/
You should now get: Hello "From: CIVO"

setup DNS
Get the traffic from the public internet into the cluster 