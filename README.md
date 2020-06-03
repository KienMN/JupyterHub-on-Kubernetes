# Manual deployment of JupyterHub on Kubernetes for a single machine

This repository provides source code for Deploying a simple JupyterHub on Kubernetes for a single machine.  

It contains
- Dockerfile files (`images` directory) for building Docker images
- `yaml` files (`jupyter-hub` directory) for deploying some components of JupyterHub on Kubernetes via `kubectl` commands.

This repository is for the post at https://medium.com/@kienmn97/manually-deploy-jupyterhub-on-kubernetes-for-a-single-machine-dbcd9c9e50a4

Update KubeSpawner service account in order to mount Kubernetes service account secrets to single user notebook: https://medium.com/@kienmn97/mounting-kubernetes-service-account-secrets-for-single-user-jupyter-notebook-pod-29163e527ad3

Update PersistentVolume and PersistentVolumeClaim for storage: https://medium.com/@kienmn97/persistent-storage-in-jupyterhub-on-kubernetes-cluster-running-on-minikube-4b469bdb1b86