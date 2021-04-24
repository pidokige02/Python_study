SELECT * 
  FROM USER_SEQUENCES 
 WHERE SEQUENCE_NAME = UPPER('test_seq');
 
select employees_seq.currval from dual;


create sequence test_seq
 start with 1
 increment BY 1
 maxvalue 10000;
 
alter sequence test_seq increment BY 39;
alter sequence test_seq increment BY 1;
 
select test_seq.currval from dual;
select test_seq.nextval from dual;

create table T(id number, name varchar2(30));

insert into T(id, name) values(test_seq.nextval, '김삼수');

select * from T;

select * from v_emp_dept;

alter table Departments add emp_cnt number(5) default 0 not null;

update Departments d
        set emp_cnt = (select count(*) from Employees where department_id = d.department_id);

select * from Departments;

select get_mgr('IT') from dual;
select get_dept_name(80) from dual;

var v_mgr number;
EXEC sp_test(10, :v_mgr);
print v_mgr;

create TYPE obj_emp_list AS OBJECT 
( 
    emp_id number(6),
    first_name varchar2(20)
); 
create TYPE TYPE_Emp IS TABLE OF obj_emp_list ;



select * from Employees order by employee_id desc;

delete from Employees where employee_id = 212;

insert into Employees(employee_id, last_name, email, hire_date, job_id, department_id)
              values(employees_seq.nextval, 'hong1', 'hong1@daa.com', current_timestamp, 'AD_VP', 80);

desc Departments;

select * from v$version;

desc Employees;

select get_mgr('Sales') from dual;

drop function get_mgr;

var v_mgr number;
EXEC sp_test(10, :v_mgr);
print v_mgr;


select * from Employees order by employee_id desc;

delete from Employees where employee_id = 209;

select department_id from Employees where employee_id = 209;

insert into Employees(employee_id, first_name, last_name, email, hire_date, job_id, salary, manager_id, department_id)
            values(employees_seq.nextval, 'Jade', 'Jeon', 'aaa@bbb.com', current_timestamp, 'AC_MGR', 9800, 101, 100);

commit;

 SELECT * 
  FROM user_SEQUENCES 
 WHERE SEQUENCE_NAME = UPPER('employees_seq');
 
drop trigger tr_emps;

alter table Departments drop column emps;