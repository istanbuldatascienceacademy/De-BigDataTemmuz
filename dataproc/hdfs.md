# Temel HDFS işlemleri

1. Dosya veya Dizin Listeleme:
```bash
hdfs dfs -ls [path]
hdfs dfs -ls /
hdfs dfs -ls /user/
hdfs dfs -ls /user/hdfs
```
2. Dizin Oluşturma:
```bash
hdfs dfs -mkdir [path]
hdfs dfs -mkdir /user/hdfs/test
hdfs dfs -mkdir /user/hdfs/test/deneme
```
3. Dosya veya Dizin Silme:
```bash
hdfs dfs -rm [-r] [path]
hdfs dfs -rm -r /user/hdfs/test/deneme
```
4. HDFS'e Dosya Yükleme:
```bash
hdfs dfs -copyFromLocal [src] [dest]
echo "Hello, HDFS!" > deneme.txt
hdfs dfs -copyFromLocal deneme.txt /user/hdfs/test/
hdfs dfs -cat /user/hdfs/test/deneme.txt
```
5. HDFS'den Dosya Kopyalama:
```bash
hdfs dfs -copyToLocal [src] [dest]
mkdir hdfs
hdfs dfs -copyToLocal /user/hdfs/test/deneme.txt /home/yusufgzbyk/hdfs/
```
6. HDFS'e Dosya Taşıma:
```bash
hdfs dfs -moveFromLocal [src] [dest]
echo "Hello, HDFS!" > deneme.txt
hdfs dfs -moveFromLocal deneme.txt /user/hdfs/test/
```
7. HDFS'den Dosya Taşıma:
```bash
hdfs dfs -moveToLocal [src] [dest]
mkdir hdfs
hdfs dfs -moveToLocal /user/hdfs/test/deneme.txt /home/yusufgzbyk/hdfs/

```
8. Dosya veya Dizin Taşıma:
```bash
hdfs dfs -mv [src] [dest]
hdfs dfs -mv /user/hdfs/test/deneme.txt /user/hdfs/test/deneme2.txt # yeniden adlandırma
hdfs dfs -mv /user/hdfs/test/deneme2.txt /user/hdfs/test/deneme/ # taşıma
```
9. Dosya veya Dizin Kopyalama:
```bash
hdfs dfs -cp [src] [dest]
hdfs dfs -cp /user/hdfs/test/deneme2.txt /user/hdfs/test/deneme3.txt # kopyalama
hdfs dfs -mv /user/hdfs/test/deneme2.txt /user/hdfs/test/
```
10. Dosya Okuma:
```bash
hdfs dfs -cat [file]
hdfs dfs -cat /user/hdfs/test/deneme.txt
```
11. Dosya İndirme:
```bash
hdfs dfs -get [src] [dest]
hdfs dfs -get /user/hdfs/test/deneme.txt /home/hdfs/ 
```
12. Dosya veya Dizin İçeriğini Görüntüleme:
```bash
- Dosya veya dizinin boyutunu gösterir.
hdfs dfs -du -h [path]
hdfs dfs -du -h /user/hdfs/test/

```
13. Hadoop Cluster'ı Kontrol Etme:
```bash
hadoop job -list
```