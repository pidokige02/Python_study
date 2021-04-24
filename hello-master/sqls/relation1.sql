create table Club(
    id smallint unsigned not null auto_increment primary key,
    name varchar(31) not null,
    createdate timestamp not null default current_timestamp,
    leader int unsigned,
    constraint foreign key fk_leader_student(leader) references Student(id)
);

insert into Club(name, leader) values('미술부', 300);

select * from Club;

select c.*, s.name as 'student name' from Club c inner join Student s on c.leader = s.id;

create table Prof(
    id smallint unsigned not null auto_increment primary key,
    name varchar(31) not null,
    likecnt int not null default 0
);

select ceil(rand() * 100) from dual;

insert into Prof(name, likecnt)
 select name, ceil(rand() * 100) from Student order by rand() limit 100;

-- 과목별 학생수
select subject, count(*) from Enroll group by subject;

-- 동일과목(한과목)에 중복 학생 존재 여부 체크
select subject, student, count(*) from Enroll group by subject, student having count(*) > 1;


select * from Prof;
select * from Student;

insert into Subject(name, prof)
 select '국어', id from Prof order by rand() limit 10;
 
update Subject set name='화학' where name='국어' and id != 10 limit 1;
 
select * from Subject;

create table `Subject`(
    id smallint unsigned not null auto_increment primary key,
    name varchar(31) not null,
    prof smallint unsigned,
    constraint foreign key fk_prof_prof (prof) references Prof(id)
    on delete set null
);


create table Enroll(
    id int unsigned not null auto_increment primary key,
    subject smallint unsigned not null,
    student int unsigned not null
);

alter table Enroll add constraint foreign key fk_subject (subject) references Subject(id) on delete cascade;
alter table Enroll add constraint foreign key fk_student (student) references Student(id) on delete cascade;


CREATE TABLE `Club` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(31) NOT NULL,
  `createdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `leader` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_leader_student` (`leader`),
  CONSTRAINT `Club_ibfk_1` FOREIGN KEY (`leader`) REFERENCES `Student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


desc Student;