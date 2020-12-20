# nature-exporter

this Prometheus exporter get data from Nature Remo Cloud API

### setup

set token

```
cat << EOS > .env
TOKEN=[token here]
EOS
```

## docker-compose

```
docker-compose up -d
```

## kubernetes

```
kubectl create secret generic nature --from-file .env
kubectl apply -f deploy deployment.yaml
```
