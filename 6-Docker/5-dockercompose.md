# Docker Compose
- Docker Compose birden fazla container'ı tek bir dosya üzerinden yönetmemizi sağlar.
- Bu yönetim işlemleri için YAML dosyası kullanılır.
- Docker Compose ile birden fazla container'ı aynı anda başlatıp durdurabiliriz.
- Volume ve Network oluşturmak için Docker Compose kullanılır.

### Docker Compose Dosyası Oluşturmak
- Docker Compose dosyası oluşturmak için `docker-compose.yml` adında bir dosya oluşturulur.
- Eğer farklı bir isimde dosya oluşturulmak istenirse, `docker-compose -f dosya_adı.yml` şeklinde dosya adı belirtilir.

### Docker Compose Dosyası Örnek
```yaml
# docker run --name deneme -p 8080:80 -v volume:/app --network mynetwork nginx
version: '3' # Docker Compose version
services: # Container'lar
  web: # Container adı
    image: nginx # Container'ın kullanacağı image
    container_name: deneme # Container'ın adı
    ports: # Container'ın hangi portları kullanacağı
      - "8080:80" # 8080 portunu 80 portuna yönlendir
      - "8081:80" # 8081 portunu 80 portuna yönlendir
      - "8082:80" # 8082 portunu 80 portuna yönlendir
    volumes: # Container'ın hangi volume'ları kullanacağı
        - ./deneme_volume:/app # volume adı /app klasörüne bağlanacak
    networks: # Container'ın hangi network'leri kullanacağı
        - mynetwork1 # mynetwork network'ünü kullan
networks: # Network'ler
    mynetwork1: # Network adı
        driver: bridge # Network driver'ı
volumes: # Volume'ler
    deneme_volume: # Volume adı
```

Spark
```yaml
version: "3"
services:
  # jupyterlab with pyspark
  pyspark:
    image: jupyter/pyspark-notebook
    container_name: pyspark
    environment:
      JUPYTER_ENABLE_LAB: "yes"
    command: ["start-notebook.sh", "--NotebookApp.token='123'", "--NotebookApp.password=''"]
    ports:
      - "8888:8888"
    volumes:
      - ./work:/home/jovyan
```

### Docker Compose Komutları
- Docker Compose dosyası oluşturmak için:
```bash
docker-compose up -d 
```
- Docker Compose dosyasını silmek için:
```bash
docker-compose down
```