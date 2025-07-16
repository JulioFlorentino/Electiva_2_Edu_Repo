FROM ubuntu:24.04

RUN apt update && apt install -y openssh-server python3 sudo nginx curl

RUN useradd -ms /bin/bash ansible && echo 'ansible:ansible' | chpasswd && adduser ansible sudo

RUN mkdir /var/run/sshd

# Expón puertos SSH y HTTP
EXPOSE 22 80

# Comando para iniciar ambos servicios
CMD service nginx start && /usr/sbin/sshd -D
