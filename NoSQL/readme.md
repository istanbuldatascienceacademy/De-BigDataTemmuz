# Kurulum adımları

Standart bir VM makine kur firewall ları aç

```bash
sudo su

apt update && apt upgrade -y && apt install docker.io -y && apt install docker-compose -y


nano docker-compose.yml
```

```yaml
version: "3"
services:
  cassandra:
    image: cassandra:latest
    container_name: cassandra
    restart: always
    ports:
      - 9042:9042
```	

```bash
docker-compose up -d
```


# Cassandra 101

Casandra, Apache Software Foundation tarafından geliştirilen, yüksek performanslı, dağıtık, açık kaynaklı bir NoSQL veritabanıdır. Cassandra, Google'un BigTable ve Amazon'un Dynamo sistemlerinden esinlenerek geliştirilmiştir. Cassandra, yüksek performans, yüksek ölçeklenebilirlik ve yüksek kullanılabilirlik sağlamak için tasarlanmıştır. Cassandra, verileri çok büyük bir küme üzerinde dağıtılmış bir şekilde depolamak ve işlemek için tasarlanmıştır. Cassandra, verileri çok büyük bir küme üzerinde dağıtılmış bir şekilde depolamak ve işlemek için tasarlanmıştır. Cassandra, verileri çok büyük bir küme üzerinde dağıtılmış bir şekilde depolamak ve işlemek için tasarlanmıştır. Cassandra, verileri çok büyük bir küme üzerinde dağıtılmış bir şekilde depolamak ve işlemek için tasarlanmıştır. Cassandra, verileri çok büyük bir küme üzerinde dağıtılmış bir şekilde depolamak ve işlemek için tasarlanmıştır. Cassandra, verileri çok büyük bir küme üzerinde dağıtılmış bir şekilde depolamak ve işlemek için tasarlanmıştır. Cassandra, verileri çok büyük bir küme üzerinde dağıtılmış bir şekilde depolamak ve işlemek için tasarlanmıştır. Cassandra, verileri çok büyük bir küme üzerinde dağıtılmış bir şekilde depolamak ve işlemek için tasarlanmıştır. Cassandra, verileri çok büyük bir küme üzerinde dağıtılmış bir şekilde depolamak ve işlemek için tasarlanmıştır. Cassandra, verileri çok büyük bir küme üzerinde dağıtılmış bir şekilde depolamak ve işlemek için tasarlanmıştır.

## Cassandra'nın Terimleri
``Node``: Cassandra kümesindeki her bir fiziksel sunucuya node denir. Cassandra kümesindeki her bir node, verilerin depolandığı ve işlendiği birimdir.

``Cluster``: Cassandra kümesi, birden fazla node'dan oluşan bir yapıdır. Cassandra kümesi, verilerin dağıtıldığı ve işlendiği birimdir.

``Data Center``: Cassandra kümesindeki node'ların fiziksel olarak konumlandığı birimdir. Cassandra kümesinde birden fazla data center olabilir.

``KeySpace``: Cassandra'da verilerin saklandığı birim KeySpace olarak adlandırılır. KeySpace, bir veritabanı gibi düşünülebilir.

``Table``: Cassandra'da verilerin saklandığı birim Table olarak adlandırılır. Table, bir tablo gibi düşünülebilir.

``Column``: Cassandra'da verilerin saklandığı birim Column olarak adlandırılır. Column, bir sütun gibi düşünülebilir.

``Row``: Cassandra'da verilerin saklandığı birim Row olarak adlandırılır. Row, bir satır gibi düşünülebilir.

``Primary Key``: Cassandra'da verilerin birincil anahtarını belirten birimdir. Primary Key, verilerin benzersiz bir şekilde tanımlanmasını sağlar.

``Secondary Key``: Cassandra'da verilerin ikincil anahtarını belirten birimdir. Secondary Key, verilerin birincil anahtara göre sıralanmasını sağlar.

``Replication Factor``: Cassandra'da verilerin kaç düğüme replike edileceğini belirten birimdir. Replication Factor, verilerin yedeklenmesini sağlar.

``Consistency Level``: Cassandra'da veri konsistansını belirten birimdir. Consistency Level, verilerin güncel ve doğru olmasını sağlar.

## Cassandra'nın Özellikleri
Yüksek Performans: Cassandra, yüksek performanslı bir veritabanıdır. Cassandra, verileri çok hızlı bir şekilde işleyebilir.

Yüksek Ölçeklenebilirlik: Cassandra, yüksek ölçeklenebilir bir veritabanıdır. Cassandra, verileri çok büyük bir küme üzerinde dağıtılmış bir şekilde depolayabilir.

Yüksek Kullanılabilirlik: Cassandra, yüksek kullanılabilir bir veritabanıdır. Cassandra, verilerin her zaman erişilebilir olmasını sağlar.

Esnek Veri Modeli: Cassandra, esnek bir veri modeline sahiptir. Cassandra, ilişkisel olmayan verileri saklamak için uygun bir veritabanıdır.

Dağıtık Mimari: Cassandra, dağıtık bir mimariye sahiptir. Cassandra, verileri çok sayıda node üzerinde dağıtılmış bir şekilde saklar.

Yüksek Güvenlik: Cassandra, yüksek güvenlikli bir veritabanıdır. Cassandra, verilerin güvenli bir şekilde saklanmasını sağlar.

## Cassandra CQL İşlemleri

Cassandra Docker konteynerine bağlanmak için aşağıdaki komutu kullanabilirsiniz.
```bash
docker exec -it cassandra cqlsh
```


### KeySpace İşlemleri
Cassandra'da verilerin saklandığı birim KeySpace olarak adlandırılır. KeySpace, bir veritabanı gibi düşünülebilir. KeySpace oluşturmak için aşağıdaki komutu kullanabilirsiniz.
```sql
CREATE KEYSPACE IF NOT EXISTS istdsa_keyspace WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};
-- If Not Exists: KeySpace daha önce oluşturulmuşsa tekrar oluşturulmaz.
-- WITH REPLICATION: KeySpace'in replikasyon stratejisi belirtilir.
-- SimpleStrategy: Verilerin birincil ve ikincil düğümlere dağıtılmasını sağlar.
-- SimpleStrategy alternatif olarak NetworkTopologyStrategy kullanılabilir.
-- replication_factor: Verilerin kaç düğüme replike edileceğini belirler.
```
KeySpace listelemek için aşağıdaki komutu kullanabilirsiniz.
```sql
DESC KEYSPACES;
```
KeySpace'e bağlanmak için aşağıdaki komutu kullanabilirsiniz.
```sql
USE istdsa_keyspace;
```
KeySpace'den çıkmak için aşağıdaki komutu kullanabilirsiniz. 
Bu komutla komple çıkış yapmış olursunuz.
```sql
EXIT;
```
KeySpace silmek için aşağıdaki komutu kullanabilirsiniz.
```sql
DROP KEYSPACE istdsa_keyspace;
```

### Tablo İşlemleri
Cassandra'da tablo oluşturmak için aşağıdaki komutu kullanabilirsiniz.
```sql
CREATE TABLE IF NOT EXISTS istdsa_keyspace.istdsa_table (
    id uuid PRIMARY KEY,
    name text,
    address text
);
-- id: Tablonun birincil anahtarıdır.
-- uuid: Universally Unique Identifier (Evrensel Benzersiz Tanımlayıcı) anlamına gelir.
-- Cassandra'da birincil anahtarlar genellikle UUID olarak tanımlanır.
-- PRIMARY KEY: Tablonun birincil anahtarını belirtir.
```
uuid kullanılmasının nedeni, verilerin dağıtılmış bir şekilde saklanmasıdır. uuid, verilerin benzersiz bir şekilde tanımlanmasını sağlar. 
Bu da id'lerin çakışmasını engeller ve verilerin dağıtılmış bir şekilde saklanmasını sağlar.

Tablo listelemek için aşağıdaki komutu kullanabilirsiniz.
```sql
DESC TABLES;
```

Tablo silmek için aşağıdaki komutu kullanabilirsiniz.
```sql
DROP TABLE istdsa_keyspace.istdsa_table;
```


### Veri İşlemleri
Veri eklemek için aşağıdaki komutu kullanabilirsiniz.
```sql
INSERT INTO istdsa_keyspace.istdsa_table (id, name, address) VALUES (uuid(), 'Zekeriya', 'Adres Deneme 1');

INSERT INTO istdsa_keyspace.istdsa_table (id, name, address) VALUES (uuid(), 'Ali', 'Adres Deneme 2');

INSERT INTO istdsa_keyspace.istdsa_table (id, name, address) VALUES (uuid(), 'Veli', 'Adres Deneme 3');
```
uuid() fonksiyonu ile benzersiz bir id oluşturulur.

Veri çekmek için aşağıdaki komutu kullanabilirsiniz.
```sql
SELECT * FROM istdsa_keyspace.istdsa_table;
```

Not: Cassandra da ve diğer NoSQL veritabanlarında veri güncelleme ve silme işlemleri oldukça maliyetlidir. Bu nedenle veri güncelleme ve silme işlemleri yerine veri eklemek daha yaygındır. Ancak veri güncelleme ve silme işlemleri de mümkündür. Aşağıda veri güncelleme ve silme işlemleri için örnekler verilmiştir ama id değerleri UUID olduğu için bu işlemler yapılamaz.


Veri güncellemek için aşağıdaki komutu kullanabilirsiniz.
```sql
UPDATE istdsa_keyspace.istdsa_table SET name = 'Ali' WHERE <UUID> = 1;
```

Veri silmek için aşağıdaki komutu kullanabilirsiniz.
```sql
DELETE FROM istdsa_keyspace.istdsa_table WHERE <UUID> = 1;
```

Cassandrada veri çekme işlemlerinde WHERE koşulu kullanıldığında ve kullanılan kolonun birincil anahtar olmadığı durumlarda ALLOW FILTERING anahtar kelimesi kullanılması gerekmektedir. 
```sql
SELECT * FROM istdsa_keyspace.istdsa_table WHERE name = 'Zekeriya' ALLOW FILTERING;
```

### Aggregation İşlemleri

Count işlemi
```sql
SELECT COUNT(*) FROM istdsa_keyspace.istdsa_table;
```

Sum işlemi
```sql
SELECT SUM(<UUID>) FROM istdsa_keyspace.istdsa_table;
```

