FROM python:3.6.8-alpine3.9
LABEL maintainer="Fabio Molinar <fabiomolinar@gmail.com>"

RUN apk update && apk add nano

# proxy settings
ARG PROXY
ENV http_proxy=${PROXY}
ENV PIP_PROXY=${PROXY}

ENV INSTALL_PATH /opt/services/quandl-data-retriever/src
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH