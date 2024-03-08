#  Principles of information security 
## Damn Vulnerable Flask App 

### Download docker
```bash
newgrp docker
sudo usermod -aG docker $USER
curl https://get.docker.com | bash
```

### Set up DVWA
```bash
docker pull vulnerables/web-dvwa
docker run -d -p 80:80 vulnerables/web-dvwa
```

### Set up DVF
You can skip postgresql container creation if you have it already installed just specify it in `.env`
```bash
docker pull postgres:16-bullseye
docker network create postgres16_network
docker run -p 5433:5432 -d \
    --network=postgres16_network \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_DB=db \
    --name postgres16_container \
    -v pgdata:/var/lib/postgresql/data \
    postgres:16-bullseye

docker build -t dvf .
docker run -p 8008:8000 -d \
    --network=postgres16_network \
    --name dvf_container \
    dvf
```

### You might have to adjust .env file according to
docker network inspect postgres16_network -f '{{range .Containers}}{{.Name}} {{.IPv4Address}}{{end}}'

### Exploitation Techniques 
* [SQLi](./exploitation/querie.md)
* [SQLMap + Extras](./exploitation/sqlmap.md)

### [Screenshots](./exploitation/screenshots.md)
<center>
    <img src="./screenshots/0.png">
</center>