# Docker Volume
- Docker volume container içinde bulunan verilerin silinmesini engellemek için kullanılır.
- Docker volume container'lar arasında veri paylaşımı yapmak için kullanılır.

- Docker volume oluşturmak için:
```bash
docker volume create myvolume
```
- Docker volume'ları listelemek için:
```bash
docker volume ls
```
- Docker volume silmek için:
```bash
docker volume rm myvolume
```
- Docker volume'ları inspect etmek için:
```bash
docker volume inspect myvolume
```
- Docker volume'ları kullanarak container oluşturmak için:
```bash
docker run -d --name mycontainer -v myvolume:/app nginx
```

* Önemli Not: Container oluşturuldukdan sonra volume atama işlemi yapılamaz. Volume atama işlemi container oluşturulurken yapılmalıdır.

* Eğer böyle bir durumla karşılaşırsanız, container'ın ``commit`` edilip yeni bir image oluşturulması gerekmektedir.