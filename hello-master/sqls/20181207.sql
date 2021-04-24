desc Subject;
show variables like '%commit%';

-- 임시테이블을 활용하여 가나다순 과목명 한줄로 표현
create temporary table t_aaa(nm varchar(31));

insert into t_aaa(nm) select name from Subject order by name;

select group_concat(nm) from t_aaa;



select group_concat(name) from Subject order by name;
select * from Subject;

START TRANSACTION;

update Student set name = '111' where id = 1;


commit;

START TRANSACTION;

asdfdsfdsafdfs

select name from Student where id = 1;


commit; 

rollback;

-- 서울지역 과목별 성별(남녀) 학생수
select subject_name, gender, sum(student_count) from (
    select min(sbj.name) subject_name, 
        (case s.gender when 1 then '남' else '여' end) as gender, 
        count(*) as student_count
      from Enroll e inner join Student s on e.student = s.id
                    inner join Subject sbj on e.subject = sbj.id
     where s.addr = '서울'
     group by sbj.id, s.gender
     order by subject_name, s.gender desc) sub
 group by subject_name, gender;
 
 replace into Test(id, name) values (25, 'ccc');
 insert into Test(name) values ('bbb') ;
 
select min(sub.name) subject_name,
                 (case stu.gender
                  when 1 then '남자'
                         else '여자' end) as 'gender', count(*) as 'num of students'
from Enroll en inner join Student stu on en.student = stu.id
               inner join Subject sub on en.subject = sub.id
where stu.addr = '서울'
group by sub.id, stu.gender
order by subject_name asc, stu.gender desc;
 
 select * from Test order by id desc;
 
select id, mod(id, 2) from Test;

select CAST('2018-12-31 11:22:22.123' AS DATETIME);

select CAST( 1.567 AS Signed Integer ), CONVERT( 1.567, Signed Integer);

select str_to_date('12/03/2018', '%d/%m/%Y');

select concat_ws(', ', 'aaa', 'bbb', 'ccc', 'ddd');

select addr, group_concat(name) from Student group by addr;

select addr, if (addr > 90, '*', ''), group_concat(name) as 'student names' from Student group by addr;
 
select addr, avg(id) from Student group by addr;

select name, ifnull(leader, '부재중') from Club;
 
show index from Student;
 
select * from Subject;



