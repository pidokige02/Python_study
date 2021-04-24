-- 1) 부서별 직원수
select max(d.department_name) department_name, count(distinct e.employee_id) emp_cnt
  from Employees e inner join Departments d on e.department_id = d.department_id
  group by e.department_id
  order by emp_cnt desc;
  
  
-- 2) 부서별 평균 급여(salary)
select max(d.department_name) department_name, round(avg(e.salary), -1) avg_sal
  from Employees e inner join Departments d on e.department_id = d.department_id
  group by e.department_id
  order by avg_sal desc;
  
  
-- 3) 직책별 평균 급여 (평균급여 기준 상위 7개 직책만) 
-- 방식 1: group by & rownum
select sub.* from (
    select e.job_id, max(j.job_title) job_title, avg(e.salary) avg_sal
      from Employees e inner join Jobs j on e.job_id = j.job_id
     group by e.job_id
     order by avg_sal desc) sub
 where rownum < 8;
 
-- 방식 2: rank()   
select sub2.job_title, sub2.avg_sal 
  from (
        select sub.*, rank() over (order by sub.avg_sal desc) ranking
          from (
            select e.job_id, max(j.job_title) job_title, avg(e.salary) avg_sal
              from Employees e inner join Jobs j on e.job_id = j.job_id
             group by e.job_id
             order by avg_sal desc) sub) sub2
 where ranking < 8;

select sub.* from ( 
    select e.job_id, max(j.job_title) job_title, avg(e.salary) avg_sal
      from Employees e inner join Jobs j on e.job_id = j.job_id
     group by e.job_id
     order by avg_sal desc) sub
 where rownum < 8;
 
  
-- 4) 자신의 매니저 보다 더 많은 급여를 받는 사람 목록
-- 방식 1
select sub.*
  from (
        select e.employee_id, e.salary, e.manager_id,
               (select salary from Employees where employee_id = e.manager_id) mgr_sal
          from Employees e
       ) sub
 where sub.salary > sub.mgr_sal;
 
-- 4) 방식2
select e.employee_id, e.last_name, e.salary
  from Employees es inner join Employees e on es.employee_id = e.manager_id
 where e.salary > es.salary;
 
-- 5) Job title이 Sales Representative인 직원 중에서, 급여가 9,000 ~ 10,000 인 직원들의 이름과 급여를 출력하시오.
-- select e.first_name || ' ' || e.last_name as emp_name, e.salary
select concat(concat(e.first_name, ' '), e.last_name) as emp_name, e.salary
  from Employees e inner join Jobs j on e.job_id = j.job_id
 where j.job_title = 'Sales Representative'
   and e.salary between 9000 and 10000
 order by e.salary desc;
   
select concat(concat(e.first_name, ' '), e.last_name) as emp_name, e.salary
  from Employees e
 where job_id = (select job_id from Jobs where job_title='Sales Representative')
   and e.salary between 9000 and 10000;
   
   
-- 6)
select min(j.job_title) job_title, sum(e.salary) sum_sal
  from Employees e inner join Jobs j on e.job_id = j.job_id
 group by e.job_id
 having sum(e.salary) > 30000
 order by sum(e.salary) desc;
 
select sub.*
  from ( select min(j.job_title) job_title, sum(e.salary) sum_sal
          from Employees e inner join Jobs j on e.job_id = j.job_id
         group by e.job_id ) sub
 where sub.sum_sal > 30000
 order by sub.sum_sal desc;
 
-- 7)
select sub.*
  from (
        select l.city, round(avg(e.salary)) avg_sal
          from Employees e inner join Departments d on e.department_id = d.department_id
                           inner join Locations l on d.location_id = l.location_id
         group by l.city
         order by avg_sal desc) sub
 where rownum <= 3;
 
-- 8)
select to_char(e.hire_date, 'YYYY') hire_year, round(avg(e.salary)) avg_sal
  from Employees e inner join Jobs j on e.job_id = j.job_id
 where j.job_title = 'Sales Manager'
 group by to_char(e.hire_date, 'YYYY')
 order by to_char(e.hire_date, 'YYYY');

-- 9)
select l.city, avg(e.salary) avg_sal, count(*) emp_cnt
  from Locations l inner join Departments d on l.location_id = d.location_id
                  inner join Employees e on d.department_id = e.department_id
 group by l.city
 having count(*) < 10
 order by avg_sal;
 
-- 10)
select e.employee_id, e.last_name, j.job_id
  from Jobs j inner join Job_history jh on j.job_id = jh.job_id
              inner join Employees e on jh.employee_id = e.employee_id
 where j.job_title = 'Public Accountant'
   and e.job_id <> j.job_id;  
   
select * from Employees where job_id ='AC_ACCOUNT';

-- 11)
select e.employee_id, e.first_name, e.last_name, NVL(d.department_name, '<Not Assigned>') department_name
  from Employees e left outer join Departments d on e.department_id = d.department_id
 where to_char(hire_date, 'YYYY') = '2007';

-- 12)
-- 부서는 생각하지 않고 급여로만 필터링
select ee.last_name, d.department_name
  from Employees ee inner join Departments d on ee.department_id = d.department_id
 where ee.salary in (select min(e.salary) min_sal
          from Employees e
         where e.department_id is not null
         group by e.department_id)
 order by d.department_name, ee.last_name;
 
-- 같은 부서, 같은 급여 (최종 답)
select dd.department_name, ee.employee_id, ee.last_name, ee.salary, min_sal
  from (select e.department_id, min(e.salary) min_sal
          from Employees e
         where e.department_id is not null
         group by e.department_id) sub inner join Employees ee 
                                               on sub.department_id = ee.department_id
                                              and ee.salary = sub.min_sal
                                       inner join Departments dd
                                               on ee.department_id = dd.department_id
 order by ee.department_id, ee.last_name;
 

-- 13)
-- 방식1: rownum 사용
select subsub.*
  from (select rownum rn, sub.*
          from (select e.last_name, e.first_name, e.salary
                  from Employees e
                 order by e.salary desc) sub ) subsub
 where rn between 6 and 10;
 
 
-- 방식 2: rank() 사용
select sub.*
  from (select e.last_name, e.first_name, e.salary,
            rank() over (order by e.salary desc) ranking
          from Employees e) sub
 where ranking between 6 and 10;
 
 
-- 14) 
select e.first_name, e.salary, d.department_name
  from Employees e inner join Departments d on e.department_id = d.department_id
 where d.department_name = 'Sales'
   and e.salary < (select avg(salary) from Employees where department_id = 100);


-- 15)
select min(d.department_name) department_name, to_char(e.hire_date, 'MM'), count(*) emp_cnt
  from Employees e inner join Departments d on e.department_id = d.department_id
 group by e.department_id, to_char(e.hire_date, 'MM')
 having count(*) >= 5
 order by department_name, to_char(e.hire_date, 'MM');

select min(d.department_name) department_name, to_char(e.hire_date, 'MM'), count(*) emp_cnt
  from Employees e inner join Departments d on e.department_id = d.department_id
 where e.department_id in
            (select department_id from Employees group by department_id having count(*) >= 5)
 group by e.department_id, to_char(e.hire_date, 'MM')
 order by department_name, to_char(e.hire_date, 'MM');
 
 
-- 16)
select sub.*
  from (select d.department_name, e.first_name, e.salary, e.commission_pct
          from Employees e inner join Departments d on e.department_id = d.department_id
         order by NVL(e.commission_pct,0) desc) sub
 where rownum <= 40
 order by sub.salary desc;
 
select hire_date, to_char(hire_date, 'Mon') from Employees;

select * from Job_history;
select * from Jobs;
select sysdate - 1 from dual;




