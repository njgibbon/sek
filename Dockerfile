FROM python:3.7-alpine
RUN apk update
RUN pip install --no-cache-dir -U boto3
RUN pip install --no-cache-dir -U sek
ENTRYPOINT ["sek"]
