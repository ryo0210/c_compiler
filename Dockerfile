FROM ubuntu:latest
RUN DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo
RUN apt update && apt install -y tzdata
RUN apt install -y gcc make git binutils libc6-dev gdb sudo
RUN adduser --disabled-password --gecos '' user
RUN echo 'user ALL=(root) NOPASSWD:ALL' > /etc/sudoers.d/user
USER user
WORKDIR /home/user