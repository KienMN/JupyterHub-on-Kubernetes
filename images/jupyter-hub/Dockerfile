FROM registry.sensetime.com/xlab/jupyterhub:v0.1.2

ARG NB_USER=jovyan

ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

WORKDIR /srv/jupyterhub

# So we can actually write a db file here
RUN chown ${NB_USER}:${NB_USER} /srv/jupyterhub

# JupyterHub API port
EXPOSE 8081

USER ${NB_USER}
#CMD ["jupyterhub"]
CMD ["jupyterhub", "--config", "/srv/jupyterhub/jupyterhub_config.py"]