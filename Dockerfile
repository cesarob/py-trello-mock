FROM python:3.6

RUN apt-get update

ARG uid=1000
ARG gid=1000
RUN addgroup -gid $gid trellomock
RUN useradd -m --uid $uid -g trellomock trellomock

# Install common dependencies
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
WORKDIR /app
ENV PYTHONPATH=/app
