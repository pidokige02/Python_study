create table Grade(
    id int unsigned not null auto_increment primary key,
    midterm tinyint unsigned not null default 0,
    finalterm tinyint unsigned not null default 0,
    enroll int unsigned,
    constraint foreign key fk_enroll(enroll) references Enroll(id)
);

desc Grade;
show create table Grade;
desc Enroll;

insert into Grade(enroll, midterm, finalterm)
 select id, ceil((0.5 + rand() / 2) * 100), mod(id, 50) + 50 from Enroll;
 
select count(*), (select count(*) from Enroll) from Grade;
select min(midterm), min(finalterm), max(midterm), max(finalterm) from Grade;

-- 6-3 report
select sub.*,
    (case when avr >= 90 then 'A'
          when avr >= 80 then 'B'
          when avr >= 70 then 'C'
          else 'F' end) '평점'
  from (
        select sbj.name '과목명', stu.name stu_name, g.midterm, g.finalterm,
                (g.midterm + g.finalterm) total, (g.midterm + g.finalterm) / 2 avr
          from Grade g inner join Enroll e on g.enroll = e.id
                       inner join Subject sbj on e.subject = sbj.id
                       inner join Student stu on e.student = stu.id
       ) sub;     
       

  
-- 6-4 report
select max(sbj.name) sbj_name, avg(g.midterm + g.finalterm) / 2 avr, count(*) stu_cnt,
    (select ss.name
      from Grade gg inner join Enroll ee on gg.enroll = ee.id
                   inner join Student ss on ee.student = ss.id
     where ee.subject = sbj.id
     order by (gg.midterm + gg.finalterm) desc, gg.finalterm desc limit 1) '최고득점자'
  from Grade g inner join Enroll e on g.enroll = e.id
               inner join Subject sbj on e.subject = sbj.id
 group by sbj.id;
 
select max(sbj.name) sbj_name, avg(g.midterm + g.finalterm) / 2 avr, count(*) stu_cnt,
    (select (select name from Student where id = ee.student)
      from Grade gg inner join Enroll ee on gg.enroll = ee.id
     where ee.subject = sbj.id
     order by (gg.midterm + gg.finalterm) desc, gg.finalterm desc limit 1) '최고득점자'
  from Grade g inner join Enroll e on g.enroll = e.id
               inner join Subject sbj on e.subject = sbj.id
 group by sbj.id;
 
 select * from ClubMember;
 

select max(stu.name) stu_name, count(*) sbj_cnt,
                sum(g.midterm + g.finalterm) total, 
                round(avg(g.midterm + g.finalterm) / 2, 2) avr
          from Grade g inner join Enroll e on g.enroll = e.id
                       inner join Subject sbj on e.subject = sbj.id
                       inner join Student stu on e.student = stu.id
    group by e.student;
 
select * from Enroll order by student;

alter table jjj rename to qqq;
 
select concat('aaa', 'bbb');
 
select max(g.midterm + g.finalterm) total
  from Grade g inner join Enroll e on g.enroll = e.id
 where e.subject = 1
 order by (g.midterm + g.finalterm) desc, g.finalterm desc limit 1;
 
 
-- ---------------------------------- 문제 3 ------------------
create table ClubMember(
    id smallint unsigned not null auto_increment primary key,
    club smallint unsigned not null,
    student int unsigned not null,
    level tinyint(1) unsigned not null default 0,
    constraint foreign key fk_club(club) references Club(id),
    constraint foreign key fk_student(student) references Student(id)
);

select * from Club;
select * from ClubMember;


insert into ClubMember(club, student, level)
 select id, leader, 2 from Club where leader is not null;
 
alter table Club drop foreign key Club_ibfk_1;
alter table Club drop index fk_leader_student;
alter table Club drop column leader;

insert into ClubMember(club, student)
select 1, id from Student
 where id not in (select student from ClubMember where club = 1)
 order by rand() limit 50;
 
insert into ClubMember(club, student)
select 3, id from Student
 where id not in (select student from ClubMember where club = 3)
 order by rand() limit 50;
 
insert into ClubMember(club, student)
select 4, id from Student
 where id not in (select student from ClubMember where club = 4)
 order by rand() limit 50;
 
select * from (select c.id cid, s.id from Club c, Student s order by rand() limit 150) sub
 order by cid;
 
insert into ClubMember(club, student)
select c.id cid, s.id from Club c, Student s order by rand() limit 150;

update ClubMember set level=1
 order by rand() limit 15;
 
delete from ClubMember where level <> 3;
select count(*) from ClubMember;

select * from ClubMember where level=1;

update ClubMember set level = 1 where id = 72;

truncate table ClubMember;

select club, count(*) from ClubMember group by club;
select club, student from  ClubMember group by club, student having count(*) > 1;

select * from ClubMember where club = 3 and student=200;

show create table Club;
desc ClubMember;
 
 
-- --------------- 문제 4 ----------------
create table Dept(
    id smallint unsigned not null auto_increment primary key,
    name varchar(31) not null,
    prof smallint unsigned null,
    student int unsigned null,
    constraint foreign key fk_prof(prof) references Prof(id) on delete set null,
    constraint foreign key fk_student(student) references Student(id) on delete set null
);

insert into Dept(name, prof)
select '국문학과', id from Prof order by rand() limit 5;

select * from Dept;

update Dept set name=substring('국문학과,영문학과,물리학과,사회학과,역사학과', (id - 1) * 5 + 1, 4);

select substring('국문학과,영문학과,물리학과,사회학과,역사학과', (id - 1) * 5 + 1, 4) from Dept;
select substring('국문학과,영문학과,물리학과,사회학과,역사학과', id * 5 - 4, 4) from Dept;

select substring('국문학과,영문학과,물리학과,사회학과,역사학과', 1, 4);
select substring('국문학과,영문학과,물리학과,사회학과,역사학과', 6, 4);
select substring('국문학과,영문학과,물리학과,사회학과,역사학과', 11, 4);

-- student 학과배정
alter table Student add column dept smallint unsigned;
alter table Student add constraint foreign key fk_dept(dept) references Dept(id);

select * from Student;
update Student set dept=(select id from Dept order by rand() limit 1);

-- 과대표
update Dept d set student = (select id from Student where dept=d.id order by rand() limit 1);

desc Prof;
 
 
-- --------- 문제 5 ---------------
create table Classroom(
    id smallint unsigned not null auto_increment primary key,
    name varchar(31) not null
);

truncate table Classroom;

insert into Classroom(name)
 select concat((id + 200), '호') from Subject;
 
select id from Subject;

select * from Classroom;

alter table Subject add column classroom smallint unsigned;
alter table Subject add constraint foreign key fk_classroom(classroom) references Classroom(id);

select * from Subject;
update Subject set classroom = (11 - id);
 
 
 
 
 
 
 
 
 
 
 
 
 