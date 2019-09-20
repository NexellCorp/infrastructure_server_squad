FROM debian:stretch
RUN apt-get update && \
  apt-get install -qy auto-apt-proxy && \
  apt-get install -qy python3 \
    python3-pip \
    libpq-dev \
    libyaml-dev \
    wget \
    unzip \
    rabbitmq-server

COPY requirements.txt /srv/
RUN pip3 install --no-binary :all: -r /srv/requirements.txt

RUN pip3 install squad

RUN apt-get update && apt-get install -y sudo vim screen ssh

ARG user=nexellSquad
ARG group=nexellSquad
ARG uid=1001
ARG gid=1001

ENV SQUAD_STAIC_DIR /app/static

RUN groupadd -g ${gid} ${group} && useradd -d "/home/${user}" -u ${uid} -g ${gid} -m -s /bin/bash ${user}
RUN echo "${user}:${user}" | chpasswd
RUN echo "${user} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

USER nexellSquad

COPY db.sqlite3 /usr/local/lib/python3.5/dist-packages/
