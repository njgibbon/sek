# Build
```
# Top level dir
# Delete dist/
python3 setup.py sdist
twine upload dist/*
```


# Dev Run
Command to run when dev due to python and relative references.
```
python3 -m sek.main --cloud=aws --resource=eks --name=test
```
