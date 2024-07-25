-- En Temel sorgumus Select'dir
select * from all_tables;

select * from hr.employees;

select FIRST_NAME,LAST_NAME from hr.employees;

select FIRST_NAME,LAST_NAME,salary from hr.employees;

select FIRST_NAME,LAST_NAME,salary+10 from hr.employees;

select FIRST_NAME,LAST_NAME,salary*2 from hr.employees;

select FIRST_NAME,LAST_NAME,(salary*2)+100 from hr.employees;

select FIRST_NAME,LAST_NAME,(salary*2)+100 as iki_kat_maas from hr.employees;

select FIRST_NAME,LAST_NAME,(salary*2)+100 iki_kat_maas from hr.employees;

select FIRST_NAME,LAST_NAME,(salary*2)+100 as "2 kat maaş" from hr.employees;

select FIRST_NAME,LAST_NAME,(salary*2)+100 "2 kat maaş" from hr.employees;

select first_name ||' ' || last_name "Isim", salary maas,12*commission_pct*salary "komisyon tutari" from hr.employees 

select first_name || '' || last_name "Isim",salary maas,12*commission_pct*salary "komisyon tutari" from hr.employees 

select first_name || '-' || last_name "Isim",salary maas,12*commission_pct*salary "komisyon tutari" from hr.employees 

desc hr.employees ;


select distinct department_id from hr.employees;

select * from hr.employees;

select * from hr.employees where department_id=90;

-- Tek tırnak kullanılmaz ise hata verir
select * from hr.employees where last_name=King;

select * from hr.employees where last_name='King';

select * from hr.employees where last_name='king';

select * from hr.employees where lower(last_name)='king';

select * from hr.employees where salary=24000;

select * from hr.employees where salary>13000;

select * from hr.employees where salary<13000;

select * from hr.employees where salary>=10000 and salary <= 11000;

select * from hr.employees where salary between 10000 and 11000;

select * from hr.employees where employee_id in(113,125,150);

select * from hr.employees where FIRST_NAME like 'L%';

select * from hr.employees where FIRST_NAME like 'Lu%';

select * from hr.employees where FIRST_NAME like '%s';

select * from hr.employees where FIRST_NAME like '%ex%';

select * from hr.employees where FIRST_NAME like '%is%';

select * from hr.employees where FIRST_NAME like 'S_n%';

select * from hr.employees where FIRST_NAME like 'S%n';

select * from hr.employees where COMMISSION_PCT is null;

select * from hr.employees where MANAGER_ID is NULL;

select * from hr.employees where MANAGER_ID is not NULL;


-- AGG İşlemleri
-- Count,Min, Max,AVG, SUM

select count(*) from hr.employees;

select count(*) from hr.employees where department_id=90;

select count(*) as toplam_calisan from hr.employees where department_id=90;

select min(HIRE_DATE) from hr.employees;

select * from hr.employees where HIRE_DATE='13-JAN-01';

-- Hata alınacak
-- select FIRST_NAME, min(HIRE_DATE) from hr.employees;

select max(HIRE_DATE) from hr.employees;

select avg(salary) from hr.employees;

select max(salary) from hr.employees;

select min(salary) from hr.employees;

select sum(salary) from hr.employees;

select 
    avg(salary),
    max(salary), 
    min(salary),
    sum(salary)
from hr.employees;

-- Group By İşlemleri

Select 
    department_id, 
    Avg(salary) as avg_salary
from hr.employees
Group By department_id;


Select 
    department_id, 
    Avg(salary) as avg_salary
from hr.employees
Group By department_id
Order by avg_salary;


Select 
    department_id, 
    Avg(salary) as avg_salary
from hr.employees
Group By department_id
Order by avg_salary ASC;

Select 
    department_id, 
    Avg(salary) as avg_salary
from hr.employees
Group By department_id
Order by avg_salary DESC;


Select 
    department_id, 
    Count(*) as count_
from hr.employees
Group By department_id
ORDER BY count_ Desc;

Select 
    department_id, 
    Count(*) as count_,
    Round(Avg(salary),3) as avg_salary
from hr.employees
Group By department_id
ORDER BY count_ Desc;

SELECT 
    department_id, 
    Min(salary) as min_salary,
    Max(salary) as max_salary
from hr.employees
GROUP BY department_id
ORDER BY min_salary;



