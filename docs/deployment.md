# Deployment

## Docker
```bash
docker-compose up -d
```

## Kubernetes
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: watchdogx
spec:
  replicas: 1
```
