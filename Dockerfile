FROM python:3.7.7-alpine3.11

# install pytorch from sorce for lowrank_svd
RUN pip install -U pip
RUN pip install nose

WORKDIR /workspace
RUN chmod -R a+w .
