#!bin/bash
docker rm -f $(docker ps -a -q)
#docker image rm -f $(docker images -q)

docker run -p 5433:5432 -d \
    --network=postgres16_network \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_DB=db \
    --name postgres16_container \
    -v pgdata:/var/lib/postgresql/data \
    postgres:16-bullseye

docker network inspect postgres16_network -f '{{range .Containers}}{{.Name}} {{.IPv4Address}}{{end}}'

docker build -t dvf .
docker run -p 8008:8000 -d \
    --network=postgres16_network \
    --name dvf_container \
    dvf