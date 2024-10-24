- Bir image'ı indirmek için docker pull komutunu kullanırız. Örneğin:
```bash
docker pull hello-world
```

- İndirilen image'ları listelemek için docker images komutunu kullanırız. Örneğin:
```bash
docker images
```


- Bir container oluşturmak için docker run komutunu kullanırız. Bu komutu kullanırken container ismi ve hangi image'dan oluşturulacağını belirtmemiz gerekmektedir. Ayrıca container'ın hangi porttan dışarıya açılacağını belirtmemiz gerekmektedir. Örneğin:
```bash
docker run hello-world
```

- Çalışan container'ları listelemek için docker ps komutunu kullanırız. Örneğin:
```bash
docker ps
```

- Çalışan ve çalışmayan container'ları listelemek için docker ps -a komutunu kullanırız. Örneğin:
```bash
docker ps -a
```
> Container ID -> Container'ın ID'si (Benzersizdir)

> Image -> Container'ın oluşturulduğu image'ın adı

> Command -> Container'ın çalıştırıldığı komut

> Created -> Container'ın ne zaman oluşturulduğu

> Status -> Container'ın durumu

> Ports -> Container'ın hangi porttan dışarıya açıldığı

> Names -> Container'ın ismi (Benzersizdir) (Container'ı oluştururken isim verilmezse rastgele bir isim verilir)



- Arayüzü olan bir container çalıştır
```bash
docker run -p 8080:80 nginx
```

- Container'ı durdurmak için docker stop komutunu kullanırız. Örneğin:
```bash
docker stop container_id/container_name
```

- Container'ı silmek için docker rm komutunu kullanırız. Örneğin:
```bash
docker rm container_id/container_name
```

- Container'ı durdurup silmek için docker rm -f komutunu kullanırız. Örneğin:
```bash
docker rm -f container_id/container_name
```


- Duran bir container'ı çalıştırmak için docker start komutunu kullanırız. Örneğin:
```bash
docker start container_id/container_name
```

- Containera isim vererek çalıştırmak
```bash
docker run --name mynginx -p 8080:80 nginx
```

- Containerı arkaplanda çalıştırmak
```bash
docker run -d --name mynginx -p 8080:80 nginx
```

- Container'ın loglarını görmek için docker logs komutunu kullanırız. Örneğin:
```bash
docker logs mynginx -> container ismi
```

- Containerlara port eklemek
```bash
docker run -d --name mynginx -p 8080:80 -p 4443:443 nginx
```

- Docker İmagelarını silmek için
```bash
docker rmi image_id
```

- Dockerhub'a login olmak
```bash
docker login
- Kullanıcı adı ve şifre girilir
```
