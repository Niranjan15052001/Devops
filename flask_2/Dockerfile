FROM python:3-alpine3.15
WORKDIR /out
COPY . /out/
RUN pip install flask

EXPOSE 8080
CMD python ./app.py