# Como 

## crear

```
docker build -t baseflask .
```

## ejecutar

```
docker run --rm -it -p 5001:5000 -v $(pwd):/workdir -d baseflask
```
