FROM python:3-alpine3.15
WORKDIR /out
COPY . /out
RUN pip3 install flask
EXPOSE 3000
CMD python ./app.py