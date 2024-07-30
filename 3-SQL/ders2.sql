-- 2li gruplama
-- 2 li gruplamada gelen değer önce ilk sütuna göre sıralanır ardından ilk sütunun aynı olanlar arasında ikinci sütuna göre sıralanır
-- Her departmanda toplam maaş giderini  departman öncelikli daha sonra da maneger öncelikli olacak şekilde listeleyiniz. maaşı yüksekten düşüğe sıralayınız 

SELECT 
    department_id, 
    manager_id,
    sum(salary) as sum_salary
from hr.employees
GROUP BY department_id,manager_id
Order by sum_salary desc;

-- Hata alınacak
-- Ortalama maaşı 10000 üzerinde maaş alan çalışanları gruplayarak listeleyiniz.
SELECT 
    department_id, 
    avg(salary) as avg_salary
from hr.employees
where avg(salary) > 10000
GROUP BY department_id;

-- Having

-- Ortalama maaşı 10000 üzerinde maaş alan çalışanları gruplayarak listeleyiniz.
SELECT 
    department_id, 
    avg(salary) as avg_salary
from hr.employees
GROUP BY department_id
Having avg(salary) > 10000;

-- Toplam maaş gideri 51608 üzerinde olan departmanları listeleyiniz.
SELECT 
    department_id, 
    sum(salary) as sum_salary
from hr.employees
GROUP BY department_id
Having sum(salary) > 51608;


-- departmandaki 13-JAN-02 yılı ile 21-APR-06 yılında işe başlayan kişilerin 
-- maaş ortalamasını 10000 üzerinde olanları Büyükten küçüğe listeleyiniz
SELECT 
    department_id, 
    avg(salary) as avg_salary
from hr.employees
    where hire_date between '13-JAN-02' and '21-APR-06'
GROUP BY department_id
Having avg(salary) >= 10000
Order by avg_salary desc;

-- Joinler
-- Inner Join

-- Employees tablosundan first_name, last_name, salary getir Departments tablosundan department_name getir
-- Uzun hali
Select
	first_name, 
    last_name, 
    salary,
    department_name
From hr.employees
Inner join hr.Departments on hr.Departments.department_id = hr.employees.department_id;

-- Kısa hali 
Select
	e.first_name, 
    e.last_name, 
    e.salary,
    d.department_name
From hr.employees e
Inner join hr.Departments d on d.department_id = e.department_id;


-- Employees tablosundan first_name, last_name, salary getir Jobs tablosundan job_title getir
Select
	e.first_name, 
    e.last_name, 
    e.salary,
	j.job_title
From hr.employees e
Inner join hr.Jobs j on j.job_id = e.job_id;



-- Employees tablosundan first_name, last_name, salary  getir Job_history tablosundan start_date getir
Select
	e.first_name, 
    e.last_name, 
    e.salary,
	jh.start_date
From hr.employees e
Inner join hr.Job_history jh on jh.employee_id = e.employee_id;


-- departman adı, çalışan adı, soyadı, maaş bilgisi ve iş adı bilgilerini listeleyiniz.
Select
	e.first_name, 
    e.last_name, 
    e.salary,
    d.department_name,
    j.job_title
From hr.employees e
Inner join hr.Jobs j on j.job_id = e.job_id
Inner join hr.Departments d on d.department_id = e.department_id
Order by e.salary desc;



-- Her departmanda en az ve en çok maaş alan çalışanların maaş bilgilerini listeleyiniz.
Select
    d.department_name,
    min(salary) min_salary,
    max(salary) max_salary
From hr.employees e
Inner join hr.Departments d on d.department_id = e.department_id
group by d.department_name;


-- Left Join
-- Left Join'de Ana tablo from kısmında olmalıdır
-- İki tabloyu birleştirirken, birinci (sol) tablodaki tüm satırları ve 
-- ikinci (sağ) tablodaki yalnızca eşleşen satırları alır. 
-- Eşleşmeyen satırlar için sağ tablodan gelen sütunlar NULL olarak döner. 

-- Employees tablosundan first_name, last_name, salary Department tablosundan department_name getir
Select
	e.first_name, 
    e.last_name, 
    e.salary,
    d.department_name
From hr.employees e
Left join hr.Departments d on d.department_id = e.department_id;


-- Employees tablosundan first_name, last_name, salary  getir Jobs tablosundan job_title getir
Select
	e.first_name, 
    e.last_name, 
    e.salary,
	j.job_title
From hr.employees e
Left join hr.Jobs j on j.job_id = e.job_id;



-- Right Join kullanımı
-- Right Join'de Ana tablo Join kısmında olmalıdır

-- Employees tablosundan first_name, last_name, salary job_id getir Jobs tablosundan job_title getir
Select
	e.first_name, 
    e.last_name, 
    e.salary,
	j.job_title
From hr.employees e
Right join hr.Jobs j on j.job_id = e.job_id;


-- Full Join kullanımı
-- Full joinde iki tablodan birinde olmayan veriler de getirilir, dolayısıyla null değerler de getirilir.
-- Employees tablosundan first_name, last_name, salary job_id getir Jobs tablosundan job_title getir
SELECT 
    e.first_name, 
    e.last_name, 
    e.salary,
    j.job_title
from hr.employees e
FULL JOIN hr.jobs j ON e.job_id = j.job_id;


-- Employees tablosundan first_name, last_name, salary , Locations tablosundan  City, Regions tablosundan region_name getir( Inner Join ile)
Select
	e.first_name, 
    e.last_name, 
    e.salary,
    l.city,
	r.region_name        
From hr.employees e
Inner join hr.Departments d on d.department_id = e.department_id
Inner join hr.locations l on d.location_id = l.location_id
Inner join hr.countries c on l.country_id = c.country_id
Inner join hr.regions r on c.region_id = r.region_id;


-- View

Create or replace View ornek_view as
Select
	e.first_name, 
    e.last_name, 
    e.salary,
    l.city,
	r.region_name        
From hr.employees e
Inner join hr.Departments d on d.department_id = e.department_id
Inner join hr.locations l on d.location_id = l.location_id
Inner join hr.countries c on l.country_id = c.country_id
Inner join hr.regions r on c.region_id = r.region_id;

select * from user_views;

select * from ornek_view;











