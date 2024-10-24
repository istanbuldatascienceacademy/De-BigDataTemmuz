# Docker Network
- Docker network container'lar arasında iletişim kurmak için kullanılır.
- Docker network oluşturmak için:
```bash
docker network create mynetwork
```

- Docker network'ları listelemek için:
```bash
docker network ls
```

### Host Network
- Containerların host(kendi bilgisayarınız yada clouddaki vm makine)'un network'ünü kullanmasını sağlar.


### Bridge Network
- Container'lar arasında iletişim kurmak için kullanılır.
- Default olarak bridge network kullanılır.

- Docker network inspect etmek için:
```bash
docker network inspect mynetwork
```

- Docker network silmek için:
```bash
docker network rm mynetwork
```

- Docker network kullanarak container oluşturmak için:
```bash
docker run -d --name mycontainer --network mynetwork nginx
```

- Docker network kullanarak container connect etme için:
```bash
docker run -d --name mycontainer1 nginx
docker network connect mynetwork mycontainer1
```

- Ping ile container'lar arasında iletişim kurmak için:
```bash
docker exec -it mycontainer1 bash
apt-get update
apt-get install iputils-ping -y
ping mycontainer2
```

- mycontainer2 yi network'e connect etmek için:
```bash
docker network connect mynetwork mycontainer2
```

