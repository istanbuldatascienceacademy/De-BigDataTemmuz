# Senaryo: 
# Ubuntu imajı üzerine bir dosya kopyalayıp 
# içeriğini ekrana yazdırmak.

FROM ubuntu:latest

# RUN apt-get update
# RUN apt-get upgrade -y 
RUN mkdir /app

# RUN apt-get update && apt-get upgrade -y && mkdir /app

WORKDIR /app

COPY deneme.txt ./

EXPOSE 80

CMD ["cat", "deneme.txt"]

# docker build -t ekrana-yazdir:v1 .
# docker run ekrana-yazdir

# docker login
# docker tag ekrana-yazdir:latest <dockerhub-kullanici-adi>/ekrana-yazdir:latest
# docker push <dockerhub-kullanici-adi>/ekrana-yazdir:latest

