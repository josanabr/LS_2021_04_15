FROM ubuntu
RUN apt-get -y update && apt-get -y install python3 python3-pip
RUN pip3 install flask
EXPOSE 5000
