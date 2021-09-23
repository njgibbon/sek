FROM python:3.9-alpine
RUN apk update
RUN pip install --no-cache-dir -U boto3
RUN pip install --no-cache-dir sek==0.0.16
ENTRYPOINT ["sek"]
