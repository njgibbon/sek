# Build
```
# Top level dir
Delete dist/
python3 setup.py sdist
twine upload dist/*
```

```
python3 -m sek.main --cloud=aws --resource=eks --name=test
```
