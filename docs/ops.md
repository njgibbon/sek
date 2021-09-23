# Operations


# Versioning
* `setup.py`
* `main.py`
* `Dockerfile`


# Build
```
# Top level dir
# Delete dist/
rm -rf dist
python3 setup.py sdist
twine upload dist/*
```


# Dev
```
python3 -m sek.main --cloud=aws --resource=eks --name=test
```


# Test
```
python3 -m unittest discover tests 
```


# Docker
```
docker build -t sek .
docker run -it --rm sek
docker tag sek nickjgibbon/sek
docker tag sek nickjgibbon/sek:0.0.16
docker image push nickjgibbon/sek
docker image push nickjgibbon/sek:0.0.16
docker run -it --rm nickjgibbon/sek
```
