FROM ubuntu:20.04

RUN apt-get update 
RUN apt-get install -y python3 iputils-ping 

WORKDIR /src
COPY mtu.py ./

ENTRYPOINT ["python3", "mtu.py"]
