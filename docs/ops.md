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
