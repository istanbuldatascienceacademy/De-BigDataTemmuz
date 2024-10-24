# Dockerfile
- Dockerfile bizim docker imaglerı oluşturmak için kullandığımız dosyadır. Dockerfile içerisinde image'ımızın nasıl oluşturulacağını belirtiriz. Dockerfile içerisindeki komutlar sırasıyla çalıştırılır ve image oluşturulur.


# Dockerfile içerisinde kullanılan komutlar

## FROM
- Dockerfile içerisinde image'ımızın hangi image'dan oluşturulacağını belirtiriz yani base image'ımızı belirtiriz.Örneğin:
```bash
FROM ubuntu:latest
```

## RUN
- Dockerfile içerisinde image'ımızın oluşturulması sırasında çalıştırılacak komutları belirtiriz.
- Bu komutlar linux komutları, shell scriptler, python scriptler olabilir. Örneğin:
```bash
RUN apt-get update
RUN apt-get upgrade -y 
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install fastapi
RUN python3 app.py
RUN mkdir /app
```
not: aynı anda birden fazla komut çalıştırmak istiyorsak && kullanabiliriz.Bu şekilde daha az katman oluşturmuş oluruz image'ımızın boyutu küçülür.Örneğin:
```bash
RUN apt-get update && apt-get upgrade -y && apt-get install -y python3 python3-pip
```

## WORKDIR
- Dockerfile içerisinde image'ımızın oluşturulması sırasında hangi dizinde çalışılacağını belirtiriz.Örneğin:
```bash
WORKDIR /app
```

## COPY
- Dockerfile içerisinde image'ımızın oluşturulması sırasında bilgisayarımızdaki dosyaları image'ımıza kopyalamak için kullanılır.Örneğin:
```bash
COPY . /app
- . -> bilgisayarımızda bulunduğumuz dizini temsil eder.
- /app -> image'ımızda oluşturulacak olan dizini temsil eder.

COPY app.py config.py requirements.txt /app/
```

## ADD
- Dockerfile içerisinde image'ımızın oluşturulması sırasında bilgisayarımızdaki yada internet üzerinden dosyaları image'ımıza kopyalamak için kullanılır.Örneğin:
```bash
ADD . /app
- . -> bilgisayarımızda bulunduğumuz dizini temsil eder.

ADD app.py config.py requirements.txt /app/
```

## EXPOSE
- Dockerfile içerisinde image'ımızın oluşturulması sırasında hangi porttan dışarıya açılacağını belirtiriz.Örneğin:
```bash
EXPOSE 80
EXPOSE 443
```


## CMD
- Dockerfile içerisinde image'ımızın oluşturulması sırasında container'ımızın çalıştırılacağı komutları belirtiriz.
- Dockerfile içerisinde sadece bir tane CMD komutu olabilir.
- CMD komutu genelde container'ımızın çalıştırılacağı ana komutu belirtir

Örneğin:
```bash
CMD ["python3", "app.py"]
CMD ["echo", "deneme.txt"]
```

## Build Aşaması
- Dockerfile içerisinde image'ımızın nasıl oluşturulacağını belirttikten sonra image'ımızı oluşturmak için build aşamasına geçeriz.

Örneğin:
```bash
docker build -t myimage:latest .
- -t -> image'ımıza isim veririz.
- . -> Dockerfile'ın bulunduğu dizini temsil eder.
```
- İmage'ımızı oluşturduktan sonra image'ımızı çalıştırmak için run aşamasına geçeriz.Örneğin:
```bash
docker run --name mycontainer  myimage:latest
```

## Docker Hub
- Docker Hub, Docker tarafından sağlanan bir bulut tabanlı hizmettir. Docker Hub, Docker image'larınızı depolamanıza, yönetmenize ve paylaşmanıza olanak tanır.
- Docker Hub üzerinde image'larınızı paylaşabilir ve başkalarının image'larını kullanabilirsiniz.
- Docker Hub üzerinde image'larınızı paylaşmak için öncelikle Docker Hub'a üye olmanız gerekmektedir.
- Docker Hub üzerinde image'larınızı paylaşmak için öncelikle image'ınızı Docker Hub'a push etmeniz gerekmektedir.Örneğin:
```bash
docker login
docker tag myimage:latest myusername/myimage:latest
docker push myusername/myimage:latest
```



