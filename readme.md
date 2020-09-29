# Apache Spark cluster example

## Pull base image
```
docker pull bitnami/spark:latest
```

## Run master node standalone

```
docker run --rm -d --name spark-master \
  -p 8080:8080 \
  -p 7077:7077 \
  -e SPARK_MODE=master \
  bitnami/spark
```

## Run worker node standalone

```
docker run --rm -d --name spark-worker \
  -e SPARK_MODE=worker \
  bitnami/spark
```
NOTE:
SPARK_MASTER_URL=spark://spark-master:7077

## Or run both using docker-compose
```
cd cluster
docker-compose up -d
```

## Client
This client should connect with cluster execute simple query reading from small JSON.  
Build docker image
```
cd client
docker build . --tag spark-client
```

Client must run on same network of cluster.

```
docker run --rm --network=$network -it spark-client:latest /bin/bash
```

Then run standalone script, in future this will be done better :)
```
python standalone.py
```

