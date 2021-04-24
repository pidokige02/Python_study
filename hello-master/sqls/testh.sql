select d.department_name, e.* from departments d inner join employees e on d.department_id = e.department_id;

select * from Test2;

truncate table Test2;

insert into Test2 values(1, '한글', 1);

insert into Test2 set id=1, name='한글', t=1;

desc Test2;

select * from jobs;

select * from Jobs where job_title like '%Presiden_';

SELECT 
       TO_CHAR(e.HIRE_DATE, 'YYYY') AS HIRE_DATE, AVG(e.salary) AS AVG
  FROM EMPLOYEES e, JOBS j
 WHERE e.JOB_ID = j.JOB_ID AND j.JOB_TITLE = 'Sales Manager' 
 GROUP BY TO_CHAR(e.HIRE_DATE,'YYYY')
 ORDER BY 1 ASC
;

SELECT 
       TO_CHAR(e.HIRE_DATE, 'YYYY') AS HIRE_DATE, AVG(e.salary) AS AVG
  FROM EMPLOYEES e inner join JOBS j on e.JOB_ID = j.JOB_ID
 WHERE j.JOB_TITLE = 'Sales Manager' 
 GROUP BY TO_CHAR(e.HIRE_DATE,'YYYY')
 ORDER BY 1 ASC
;