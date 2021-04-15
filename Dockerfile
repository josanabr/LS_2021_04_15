FROM ubuntu
RUN apt-get -y update && apt-get -y install python3 python3-pip
RUN pip3 install flask
EXPOSE 5000
ENV FLASK_APP=/workdir/holamundo.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask","run"]
