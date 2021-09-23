FROM python:3.9-alpine
COPY requirements.txt requirements.txt
RUN apk update
RUN pip install -r requirements.txt
RUN pip install sek==0.0.16
ENTRYPOINT ["sek"]
