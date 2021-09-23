FROM python:3.9-alpine
RUN apk update
RUN pip install --no-cache-dir boto3==1.18.46
RUN pip install --no-cache-dir sek==0.0.16
ENTRYPOINT ["sek"]
