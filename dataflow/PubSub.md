# Pub/Sub

**Topic** : Pub/Sub yapıları, birçok uygulama tarafından kullanılan bir mesajlaşma modelidir. Bu modelde, mesajlar bir **topic** üzerinden yayınlanır ve bu topic'e abone olan uygulamalar bu mesajları alır. Bu model, uygulamalar arasında asenkron mesajlaşma sağlar.

**Publisher** : Mesajları yayınlayan uygulamalardır.

**Subscriber** : Mesajları alan uygulamalardır.

**Message** : Yayınlanan mesajlardır.

**Schema** : Mesajların formatını belirler. Mesajlar Avro formatında olabilir.

ornek bir schema:

Elimizde ürettiğimiz veri

```json
{
  "Education": "Bachelors",
  "JoiningYear": 2017,
  "City": "Bangalore",
  "PaymentTier": 3,
  "Age": 34,
  "Gender": "Male",
  "EverBenched": "No",
  "ExperienceInCurrentDomain": 0,
  "LeaveOrNot": 0
}
```

Avro formatında olacak şekilde schema:
ornek_schema
```json
{
  "type": "record",
  "name": "Employee",
  "fields": [
    { "name": "Education", "type": "string" },
    { "name": "JoiningYear", "type": "int" },
    { "name": "City", "type": "string" },
    { "name": "PaymentTier", "type": "int" },
    { "name": "Age", "type": "int" },
    { "name": "Gender", "type": "string" },
    { "name": "EverBenched", "type": "string" },
    { "name": "ExperienceInCurrentDomain", "type": "int" },
    { "name": "LeaveOrNot", "type": "int" }
  ]
}
```

**Type** : Mesajların formatını belirler.

**Name** : Mesajın adını belirler.

**Fields** : Mesajın içeriğini belirler.


Bu yapının Bigquerydeki tablo create komutu

```sql

CREATE TABLE `scenic-parity-429506-b8.de_nisan.dataflow`
(
  Education STRING,
  JoiningYear INT64,
  City STRING,
  PaymentTier INT64,
  Age INT64,
  Gender STRING,
  EverBenched STRING,
  ExperienceInCurrentDomain INT64,
  LeaveOrNot INT64
)
```

Not: Pub/Sub dan bigquerye veri aktarımı direkt yapılır fakat IAM den yetkilendime verilmesi gerekmektedir.

Use-schema yı seçince aşağıdakine benzer bir hata alıncak

- Cannot determine whether service account `service-683276613998@gcp-sa-pubsub.iam.gserviceaccount.com` has permission to write to the BigQuery table. Please check that the table exists and that permissions are configured.


Bu hatayı çözmek için aşağıdaki adımları takip edebilirsiniz.

1. IAM & Admin kısmına gidin.
2. IAM kısmına tıklayın ve Grant Access butonuna tıklayın.
3. hatada veriler accountu yetki mail kısmına yapıştırın.
4. Role kısmına BigQuery Admin ve BigQuery Data Editor seçin.