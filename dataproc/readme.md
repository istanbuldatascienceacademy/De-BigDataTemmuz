**Google Dataproc ile Spark Uygulaması: Genişletilmiş Özet**

**1. Hadoop Ekosistemi ve Spark'ın Yükselişi:**
   - **Hadoop'un Gelişim Süreci:** Hadoop, büyük veri dünyasında devrim niteliğinde bir çerçeve olarak ortaya çıktı. HDFS (Hadoop Distributed File System) ve MapReduce, Hadoop ekosisteminin iki temel bileşeni olarak bilinir. HDFS, büyük veri kümelerini depolamak için kullanılırken, MapReduce bu verileri işlemek için dağıtık bir yöntem sunar. Bu yapı, veri mühendislerinin petabayt büyüklüğündeki veri kümeleri üzerinde ölçeklenebilir ve güvenilir analizler yapmasına olanak tanır.
   - **Spark'ın Rolü:** Apache Spark, Hadoop'un performansını önemli ölçüde artıran bir veri işleme motoru olarak geliştirilmiştir. Spark, özellikle bellek içi (in-memory) işlem yetenekleri sayesinde, MapReduce'a kıyasla çok daha hızlı veri işleme sunar. Ayrıca, Spark SQL, MLlib, GraphX gibi bileşenleri ile geniş bir uygulama yelpazesi sunar.

**2. Google Dataproc Üzerinde Hadoop ve Spark Çalıştırma:**
   - **Dataproc'un Avantajları:** Google Dataproc, Hadoop ve Spark iş yüklerini bulutta çalıştırmak için optimize edilmiş bir yönetimli hizmettir. Dataproc, hızlı kurulum, otomatik ölçeklendirme, entegre izleme ve düşük maliyetli işletim avantajları sağlar. Dataproc, kümeleri dakikalar içinde başlatabilme yeteneği ile, geleneksel on-premise Hadoop kurulumlarına kıyasla büyük bir esneklik sunar.
   - **Esneklik ve Ölçeklenebilirlik:** Dataproc, kullanıcıların ihtiyaçlarına göre Hadoop ve Spark kümelerini kolayca özelleştirmesine olanak tanır. Kullanıcılar, gerektiğinde kümelerini otomatik olarak ölçeklendirebilir veya belirli iş yükleri için optimize edebilirler. Bu, maliyetlerin kontrol altında tutulmasını sağlar ve verimliliği artırır.

**3. Google Cloud Storage ve HDFS Karşılaştırması:**
   - **Depolama Alternatifleri:** Google Cloud Storage, Hadoop'un HDFS'sine bir alternatif olarak sunulmaktadır. HDFS, dağıtık veri depolama için kullanılırken, Google Cloud Storage, daha esnek ve ölçeklenebilir bir depolama çözümü sunar. Cloud Storage, kullanıcıların mevcut Hadoop işlerini yeniden yapılandırmadan bulutta çalıştırmasına olanak tanır.
   - **Diğer Google Cloud Ürünleri:** Büyük veri analitiği ve veri depolama ihtiyaçları için Google Cloud, Bigtable ve BigQuery gibi alternatif çözümler sunar. Bigtable, büyük ölçekli yapılandırılmamış verileri yönetmek için ideal bir NoSQL veritabanıdır. BigQuery ise, hızlı ve yüksek performanslı veri analitiği sunan tam yönetimli bir veri ambarıdır. Bu hizmetler, Dataproc ile entegre edilerek daha kapsamlı veri işleme çözümleri oluşturulabilir.

**4. Dataproc Optimizasyon Teknikleri:**
   - **Maliyet Optimizasyonu:** Dataproc, maliyetleri düşürmek için çeşitli optimizasyon seçenekleri sunar. Preemptible VM'ler kullanılarak, düşük maliyetli ve kısa süreli işlem kapasitesi elde edilebilir. Ayrıca, özel makine türleri kullanılarak, spesifik iş yükleri için gerekli olan kaynaklar en verimli şekilde tahsis edilebilir.
   - **Özelleştirilebilir Başlangıç Eylemleri:** Dataproc, kümelerin başlatılması sırasında otomatik olarak çalıştırılacak başlangıç eylemleri tanımlamaya olanak tanır. Bu eylemler, ek yazılımların kurulumu, özel yapılandırmaların uygulanması veya veri kaynaklarının yüklenmesi gibi işlemleri içerir. Bu sayede, kullanıcılar kümelerini tamamen kendi ihtiyaçlarına göre özelleştirebilir.

**5. Dataproc Üzerinde İş Gönderimi ve Yönetimi:**
   - **İş Gönderme Yöntemleri:** Dataproc üzerinde işler, Google Cloud Console, gcloud komut satırı aracı veya REST API aracılığıyla gönderilebilir. Kullanıcılar, bu yöntemlerle işleri kolayca yönetebilir ve izleyebilir. Ayrıca, Dataproc Workflow Templates ve Cloud Composer gibi araçlar, işlerin daha karmaşık iş akışları içinde otomatik olarak yürütülmesini sağlar.
   - **İş Yaşam Döngüsü Yönetimi:** Dataproc, gönderilen işlerin yaşam döngüsünü detaylı bir şekilde yönetir. İşler, bekleme, sıraya alınma, çalışma, hata durumu ve tamamlanma gibi aşamalardan geçer. Kullanıcılar, işlerin durumunu izleyebilir, gerektiğinde müdahale edebilir ve hata durumlarını analiz ederek çözüm üretebilir. Bu süreç, Dataproc'un kullanıcı dostu arayüzleri ve detaylı loglama özellikleri ile desteklenir.


# Bir DataProc Kümesi Oluşturmak

Google Cloud Platform'da bir DataProc kümesi oluşturmak için aşağıdaki adımları izleyebilirsiniz:

1. Google Cloud Platform konsoluna gidin.
2. Sol üst köşede bulunan "Navigation menu" simgesine tıklayın ve "Dataproc" seçeneğini seçin.
3. "Clusters" sayfasına gidin ve "Create cluster" düğmesine tıklayın ve `Cluster on Compute Engine` seçeneğini seçin.
4. İçerideki Ayarları doldurun ve "Create" düğmesine tıklayın.
    - Cluster name: Kümenin adını belirtin.
    - Region: Kümenin oluşturulacağı bölgeyi belirtin.
    - Cluster Type: Oluşacak kümenin türünü belirtin (Single Node)
    - Components: Oluşacak kümenin bileşenlerini belirtin (Hadoop, Spark, Hive, Pig, HBase, Zookeeper)
        - Component Gateway: Oluşacak kümenin bileşenlerinin erişimini belirtin (Enable)
    - Optional Components: Opsiyonel bileşenleri belirtin (`Jupyter Notebook`, Zeppelin) ihtiyacınız olanı seçin.
    - Configre Nodes: Node'ların yapılandırmasını belirtin (Machine type, Number of nodes, Boot disk type, Boot disk size, Preemptibility)
        - Machine type: Node'ların makine türünü belirtin.
            - Series: N2
            - Machine type: n2-standard-4
            - Primary disk size: 100 GB


```bash
gcloud dataproc clusters create denisan-spark --enable-component-gateway --region us-west1 --single-node --master-machine-type n2-standard-4 --master-boot-disk-type pd-balanced --master-boot-disk-size 100 --image-version 2.1-debian11 --optional-components JUPYTER --project scenic-parity-429506-b8
```
