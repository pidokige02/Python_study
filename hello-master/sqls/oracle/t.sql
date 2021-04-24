select sysdate, current_timestamp from dual;

select to_char(sysdate, 'YYYY-mm-dd HH24:MI:SS') from dual;

select to_char(current_timestamp, 'YYYY-mm-dd HH:MI:SS AM') from dual;

select to_char(CURRENT_TIMESTAMP, 'WW W DDD RM DY PM TZD')
  from dual;

select to_char(tsz, 'J'), to_char(tsz, 'YY-MM-DD HH24:MI:SS') from Test;

select power(2,3), sqrt(2) from dual;

select to_date('2018-12-25 12:22:44', 'YYYY-MM-DD HH24:MI:SS') from dual;


select manager_id, NVL(manager_id, 12), uid, user from Employees;
select manager_id as "매니저 ID", 'abc' "abc", NVL(manager_id, 12), uid, user from Employees;

select decode(employee_id, 100, 'one', 200, 'two', 150, 'ten', 'none') from Employees;
select (case employee_id when 100 then 'one' else 'none' end) from Employees;

select * from Employees;

select USERENV('sid') from dual;

desc Employees;

select max(salary) from Employees;
select least(1,5,3,2,9) from dual;

select replace('abc', 'bc', 'x') from dual;


create table Test (
	ts   timestamp,
	tsz  timestamp with time zone,
	ts0  timestamp(0)
);

insert into Test(ts, tsz, ts0)
 values(SYSDATE, SYSDATE, SYSDATE);

select ts, tsz, ts0, lengthb(ts), lengthb(tsz),
       lengthb(ts0) from Test;
       
       
select salary, count(*) cnt from Employees group by salary order by cnt desc;

select stats_mode(salary) from Employees;


select employee_id, first_name, salary,
	  dense_rank() over(order by salary) Ranking
  from Employees;
 
select e.job_id, max(j.job_title), sum(e.salary) tot
  from Employees e inner join Jobs j on e.job_id = j.job_id
 group by e.job_id
 order by tot desc;
 
 
select NVL(department_id, 0) from Employees where department_id is null;

select employee_id, first_name from Employees where employee_id < 103
 UNION ALL
select first_name, employee_id from Employees where employee_id < 105;

