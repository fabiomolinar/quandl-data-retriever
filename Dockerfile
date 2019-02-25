FROM python:3.6.8
LABEL maintainer="Fabio Molinar <fabiomolinar@gmail.com>"

RUN apt-get update && apt-get install -y nano build-essential libssl-dev libffi-dev python-dev

# proxy settings
ARG PROXY
ENV http_proxy=${PROXY}
ENV PIP_PROXY=${PROXY}

ENV INSTALL_PATH /opt/services/quandl-data-retriever/src
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH
COPY . .
RUN pip install --upgrade pip && \
  pip install pipenv && \
  pipenv install --system