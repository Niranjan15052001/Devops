FROM ubuntu


RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install flask
WORKDIR /out
COPY . /out/

ENTRYPOINT FLASK_APP=/out/app.py flask run --host=0.0.0.0 --port=3000