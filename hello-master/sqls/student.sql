-- append gender column
alter table Student add column gender bit not null default 0;

update Student set gender = (case when name like '%혜%' or name like '%솔%' 
                                or name like '%숙%' or name like '%민%'
                                or name like '%현%'  or name like '%희%' 
                                or name like '%영%' or name like '%주%' then 0 else 1 end)
 where id > 0;
                                
update Student set gender = 1
 where not (name like '%혜%' or name like '%솔%' 
                                or name like '%숙%' or name like '%민%'
                                or name like '%현%'  or name like '%희%' 
                                or name like '%영%' or name like '%주%')
  and id > 0;
  
select gender, count(*) from Student group by gender;

select * from Student;


update Student set gender = mod(id, 2);

select * from Student;

select count(*) from Student
 where name like '%혜%' or name like '%솔%' or name like '%숙%' or name like '%민%'
   or name like '%현%'  or name like '%희%' or name like '%영%' or name like '%주%';



select birth, replace(substring(birth, 3), '-', '') from Student;

update Student set birth = replace(substring(birth, 3), '-', '')
 where id > 0 and birth is not null;
 
select * from Student order by id desc;

select * from Student where name not like '%정_';
select * from Student where id not in (10, 20, 30);
select * from Student where id = 10 or id = 20 or id = 30;
select * from Student where id not between 10 and 30;
select * from Student where id in (select id from Test where id between 5 and 30);

-- ㅂ으로 시작하는 성씨의 학생만 추출!
select * from Student where name between '바' and '빟';
select * from Student where substring(name,3) >= '바' and  name < '사';

-- email이 a로 시작하고, tel의 가운데 숫자가 9000 보다 큰 학생 추출
select * from Student where email like 'a%' and tel like '010-9%';

select * from Student order by addr, name desc;
select * from Student order by rand();
select * from Student order by name limit 30, 50;

-- 강원지역 학생중 어린순서로 11번째부터 5명 추출
select * from Student where addr = '강원' order by birth desc limit 10, 5;

-- 지역별 학생수
select addr, count(*) as cnt, avg(id) from Student group by addr order by cnt desc;

-- 지역별 학생수가 330명 이상인 지역들만 추출
select addr, count(*) as cnt, avg(id) from Student
 group by addr having cnt > 330;
 
 select name, birth, addr from Student limit 10;
 
select name, birth, addr,
   (case addr when '서울' then 'SE' 
              when '부산' then 'PS'
              else 'GD' end),
   (case when birth like '7%' then '아재'
         when birth like '8%' then '젊은이'
         else '청춘' end)
 from Student limit 10;


-- distinct 
select distinct(birth) from Student s where birth='700601';
select birth from Student s where birth='700601';
select count(distinct birth) from Student s where birth='700601';

select * from Test;
delete from Test where id = 8;

insert into Test(name) select name from Student where id < 10;

update Test set name=(select name from Student where id>2997) where id=3;



select name from Student where id>2997;

insert into Test(name) values('김이수'), ('김칠수');

insert into Test set name='김삼수';

Show table status;
show tables;
show databases;

drop table Test3;

alter table Student drop column tt;

select tel, count(*) as cnt from Student group by tel order by cnt desc;

truncate table Student;

create table Student(
    id int unsigned not null auto_increment comment '학번',
    name varchar(32) not null comment '학생명',
    addr varchar(30),
    birth date,
    tel varchar(15),
    email varchar(31),
    regdt timestamp default current_timestamp not null,
    primary key(id)
);

alter table Student add column tt int;
select 0.1 + 0.1;
select CAST(10.49 AS signed integer), CONVERT( 10.6123, decimal);
             
show index from Student;
show table status;

select *, replace(substring(birth, 3),'-','') from Student s;

explain select s.* from (select name, addr, email from Student where tel like '010-9999%') s
 where s.email like 'bbb%';
 
select tel from Student group by tel having count(*) > 1;


select * from t_student;

alter table t_student drop column email;


INSERT INTO `dooodb`.`t_student`
(`name`,`addr`,`birth`,`tel`,`email`)
VALUES('김오수', 'ㅁㅁㅁ', '121212', '010', 'ㄷaa@dfd');

delete from t_student where id > 0;
truncate t_student;

insert into t_student select * from Student;

create table t_student like Student;

update Student set tel='010-2222-2323' where id = 4;

CREATE TABLE `t_student` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '학번',
  `name` varchar(32) NOT NULL COMMENT '학생명',
  `addr` varchar(30) DEFAULT NULL,
  `birth` varchar(10) DEFAULT NULL,
  `tel` varchar(15) DEFAULT NULL,
  `email` varchar(31) DEFAULT NULL,
  `regdt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `Student` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '학번',
  `name` varchar(32) NOT NULL COMMENT '학생명',
  `addr` varchar(30) DEFAULT NULL,
  `birth` date DEFAULT NULL,
  `tel` varchar(15) DEFAULT NULL,
  `email` varchar(31) DEFAULT NULL,
  `regdt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


ALTER DATABASE dooodb DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

show processlist;

show variables like '%session%';


desc Test2;
CREATE TABLE `Test3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ttt` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


show create table Test;

insert into Test(name) values('김일수');

select * from Test;

CREATE TABLE `Test` (
  `id` tinyint(3) unsigned NOT NULL AUTO_INCREMENT,
  `name` char(5) CHARACTER SET latin1 NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
