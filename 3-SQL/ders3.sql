-- SubQuery
-- Subquery (Alt Sorgu) SQL sorgularında bir sorgunun içinde başka bir sorgunun kullanılmasıdır.

-- Where ile subquery kullanımı
-- Alexander Hunold dan daha fazla maaş alan çalışanları listeleyiniz.

select salary from hr.employees where last_name = 'Hunold';

select 
    first_name,
    last_name,
    salary
from hr.employees 
where salary > (select salary from hr.employees where last_name = 'Hunold');

-- Location_id si 1700 den büyük olan departmanlarda çalışanları listeleyiniz.
select department_id from hr.departments where location_id >1700;

select 
    first_name,
    last_name,
    salary
from hr.employees 
where department_id IN (select department_id from hr.departments where location_id >1700);


-- Southlake de çalışanları listeleyiniz.

-- Southlake'in location_id sini bulduk
select location_id from hr.locations where city ='Southlake';

-- location_id değerinden yola çıkarak Southlake de bulunan departmanlarım neler ?
select 
    department_id 
from hr.departments 
where location_id = (select location_id from hr.locations where city ='Southlake');

-- Bulduğumuz department_id leri ile eşleşen kişileri listeleyebiliriz
select 
    first_name,
    last_name,
    salary
from hr.employees 
where department_id IN (select 
                            department_id 
                        from hr.departments 
                        where location_id = (select location_id from hr.locations where city ='Southlake'));

-- From ile subquery kullanımı
-- Departman ve Employee tablosunu subquery ile birleştirip çalışanların 10000 üzerindeki maaş ortalamasını listeleyiniz.

select
    * 
from hr.employees e
inner join hr.departments d on e.department_id = d.department_id;

select 
    * 
From (
    select * from hr.employees e 
    inner join hr.departments d on e.department_id = d.department_id) ed
where ed.salary > 10000;


-- Select Subquery kullanımı
-- first_name, last_name, salary, department_name, job_title bilgilerini listeleyiniz.

select 
    first_name, last_name, salary,
    (select department_name from hr.departments d where d.department_id = e.department_id) department_name,
    (select job_title from hr.jobs j where j.job_id = e.job_id ) job_title
from hr.employees e;


-- Analitik Fonksiyonlar
-- Window Functions Keywords
-- 1. OVER: OVER keywordü ile analitik fonksiyonlar belirtilir. 
-- 2. PARTITION BY: PARTITION BY keywordü ile gruplama yapılır.
-- 3. ORDER BY: ORDER BY keywordü ile sıralama yapılır.
-- 4. ROWS BETWEEN: ROWS BETWEEN keywordü ile belirli bir aralıkta işlem yapılır.
-- 5. ROW_NUMBER: ROW_NUMBER fonksiyonu ile sıralı numaralar verilir.
-- 6. RANK: RANK fonksiyonu ile sıralı numaralar verilir ve eşitlik durumunda aynı numara verilir.
-- 7. DENSE_RANK: DENSE_RANK fonksiyonu ile sıralı numaralar verilir ve eşitlik durumunda aynı numara verilir ama boşluk bırakmaz.

-- her yeni kişide maaşlar ne kadar artmış
select 
    employee_id,first_name, last_name, salary,
    sum(salary) OVER (order by employee_id) as total_salary
from hr.employees;

-- Partition By örneği
-- Departman Bazlı kişilerin maaşları toplamı

select 
    department_id,first_name, last_name, salary,
    sum(salary) OVER (Partition by department_id order by employee_id) as total_salary
from hr.employees;

-- Departman Bazlı En Yüksek Maaş
select 
    department_id,first_name, last_name, salary,
    max(salary) OVER (Partition by department_id) as max_salary
from hr.employees;

-- Row Number örneği
-- Row Number otomatik olarak sıralı numaralar verir ve eğer aynı değer varsa farklı numaralar verir. (employee_id=189 )
-- Her çalışanın maaş sırasını departmana göre sıralanması
select 
    employee_id,first_name, last_name, department_id,salary,
    ROW_NUMBER() OVER (Partition by department_id order by salary desc) as salary_rank
from hr.employees;



-- Rank örneği
-- Rank fonksiyonu sıralı numaralar verir ve eğer aynı değer varsa aynı numaralar verir ama farklı değere geçince boşluklu numaralar verir. (employee_id=189 )
-- Her çalışanın maaş sırasını departmana göre sıralanması
select 
    employee_id,first_name, last_name, department_id,salary,
    RANK() OVER (Partition by department_id order by salary desc) as salary_rank
from hr.employees;


-- Dense Rank örneği
-- Dense Rank fonksiyonu sıralı numaralar verir ve eğer aynı değer varsa aynı numaralar verir ama farklı değere geçince boşluklu numaralar vermez. (employee_id=189 )
-- Her çalışanın maaş sırasını (eşit maaşlar aynı sırayı alır, boşluk olmadan) departmana göre sıralamak
select 
    employee_id,first_name, last_name, department_id,salary,
    DENSE_RANK() OVER (Partition by department_id order by salary desc) as salary_rank
from hr.employees;




-- CASE WHEN 
-- Case when sqlde koşullu ifadeler yazmamızı sağlar.
-- Genel kullanımı şu şekildedir.
-- CASE
--     WHEN koşul THEN sonuç
--     WHEN koşul THEN sonuç
--     ELSE sonuç
-- END
-- WHEN koşul sağlanırsa sonuç döner, sağlanmazsa bir sonraki koşula bakılır. Hiçbir koşul sağlanmazsa else bloğu çalışır.
-- THEN bloğu çalıştıktan sonra case bloğu sonlanır.

-- Maaşı 10000 den büyük olan kişileri yüksek maaşlı,5000 den büyük olanları orta maaşlı, diğerlerini düşük maaşlı olarak belirleyiniz.
select
	first_name, last_name,salary,
	CASE
		WHEN salary >10000 THEN 'Yüksek Maaşlı'
		WHEN salary >5000 THEN 'Orta Maaşlı'
		ELSE 'Düşük Maaşlı'
	END as salary_level
from hr.employees;


-- Maaşı 10000 den büyük olan kişilerin maaşlarını 10% arttırınız.
select
	first_name, last_name,salary,
	CASE
		WHEN salary >10000 THEN salary * 1.1
		ELSE salary
	END as salary_level
from hr.employees;


-- Birden fazla koşul
-- Maaşı 10000 den büyük olan ve departmanı 90 olan kişilerin maaşlarını 10% arttırınız.
select
	department_id,first_name, last_name,salary,
	CASE
		WHEN salary >10000 and department_id = 90 THEN salary * 1.1
		ELSE salary
	END as salary_level
from hr.employees;




-- Bu komutlar livesql de yetkiden dolayı çalışmıyor
-- Temel İnsert İşlemleri

-- Tek bir kayıt ekleme
INSERT INTO hr.employees (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id)
VALUES (207, 'Ali', 'Veli', 'example@email.com', '123456789', '01-JAN-2021', 'IT_PROG', 10000, 0.1, 100, 90);

-- Birden fazla kayıt ekleme
INSERT INTO hr.employees (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id)
VALUES (208, 'Ali', 'Veli', 'example@email.com', '123456789', '01-JAN-2021', 'IT_PROG', 10000, 0.1, 100, 90),
       (209, 'Ali', 'Veli', 'example@email.com', '123456789', '01-JAN-2021', 'IT_PROG', 10000, 0.1, 100, 90),
       (210, 'Ali', 'Veli', 'example@email.com', '123456789', '01-JAN-2021', 'IT_PROG', 10000, 0.1, 100, 90);

-- Temel Update İşlemleri
-- 207 nolu çalışanın maaşını 15000 yapalım
UPDATE hr.employees
SET salary = 15000
WHERE employee_id = 207;

-- Temel Delete İşlemleri
-- 207 nolu çalışanı silelim
DELETE FROM hr.employees
WHERE employee_id = 207;




-- Tablo Oluşturma

-- Veri tipleri
-- Veri tipleri belirleme bize Consistency(Veri tutarlılığı) sağlar yani A tablosunun x kolonu integer ise eşleştirme yapacağımız 
-- B tablosunun y kolonu da integer olmalıdır aksi takdirde veri tutarlılığı bozulur eksta dönüşüm işlemleri yapmamız gerekir.

-- Her kolonun bir veri tipi vardır ve bu veri tipleri veri tabanına göre değişiklik gösterebilir.

-- Kolonlarda verilecek veriler en uygun veri tipi seçilerek saklanmalıdır. Örneğin bir kolonda sadece sayısal değerler varsa bu kolonun veri tipi integer olmalıdır.
-- Ama sadece yaşını tutuyorsa bu yapı integerın daha az yer kaplayan bir veri tipi olan tinyint gibi bir veri tipi seçilebilir.



-- Kısıtlamalar (Constraints) ve İlişkisel Veritabanı Tasarımı

-- Kısıtlamalar (Constraints)
-- Kısıtlamalar veritabanında veri bütünlüğünü sağlamak için kullanılır. 
-- Kısıtlamalar sayesinde veritabanında veri bütünlüğü sağlanır ve veritabanında hatalı veri girişleri engellenir.

-- Kısıtlamalar
-- 1. NOT NULL: Bir kolonun değerinin null olmasını engeller.
-- 2. UNIQUE: Bir kolonun değerinin benzersiz olmasını sağlar.
-- 3. PRIMARY KEY: Bir kolonun benzersiz olmasını ve null olmamasını sağlar.
-- 4. FOREIGN KEY: İki tablo arasındaki ilişkiyi sağlar.





